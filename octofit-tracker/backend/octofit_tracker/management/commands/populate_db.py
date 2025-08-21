
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

        # Insert test data
        users = [
            {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
            {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
            {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
            {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
            {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
            {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
        ]
        teams = [
            {"name": "Marvel", "members": ["Iron Man", "Captain America", "Black Widow"]},
            {"name": "DC", "members": ["Superman", "Batman", "Wonder Woman"]},
        ]
        activities = [
            {"user": "Superman", "activity": "Flight", "duration": 60},
            {"user": "Iron Man", "activity": "Suit Training", "duration": 45},
        ]
        leaderboard = [
            {"team": "Marvel", "points": 120},
            {"team": "DC", "points": 110},
        ]
        workouts = [
            {"name": "Strength", "suggestion": "Pushups, Squats"},
            {"name": "Cardio", "suggestion": "Running, Cycling"},
        ]

        for user in users:
            User.objects.create(**user)
        for team in teams:
            Team.objects.create(name=team["name"], members=team["members"])
        for activity in activities:
            Activity.objects.create(**activity)
        for entry in leaderboard:
            Leaderboard.objects.create(**entry)
        for workout in workouts:
            Workout.objects.create(**workout)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
