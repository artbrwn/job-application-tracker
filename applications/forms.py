from django.forms import ModelForm
from applications.models import Application

# Create the form class.
class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ["title", "company", "url", "location", "description", "required_experience", "status"]