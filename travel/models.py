from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    create_at = models.DateField(auto_now_add=True)
    upadate_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Flight(BaseModel):
    From = models.CharField(max_length=100, blank=True, null=True)
    to = models.CharField(max_length=100, blank=True, null=True)
    flight_price = models.IntegerField()
    image = models.ImageField(upload_to='img', null=True, blank=True)
    f_date = models.DateField()
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)

    def __str__(self):
        return self.From


class Flightbooking(BaseModel):
    Name = models.ForeignKey(
        Flight, related_name='flight_booking', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="user_booking", on_delete=models.CASCADE)
    start_date = models.DateField()
    Class = models.CharField(max_length=100,
                             choices=(('Econnamy', 'Econnamy'), ('Bussines', 'Bussines')))
    Gender = models.CharField(max_length=100,
                              choices=(('Male', 'Male'), ('Female', 'Female')))
    booking_type = models.CharField(max_length=100,
                                    choices=(('Success', 'Success'), ('Failed', 'Failed')))
