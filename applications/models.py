from django.db import models

# Create your models here.
class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED = "APPLIED", "Applied"
        IN_PROCESS = "PROCESS", "In Process"
        REJECTED_AFTER_REVIEW = "REJ_REV", "Rejected after review"
        REJECTED_DIRECTLY = "REJ_DIR", "Directly Rejected"
    
    class Experience(models.TextChoices):
        ZERO = "0", "No experience required"
        ONE_YEAR = "1", "1 year of experience required"
        TWO_YEARS = "2", "2 years of experience required"
        THREE_YEARS = "3", "3 years of experience required"
        FOUR_YEARS = "4", "4 years of experience required"
        FIVE_PLUS_YEARS = "5", "5 or more years of experience required"

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

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name