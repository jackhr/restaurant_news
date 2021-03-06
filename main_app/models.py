from django.db import models
from django.urls import reverse

OCCASIONS = (
    ('B', 'Birthday'),
    ('A', 'Anniversary'),
    ('S', 'Special Occasion')
)

FREQUENCY = (
    ('D', 'Daily'),
    ('W', 'Weekly'),
    ('M', 'Monthly')
)

# Create your models here.
class Subscriber(models.Model):
    first_name = models.CharField(
      'First Name', max_length=50
    )
    last_name = models.CharField(
      'Last Name', blank=True, max_length=50,
    )
    email = models.EmailField(
      'Email', max_length=254
    )
    zipcode = models.CharField(
      'Zipcode', blank=True, max_length=10
    )
    special_date = models.DateField(
      'Date', blank=True, null=True
    )
    special_date_name = models.CharField(
        max_length=1,
        choices=OCCASIONS,
        default=OCCASIONS[0][0]
    )
    phone = models.CharField(
      'Phone #', blank=True, max_length=10
    )
    frequency = models.CharField(
        max_length=1,
        choices=FREQUENCY,
        default=[0][0]
    )
    placename = models.CharField(
      max_length=50, default='None'
    )

    def get_absolute_url(self):
        return reverse('confirmation')
