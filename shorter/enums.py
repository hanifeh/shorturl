from django.db import models


class StatusTypes(models.TextChoices):
    """
    Different types of shorter url status
    """
    public = 'public'
    privet = 'privet'
