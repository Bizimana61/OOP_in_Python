#Jerome Bizimana
#Alex Kanu

#File: restaurant.py
from datetime import datetime

class Restaurant:
    def __init__(self, business_id, name, address, city, state, postal_code, latitude=None, longitude=None, is_open=False, categories=None, hours=None):
        self.business_id = business_id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.latitude = latitude
        self.longitude = longitude
        self.is_open = bool(is_open)
        self.categories = categories.split(',')
        self.hours = hours if hours else {}

    def __str__(self):
        return f"{self.name} ({self.address} {self.city}, {self.state})"

    def is_category(self, cat):
        stripped_categories = [category.strip() for category in self.categories]
        return cat.strip() in stripped_categories

    def check_open(self, day, time):
        if not self.is_open:
            return False

        if day in self.hours:
            try:
                opening_time, closing_time = self.hours[day].split('-')
                time_format = "%H:%M"
                current_time = datetime.strptime(time, time_format)
                opening_time_dt = datetime.strptime(opening_time, time_format)
                closing_time_dt = datetime.strptime(closing_time, time_format)
                
                return opening_time_dt <= current_time <= closing_time_dt
            except ValueError:
                return False
        
        return False

