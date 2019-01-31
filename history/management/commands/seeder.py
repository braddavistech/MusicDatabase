from django.core.management.base import BaseCommand
from django_seed import django_seed
import random
seeder = Seed.seeder()
from history.models import *


class Command(BaseCommand):
  def handle(self, *args, **options):
    adjectives = ["Ugly", "Pretty", "Fat", "Skinny"]

    nouns = ["Ball", "Car", "Bookcase", "Battery", "Computer"]