from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings


class Command(BaseCommand):
    help = "Create a superuser from environment variables"

    def handle(self, *args, **kwargs) -> str | None:
        User = get_user_model()

        username = settings.SUPERUSER_NAME
        email = settings.SUPERUSER_EMAIL
        password = settings.SUPERUSER_PASSWORD

        if username and email and password:
            if not User.objects.filter(username=username).exists():
                User.objects.create_superuser(
                    username=username, email=email, password=password
                )
                self.stdout.write(self.style.SUCCESS("Superuser created successfully"))
            else:
                self.stdout.write(self.style.WARNING("Superuser already exists"))

        else:
            self.stdout.write(
                self.style.ERROR("Missing environment variables for superuser creation")
            )
