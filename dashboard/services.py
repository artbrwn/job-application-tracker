from applications.models import Application
from datetime import datetime, timezone, timedelta

def get_basic_metrics(user):
    pass

def get_evolution_data(user):
    pass

def get_average_applications(user):
    applications = Application.objects.filter(user=user).order_by("application_date")
    if applications:
        number_of_days = datetime.now(timezone.utc).date() - applications.first().application_date.date() + timedelta(days=1)
        number_of_apps = len(applications)
        average = number_of_apps / number_of_days.days
    else:
        average = 0
    return average

def get_percentage_rejected(user):
    applications = Application.objects.filter(user=user).order_by("application_date")
    if applications:
        rejected = len([a for a in applications if a.status == "REJ_DIR" or a.status == "REJ_REV"])
        percentage = rejected * 100 / len(applications)
    else:
        percentage = 0
    return percentage

def get_average_time_response(user):
    applications = Application.objects.filter(user=user).order_by("application_date")
    if applications:
        days = []
        for application in applications:
            if not application.response_date:
                continue
            difference = application.response_date - application.application_date.date()
            days.append(difference.days)
        
        average = sum(days) / len(days)
    else:
        average = 0
    
    return average