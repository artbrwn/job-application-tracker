from django.db import models

# Create your models here.
class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "APPLIED", "Solicitado"
        IN_PROCESS = "PROCESS", "En proceso"
        REJECTED_AFTER_REVIEW = "REJ_REV", "Rechazo tras entrevista"
        REJECTED_DIRECTLY = "REJ_DIR", "Rechazo directo"
    
    class Experience(models.TextChoices):
        ZERO = "0", "Sin experiencia"
        ONE_YEAR = "1", "1 año"
        TWO_YEARS = "2", "2 años"
        THREE_YEARS = "3", "3 años"
        FOUR_YEARS = "4", "4 años"
        FIVE_PLUS_YEARS = "5", "5 años"
        NOT_SPECIFIED = "6", "No especificado"


    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name=("Título del puesto"), help_text=("Ej: Desarrollador Backend Python"))
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    url = models.URLField(verbose_name=("URL"), help_text=("Enlace a la oferta"))
    location = models.CharField(max_length=100, verbose_name=("Localización"), help_text=("Madrid, Barcelona..."))
    description = models.TextField(verbose_name=("Descripción"), help_text=("Tareas, certificaciones, requisitos..."))
    required_experience = models.CharField(max_length=1, choices=Experience.choices, verbose_name=("Experiencia requerida"))
    application_date = models.DateTimeField()
    response_date = models.DateField(null=True, blank=True, verbose_name=("Fecha de respuesta"), help_text=("Fecha de respuesta"))
    status = models.CharField(max_length=10, choices=Status.choices, verbose_name=("Estado"))

    def __str__(self):
        return f"{self.title}, {self.company}"
    
    @property
    def status_badge_class(self):
        status_classes = {
            "APPLIED": "bg-secondary",
            "PROCESS": "bg-success",
            "REJ_DIR": "bg-danger",
            "REJ_REV": "bg-warning"
        }
        return status_classes.get(self.status, "bg-secondary")

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name