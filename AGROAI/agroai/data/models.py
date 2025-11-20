from django.db import models
from django.contrib.auth.models import User

class OceanData(models.Model):
    REGION_CHOICES = [
        ('pacific', 'Pacific Ocean'),
        ('atlantic', 'Atlantic Ocean'),
        ('indian', 'Indian Ocean'),
        ('arctic', 'Arctic Ocean'),
        ('southern', 'Southern Ocean'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=20, choices=REGION_CHOICES)
    parameter = models.CharField(max_length=50)
    value = models.FloatField()
    unit = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    depth = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.parameter} - {self.region} - {self.timestamp}"