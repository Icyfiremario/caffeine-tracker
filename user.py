import math
from datetime import datetime


class User:

    def __init__(self):

        self.current_caffeine = 0.0
        self.last_dose_time = datetime.now().hour + (datetime.now().minute / 60)

    def check_caffeine(self):
        time_since_last_dose = (datetime.now().hour + (datetime.now().minute / 60)) - self.last_dose_time

        decay = math.pow(0.5, time_since_last_dose / 6)
        self.current_caffeine *= decay
        return

    def add_dose(self, mg: float):
        self.check_caffeine()
        self.current_caffeine += mg
        self.last_dose_time = datetime.now().hour + (datetime.now().minute / 60)