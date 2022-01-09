import datetime


class Week_type():

    def type_of_week():
        return 'NUM' if datetime.datetime.now().isocalendar()[1] % 2 == 0 else 'DEN'
