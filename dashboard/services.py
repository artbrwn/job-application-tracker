from applications.models import Application
from datetime import datetime, timezone, timedelta
from collections import Counter

def get_basic_metrics(user):
    applications = Application.objects.filter(user=user).order_by("application_date")
    metrics = {}
    if applications:
        rejected = len([a for a in applications if a.status == "REJ_DIR" or a.status == "REJ_REV"])
        metrics = {
                "total": applications.count(),
                "rejected": rejected,
                "percentage_rejected": get_percentage_rejected(user),
                "average_time_response": get_average_time_response(user)
            }

    return metrics

def get_evolution_data(user):
    applications = Application.objects.filter(user=user).order_by("application_date")

    start_date = applications.first().application_date.date()
    end_date = datetime.now().date()

    current_date = start_date
    date_range = []
    while current_date <= end_date:
        date_range.append(current_date)
        current_date += timedelta(days=1)

    labels = [date.strftime("%Y-%m-%d") for date in date_range]

    # ----- Applications data -----
    applications_per_day = Counter(str(app.application_date.date()) for app in applications)
    applications_values = []
    for date in date_range:
        date_str = date.strftime("%Y-%m-%d")
        applications_values.append(applications_per_day.get(date_str, 0))

    # ----- Rejections data -----
    rejections_per_day = Counter(str(app.response_date) for app in applications if app.status == "REJ_REV" or app.status == "REJ_DIR")
    rejections_values = []
    for date in date_range:
        date_str = date.strftime("%Y-%m-%d")
        rejections_values.append(rejections_per_day.get(date_str, 0))

    evolution_data = {
        "labels": labels,
        "datasets": [{
            "label": "Postulaciones por día",
            "data": applications_values,
            "fill": False,
            "borderColor": "rgb(13, 110, 253)",
            "tension": 0.1
        },
        {
            "label": "Rechazos por día",
            "data": rejections_values,
            "fill": False,
            "borderColor": "rgb(220, 53, 69)",
            "tension": 0.1
        }]
    }
    return evolution_data


def get_average_applications_per_day(user):
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