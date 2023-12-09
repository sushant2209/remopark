from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from django.core.management import call_command

class SmartappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "smartapp"
    
    def ready(self):
        import smartapp.signals  # noqa
    # def ready(self):
    #     scheduler = BackgroundScheduler()
    #     scheduler.add_job(self.check_bookings, 'interval', minutes=100)  # Run every minute, adjust as needed
    #     scheduler.start()

    # @staticmethod
    # def check_bookings():
    #     current_time = timezone.now()
    #     call_command('check_bookings')
