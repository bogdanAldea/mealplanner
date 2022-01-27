from django.contrib.auth import models


class Cook(models.AbstractUser):
    """Model implements the AbstractUser class,
    defining a custom application user."""