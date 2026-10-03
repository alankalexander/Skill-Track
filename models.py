from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=150)

    college = models.CharField(
        max_length=200,
        blank=True
    )

    course = models.CharField(
        max_length=150,
        blank=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    profile_image = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.full_name