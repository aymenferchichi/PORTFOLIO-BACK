from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path

from .models import Journey


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    change_list_template = 'admin/journeys/journey/change_list.html'
    list_display = ('display_order', 'title', 'subcategory', 'year', 'slug', 'accent_preview')
    list_display_links = ('title',)
    list_editable = ('display_order',)
    ordering = ('display_order',)
    list_filter = ('subcategory',)
    search_fields = ('title', 'slug', 'year', 'eyebrow', 'detail', 'summary')
    prepopulated_fields = {'slug': ('title',)}
    fields = (
        'display_order',
        'title',
        'slug',
        'year',
        'eyebrow',
        'subcategory',
        'client_label',
        'project_scope',
        'outcome_highlight',
        'detail',
        'summary',
        'focus',
        'deliverables',
        'accent',
    )

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                'dashboard/',
                self.admin_site.admin_view(self.dashboard_view),
                name='journeys_journey_dashboard',
            ),
        ]
        return custom_urls + urls

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['dashboard_url'] = 'dashboard/'
        return super().changelist_view(request, extra_context=extra_context)

    def dashboard_view(self, request):
        journeys = list(Journey.objects.all())
        accent_groups = []
        seen_accents = set()

        for journey in journeys:
            if journey.accent in seen_accents:
                continue

            seen_accents.add(journey.accent)
            accent_groups.append(
                {
                    'accent': journey.accent,
                    'count': sum(1 for item in journeys if item.accent == journey.accent),
                }
            )

        context = {
            **self.admin_site.each_context(request),
            'title': 'Journey dashboard',
            'total_journeys': len(journeys),
            'first_milestone': journeys[0] if journeys else None,
            'latest_milestone': journeys[-1] if journeys else None,
            'journeys': journeys,
            'accent_groups': accent_groups,
            'opts': self.model._meta,
        }
        return TemplateResponse(request, 'admin/journeys/dashboard.html', context)

    @admin.display(description='Accent')
    def accent_preview(self, obj):
        return obj.accent