from applications.models import Application
from datetime import datetime, timezone, timedelta

def get_basic_metrics(user):
    pass

def get_evolution_data(user):
    pass

def get_average_applications(user):
    applications = Application.objects.filter(user=user).order_by("application_date")
    number_of_days = datetime.now(timezone.utc).date() - applications.first().application_date.date() + timedelta(days=1)
    number_of_apps = applications.count()
    average = number_of_apps / number_of_days.days
    return average