from django.db import models

# Create your models here.
class Schedule(models.Model):
    DFCHOICES = [
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
    ]
    date = models.DateField(primary_key=True)
    yesterday_time_of_sleep = models.DateTimeField()
    wakeup_time = models.DateTimeField()
    exercise = models.BooleanField()
    exercise_duration = models.IntegerField(default=0)
    water_glasses = models.IntegerField()
    weight_gain = models.FloatField()
    current_weight = models.FloatField()
    df = models.BooleanField()
    df_quality = models.IntegerField(choices=DFCHOICES)