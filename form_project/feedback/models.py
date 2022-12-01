from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse


# Create your models here.


class Feedback(models.Model):
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2)])
    surname = models.CharField(max_length=60, validators=[MinLengthValidator(2)])
    feedback = models.TextField()
    rating = models.PositiveIntegerField()

    def get_url(self):
        return reverse('feedback_detail', args=[self.id])

