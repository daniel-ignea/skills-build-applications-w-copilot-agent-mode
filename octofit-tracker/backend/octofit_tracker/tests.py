from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelSmokeTest(TestCase):
    def test_team_create(self):
        t = Team.objects.create(name='Test Team')
        self.assertEqual(str(t), 'Test Team')
    def test_user_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pw', team=t)
        self.assertEqual(str(u), 'test')
    def test_activity_create(self):
        t = Team.objects.create(name='Test Team')
        u = User.objects.create_user(username='test', email='test@example.com', password='pw', team=t)
        a = Activity.objects.create(user=u, type='run', duration=10, calories=100)
        self.assertEqual(str(a), 'test - run')
    def test_workout_create(self):
        w = Workout.objects.create(name='W', description='desc', duration=10)
        self.assertEqual(str(w), 'W')
    def test_leaderboard_create(self):
        t = Team.objects.create(name='Test Team')
        l = Leaderboard.objects.create(team=t, points=10)
        self.assertEqual(str(l), 'Test Team: 10')
