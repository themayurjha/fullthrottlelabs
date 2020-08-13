from django.core.management.base import BaseCommand, CommandError
from api.models import ActivityPeriods, Members
from services.command.demogenerators import RandomIdGenerator, RandomNameGenerator, RandomTimeZone, RandomDate
import random

class Command(BaseCommand):
    help = "Updates Database With Dummy Data"

    def __init__(self):
        self.count = 0


    def handle(self, *args, **options):
        while True:

            '''
            Count is used to keep track of how many rows have been inserted in the models
            '''
            if self.count == 10:
                break
            '''
            Generates random datetime stamps and saves it to ActivityPeriods Model.
            '''
            try:
                start, end = RandomDate.gen_datetime()
                activity = ActivityPeriods.objects.create(start_time=start, end_time=end)
                activity.save()
            except Exception as e:
                print(e, 'Error occurred when creating data for activity ')

            '''
            Generates random Id, name and timezone stamps and saves it to Members Model.
            '''

            try:
                ids = RandomIdGenerator.get_id()
                name = RandomNameGenerator.get_male_name()
                timezone = RandomTimeZone.get_time_zone()

                count = ActivityPeriods.objects.count()
                activity_obj1 = ActivityPeriods.objects.get(id=random.randint(1, count))
                activity_obj2 = ActivityPeriods.objects.get(id=random.randint(1, count))

                member = Members.objects.create(id=ids, real_name=name, tz=timezone)
                member.activity_periods.add(activity_obj2)
                member.activity_periods.add(activity_obj1)
                member.save()
            except Exception as e:
                print(e, "Error happened when creating data for Members. Please try again!!!")

            self.count += 1
