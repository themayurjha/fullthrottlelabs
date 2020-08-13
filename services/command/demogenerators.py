import string
import random
import names
import pytz
from datetime import datetime, timedelta


'''
RandomNameGenerator generates random names based on gender. It has two class
methods get_male_name which returns male name and get_female_name which
returns Female name
'''


class RandomNameGenerator:

    @classmethod
    def get_male_name(cls):
        return names.get_full_name("male")

    @classmethod
    def get_female_name(cls):
        return names.get_full_name("Female")


'''
RandomIdGenerator generates 9 characters long alphanumeric string.
This is used for coloumn id of model Members
'''


class RandomIdGenerator:

    @classmethod
    def get_id(cls):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))


'''
RandomTimeZone is used to get random timezone from
pytz module.
'''


class RandomTimeZone:

    @classmethod
    def get_time_zone(cls):
        return random.choice(pytz.all_timezones)


'''
RandomDate generates random date time stamp for Members activity models.
First it takes the current time as end time and the start time is calculated by subtracting end time
with random minutes which is generated using random module. It returns start_time and end_time
'''

class RandomDate:

    @classmethod
    def gen_datetime(self):
        end_time = datetime.now()
        start_time = end_time - timedelta(minutes=60 * random.random())
        return start_time, end_time

