from django.contrib import admin
from django.db.models import Count
from django.template.response import TemplateResponse
from django.utils import timezone
from django.urls import path
from urllib.parse import urlencode

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
	change_list_template = 'admin/contacts/contactmessage/change_list.html'
	list_display = ('name', 'email', 'subject', 'estimator_project_type', 'status', 'created_at')
	list_filter = ('status', 'created_at')
	search_fields = ('name', 'email', 'subject', 'message')
	readonly_fields = (
		'created_at',
		'updated_at',
		'estimator_project_type',
		'estimator_page_scope',
		'estimator_timeline',
		'estimator_support_level',
		'estimator_budget_min',
		'estimator_budget_max',
	)

	def get_urls(self):
		urls = super().get_urls()
		custom_urls = [
			path(
				'dashboard/',
				self.admin_site.admin_view(self.dashboard_view),
				name='contacts_contactmessage_dashboard',
			),
		]
		return custom_urls + urls

	def changelist_view(self, request, extra_context=None):
		extra_context = extra_context or {}
		extra_context['dashboard_url'] = 'dashboard/'
		return super().changelist_view(request, extra_context=extra_context)

	def dashboard_view(self, request):
		queryset = ContactMessage.objects.all()
		selected_status = request.GET.get('status', '').strip()
		selected_window = request.GET.get('window', 'all').strip() or 'all'

		if selected_status in dict(ContactMessage.Status.choices):
			queryset = queryset.filter(status=selected_status)

		window_options = {
			'all': None,
			'7d': 7,
			'30d': 30,
			'90d': 90,
		}
		window_days = window_options.get(selected_window)
		if window_days:
			queryset = queryset.filter(created_at__gte=timezone.now() - timezone.timedelta(days=window_days))

		total_messages = queryset.count()
		status_breakdown = list(
			queryset.values('status').annotate(total=Count('id')).order_by('status')
		)
		for item in status_breakdown:
			item['label'] = ContactMessage.Status(item['status']).label
			item['percentage'] = round((item['total'] / total_messages) * 100, 1) if total_messages else 0

		status_filters = [
			{
				'label': 'All statuses',
				'value': '',
				'url': f"?{urlencode({'window': selected_window})}" if selected_window != 'all' else '?',
				'active': selected_status == '',
			}
		]
		for value, label in ContactMessage.Status.choices:
			params = {'status': value}
			if selected_window != 'all':
				params['window'] = selected_window
			status_filters.append(
				{
					'label': label,
					'value': value,
					'url': f"?{urlencode(params)}",
					'active': selected_status == value,
				}
			)

		window_filters = []
		for key, label in [('all', 'All time'), ('7d', 'Last 7 days'), ('30d', 'Last 30 days'), ('90d', 'Last 90 days')]:
			params = {}
			if selected_status:
				params['status'] = selected_status
			if key != 'all':
				params['window'] = key
			window_filters.append(
				{
					'label': label,
					'value': key,
					'url': f"?{urlencode(params)}" if params else '?',
					'active': selected_window == key,
				}
			)

		recent_messages = queryset[:10]
		context = {
			**self.admin_site.each_context(request),
			'title': 'Contact message dashboard',
			'total_messages': total_messages,
			'new_messages': queryset.filter(status=ContactMessage.Status.NEW).count(),
			'replied_messages': queryset.filter(status=ContactMessage.Status.REPLIED).count(),
			'status_breakdown': status_breakdown,
			'status_filters': status_filters,
			'window_filters': window_filters,
			'selected_status': selected_status,
			'selected_window': selected_window,
			'recent_messages': recent_messages,
			'opts': self.model._meta,
		}
		return TemplateResponse(request, 'admin/contacts/dashboard.html', context)
