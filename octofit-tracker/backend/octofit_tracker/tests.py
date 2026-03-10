from django.test import TestCase
from django.contrib.auth.models import User
from .models import User, Team, Activity, Leaderboard, Workout
from django.test import TestCase

class UserTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='testuser@example.com', team=self.team)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Test User')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.team.name, 'Test Team')

class TeamTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

class ActivityTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='testuser@example.com', team=self.team)
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30)

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.duration, 30)

class WorkoutTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='testuser@example.com', team=self.team)
        self.workout = Workout.objects.create(user=self.user, description='Test Workout', duration=45)

    def test_workout_creation(self):
        self.assertEqual(self.workout.description, 'Test Workout')
        self.assertEqual(self.workout.duration, 45)

class LeaderboardTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='testuser@example.com', team=self.team)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)