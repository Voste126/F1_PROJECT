from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Race, LapTime, FantasyTeam, Driver, FantasyScore
import pandas as pd

class DashboardViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.race = Race.objects.create(name="Test Race")
        self.driver = Driver.objects.create(name="Test Driver")
        self.fantasy_team = FantasyTeam.objects.create(user=self.user, name="Test Team")
        self.fantasy_team.drivers.add(self.driver)
        FantasyScore.objects.create(fantasy_team=self.fantasy_team, score=100)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome to the F1 Dashboard!')

    def test_historical_comparison_view(self):
        response = self.client.get(reverse('historical_comparison'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'comparison_data')

    def test_create_fantasy_team_view_get(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get(reverse('create_fantasy_team'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'drivers')

    def test_create_fantasy_team_view_post(self):
        self.client.login(username='testuser', password='password')
        response = self.client.post(reverse('create_fantasy_team'), {
            'team_name': 'New Team',
            'drivers': [self.driver.id]
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation
        self.assertTrue(FantasyTeam.objects.filter(name='New Team').exists())

    def test_leaderboard_view(self):
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Team')

    def test_driver_profile_view(self):
        response = self.client.get(reverse('driver_profile', args=[self.driver.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Driver')

    def test_team_profile_view(self):
        response = self.client.get(reverse('team_profile', args=[self.fantasy_team.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'Team Profile for Team ID: {self.fantasy_team.id}')