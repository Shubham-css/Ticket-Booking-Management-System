from django.db import models
from django.contrib.auth.models import User

class Show(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    available_seats = models.IntegerField()

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    booking_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.show.title} x{self.quantity}"