from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30)
        Activity.objects.create(user=batman, type='Cycling', duration=45)
        Activity.objects.create(user=superman, type='Swimming', duration=60)
        Activity.objects.create(user=captain, type='Walking', duration=20)

        # Create workouts
        Workout.objects.create(user=ironman, description='Chest workout', duration=40)
        Workout.objects.create(user=batman, description='Leg workout', duration=50)
        Workout.objects.create(user=superman, description='Core workout', duration=30)
        Workout.objects.create(user=captain, description='Arm workout', duration=25)

        # Create leaderboard
        Leaderboard.objects.create(user=ironman, points=100)
        Leaderboard.objects.create(user=batman, points=90)
        Leaderboard.objects.create(user=superman, points=95)
        Leaderboard.objects.create(user=captain, points=85)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
