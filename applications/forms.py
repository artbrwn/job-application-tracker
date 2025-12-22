from django.forms import CharField, ModelForm, ValidationError
from applications.models import Application
from .models import Company

# Create the form class.
class ApplicationForm(ModelForm):
    company_name = CharField(
        max_length=100,
        label="Empresa",
        help_text="Escribe para crear nueva o seleccionar existente"
    )
    
    class Meta:
        model = Application
        fields = ["title", "url", "location", "description", 
                 "required_experience", "status", "response_date"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['response_date'].widget.input_type = 'date'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            if field.help_text:
                field.widget.attrs['placeholder'] = field.help_text

    def clean(self):
        cleaned_data = super().clean()
        response_date = cleaned_data.get('response_date')
        
        if self.instance and self.instance.pk:
            application_date = self.instance.application_date.date()
            print(f"Application date: {application_date}, Edited date: {response_date}")
            if response_date and response_date < application_date:
                raise ValidationError(
                    'La fecha de respuesta no puede ser anterior a la fecha de solicitud.'
                )
        
        return cleaned_data
    
    def save(self, commit=True, user=None):
        company_name = self.cleaned_data['company_name']
        
        company, created = Company.objects.get_or_create(
            name=company_name
        )
        
        application = super().save(commit=False)
        application.company = company
        
        if user:
            application.user = user
            
        if commit:
            application.save()
        
        return application