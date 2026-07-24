from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class JourneyApiTests(APITestCase):
    def test_list_returns_seeded_journeys_in_order(self):
        response = self.client.get('/api/journeys/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.data[0]['slug'], 'foundation')
        self.assertEqual(response.data[-1]['slug'], 'current-direction')

    def test_detail_returns_journey_by_slug(self):
        response = self.client.get('/api/journeys/ui-ux-expansion/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'UI / UX expansion')
        self.assertEqual(response.data['display_order'], 3)

    def test_journey_dashboard_requires_admin_authentication(self):
        response = self.client.get(reverse('admin:journeys_journey_dashboard'))

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)

    def test_admin_can_open_journey_dashboard(self):
        user = get_user_model().objects.create_superuser(
            username='journey-admin',
            email='journey-admin@example.com',
            password='TempPass123!',
        )
        self.client.force_login(user)

        response = self.client.get(reverse('admin:journeys_journey_dashboard'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
