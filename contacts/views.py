import logging
from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .models import ContactMessage
from .serializers import ContactMessageSerializer


logger = logging.getLogger(__name__)


class ContactMessageViewSet(viewsets.ModelViewSet):
	queryset = ContactMessage.objects.all()
	serializer_class = ContactMessageSerializer

	def get_permissions(self):
		if self.action == 'create':
			permission_classes = [permissions.AllowAny]
		else:
			permission_classes = [permissions.IsAdminUser]

		return [permission() for permission in permission_classes]

	def _send_contact_email(self, contact_message):
		send_mail(
			subject=f"Portfolio contact: {contact_message.subject}",
			message=(
				f"Name: {contact_message.name}\n"
				f"Email: {contact_message.email}\n"
				f"Phone: {contact_message.phone or 'Not provided'}\n\n"
				f"Message:\n{contact_message.message}"
			),
			from_email=settings.DEFAULT_FROM_EMAIL,
			recipient_list=[settings.CONTACT_RECEIVER_EMAIL],
			fail_silently=False,
		)

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		contact_message = serializer.save()

		response_data = self.get_serializer(contact_message).data

		try:
			self._send_contact_email(contact_message)
		except (SMTPException, OSError, TimeoutError) as error:
			logger.exception('Contact message email delivery failed.')
			response_data['delivery_warning'] = (
				'Your message was saved, but email delivery is not configured correctly yet.'
			)

		headers = self.get_success_headers(response_data)
		return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)
