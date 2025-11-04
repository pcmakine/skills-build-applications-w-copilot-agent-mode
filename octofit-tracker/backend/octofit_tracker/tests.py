from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Team, Activity, Workout, Leaderboard

class UserModelTest(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = get_user_model().objects.create_user(username='activityuser', password='testpass')
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5.0)
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Morning Cardio', description='Cardio session', duration=45)
        self.assertEqual(workout.name, 'Morning Cardio')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        user = get_user_model().objects.create_user(username='leaderuser', password='testpass')
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
