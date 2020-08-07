from django.db import models
from django.urls import reverse
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class Event(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('earlcal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=20, default='Earl', editable=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=100)
    passport_id = models.CharField(max_length=15)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    birthday = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    @property
    def get_html_url(self):
        url = reverse('earlcal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.first_name} </a>'
