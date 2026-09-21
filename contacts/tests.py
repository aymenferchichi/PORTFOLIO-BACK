from smtplib import SMTPAuthenticationError
from unittest.mock import patch

from django.core import mail
from django.test import override_settings
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


@override_settings(EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend')
class ContactMessageApiTests(APITestCase):
	def test_public_contact_submission_creates_message_and_sends_email(self):
		payload = {
			'name': 'Jane Client',
			'email': 'jane@example.com',
			'subject': 'Portfolio website',
			'phone': '+123456789',
			'message': 'I need a new website for my studio.',
			'estimator_project_type': 'Portfolio website',
			'estimator_page_scope': '3 to 5 pages',
			'estimator_timeline': '2 to 3 weeks',
			'estimator_support_level': 'Design and front-end build',
			'estimator_budget_min': 1800,
			'estimator_budget_max': 2600,
		}

		response = self.client.post('/api/contacts/', payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(len(mail.outbox), 1)
		self.assertIn('Portfolio contact: Portfolio website', mail.outbox[0].subject)
		self.assertEqual(response.data['name'], payload['name'])
		self.assertEqual(response.data['estimator_project_type'], payload['estimator_project_type'])
		self.assertIn('Project scope guide:', mail.outbox[0].body)

	@patch('contacts.views.send_mail', side_effect=SMTPAuthenticationError(535, b'Bad credentials'))
	def test_public_contact_submission_survives_email_auth_failure(self, _send_mail_mock):
		payload = {
			'name': 'Jane Client',
			'email': 'jane@example.com',
			'subject': 'Portfolio website',
			'phone': '+123456789',
			'message': 'I need a new website for my studio.',
		}

		response = self.client.post('/api/contacts/', payload, format='json')

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data['name'], payload['name'])
		self.assertIn('delivery_warning', response.data)

	def test_contact_dashboard_requires_admin_authentication(self):
		response = self.client.get(reverse('admin:contacts_contactmessage_dashboard'))

		self.assertEqual(response.status_code, status.HTTP_302_FOUND)
