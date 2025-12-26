from django.test import TestCase
from applications.models import Application, Company
from users.models import User
from datetime import datetime, timedelta
from .services import get_average_applications, get_percentage_rejected, get_average_time_response

# Create your tests here.
class TestDashboardService(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )
        self.company = Company.objects.create(name="Test Company")

        self.empty_user = User.objects.create_user(
            username="emptyuser",
            password="testpass123"
        )
        
        for i in range(5):
            Application.objects.create(
                user=self.user,
                title=f"Job {i}",
                company=self.company,
                url=f"https://example.com/{i}",
                location="Madrid",
                description="Test",
                status="APPLIED" if i % 2 == 0 else "REJ_DIR",
                application_date=datetime.now() - timedelta(days=i),
                response_date=datetime.now() + timedelta(days=i)
            )

    def test_get_average_applications(self):
        average = get_average_applications(self.user)
        self.assertEqual(average, 1)

    def test_get_average_no_applications(self):
        average = get_average_applications(self.empty_user)
        self.assertAlmostEqual(average, 0)

    def test_get_percentage_rejected(self):
        percentage = get_percentage_rejected(self.user)
        self.assertEqual(percentage, 40)

    def test_get_percentage_empty(self):
        percentage = get_average_applications(self.empty_user)
        self.assertEqual(percentage, 0)

    def test_get_average_time_response(self):
        average_time = get_average_time_response(self.user)
        self.assertEqual(average_time, 4)
    
    def test_get_basic_stats(self):
        pass

    def test_get_evolution_stats(self):
        pass
