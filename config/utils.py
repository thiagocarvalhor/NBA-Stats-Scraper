import calendar
import datetime

# PEGANDO A DATA DO DIA E DO DIA ANTERIOR
def handleDate():
    # A DATA ATUAL
    date_now = datetime.date.today()
    # O ULTIMO DIA DO MÊS
    last_day_of_month = datetime.date(date_now.year, date_now.month, calendar.monthrange(
        date_now.year, date_now.month)[1]).day
    # O DIA ANTERIOR
    yesterday = datetime.date.today(
    ) - datetime.timedelta(days=1) if date_now.day != 1 else date_now

    return date_now, last_day_of_month, yesterday
