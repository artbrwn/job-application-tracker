from django.forms import CharField, ModelForm
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
                 "required_experience", "status"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
            if field.help_text:
                field.widget.attrs['placeholder'] = field.help_text
    
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