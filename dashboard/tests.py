from django.test import TestCase
from applications.models import Application, Company
from users.models import User
from datetime import datetime, timedelta
from .services import get_average_applications

# Create your tests here.
class TestDashboardService(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.company = Company.objects.create(name="Test Company")
        
        for i in range(5):
            Application.objects.create(
                user=self.user,
                title=f"Job {i}",
                company=self.company,
                url=f"https://example.com/{i}",
                location="Madrid",
                description="Test",
                status="APPLIED",
                application_date=datetime.now() - timedelta(days=i)
            )

    def test_get_average_applications(self):
        average = get_average_applications(self.user)
        self.assertEqual(average, 1)

    def test_get_basic_stats(self):
        pass

    def test_get_evolution_stats(self):
        pass
