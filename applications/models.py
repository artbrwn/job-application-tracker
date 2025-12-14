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
    title = models.CharField(max_length=200)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    url = models.URLField()
    location = models.CharField(max_length=100)
    description = models.TextField()
    required_experience = models.CharField(max_length=1, choices=Experience.choices)
    application_date = models.DateTimeField()
    response_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=Status.choices)

    def __str__(self):
        return f"{self.title}, {self.company}"

class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name