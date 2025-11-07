from django.core.management.base import BaseCommand
from django.utils import timezone
from polls.models import Question, Choice


class Command(BaseCommand):
    help = 'Seed database with sample food-related poll questions'

    def handle(self, *args, **options):
        # Clear existing data
        Question.objects.all().delete()
        
        # Create food-related questions
        question1 = Question.objects.create(
            question_text="What's your favorite type of cuisine?",
            pub_date=timezone.now()
        )
        
        question2 = Question.objects.create(
            question_text="What's the best meal of the day?",
            pub_date=timezone.now()
        )
        
        # Create choices for question 1
        Choice.objects.create(question=question1, choice_text="Italian", votes=0)
        Choice.objects.create(question=question1, choice_text="Mexican", votes=0)
        Choice.objects.create(question=question1, choice_text="Chinese", votes=0)
        Choice.objects.create(question=question1, choice_text="Indian", votes=0)
        
        # Create choices for question 2
        Choice.objects.create(question=question2, choice_text="Breakfast", votes=0)
        Choice.objects.create(question=question2, choice_text="Lunch", votes=0)
        Choice.objects.create(question=question2, choice_text="Dinner", votes=0)
        Choice.objects.create(question=question2, choice_text="Snack Time", votes=0)
        
        self.stdout.write(
            self.style.SUCCESS('Successfully seeded database with food polls!')
        )