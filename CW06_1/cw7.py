  
from datetime import date, timedelta

class DateHelper:
    @classmethod
    def get_next_day(cls, current_date):
        return current_date + timedelta(days=1)


current_date = date(2024, 6, 27)
next_day = DateHelper.get_next_day(current_date)
print(next_day)  
