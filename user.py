import math
from datetime import datetime


class User:

    def __init__(self):

        self.current_caffeine = 0.0
        self.last_dose_time = datetime.now()

    def check_caffeine(self):
        last_dose_time_delta = datetime.now() - self.last_dose_time
        time_since_last_dose = last_dose_time_delta.total_seconds() / 3600

        decay = math.pow(0.5, time_since_last_dose / 6)
        new_caffeine = self.current_caffeine * decay
        return new_caffeine

    def add_dose(self, mg: float):
        self.current_caffeine = self.check_caffeine() + mg
        self.last_dose_time = datetime.now()

    def reset_dose(self):
        self.current_caffeine = 0.0
