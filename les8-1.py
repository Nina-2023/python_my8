class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def date_transform(cls, date_string):
        day, month, year = date_string.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def validate(day, month, year):
        if 1 <= month <= 12:
            return True
        return False


date = Date('18-03-2023')
day, month, year = date.date_transform('18-03-2023')
print(date.validate(day, month, year))

