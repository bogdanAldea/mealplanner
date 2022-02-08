from django.contrib.auth import models


class Cook(models.AbstractUser):
    """Model implements the AbstractUser class,
    defining a custom application user."""

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    __repr__ = __str__