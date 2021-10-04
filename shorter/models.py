from django.db import models
from .enums import StatusTypes
from .utils import create_random_string, create_random_password
from django.utils import timezone


class Shorter(models.Model):
    """
    model class for shorter url
    """
    original_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True)
    counter = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    validate_time = models.PositiveIntegerField(default=60)  # minutes add for expire time
    expire_time = models.DateTimeField()
    status = models.CharField(choices=StatusTypes.choices, default=StatusTypes.public, max_length=15)
    one_time_password = models.CharField(max_length=12)

    def save(self, *args, **kwargs):
        """
        create short url
        add expire time
        create random password if status is privet
        """
        if not self.short_url:
            self.short_url = self.create_short_url()
        if not self.expire_time:
            self.expire_time = timezone.now() + timezone.timedelta(minutes=self.validate_time)
        if self.status == 'privet' and not self.one_time_password:
            self.one_time_password = create_random_password()
        super().save(*args, **kwargs)

    @classmethod
    def create_short_url(cls):
        """
        check random string is not use before
        """
        random_string = create_random_string()
        if cls.objects.filter(short_url=random_string).exists():
            return cls.create_short_url()
        return random_string
