from django.db import models
from django.utils import timezone

class Event(models.Model): 
    id   = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "events"
        

class EventDate(models.Model): 
    id    = models.BigAutoField(primary_key=True)
    date  = models.DateTimeField(default=None)
    event = models.ForeignKey(Event, on_delete=models.PROTECT, related_name='dates_of_event')

    class Meta:
        db_table = "event_dates"


class EventVote(models.Model): 
    id    = models.BigAutoField(primary_key=True) 
    name  = models.CharField(max_length=50)
    date  = models.ForeignKey(EventDate, on_delete=models.PROTECT, related_name='vote_for_date')

    class Meta:
        db_table = "event_votes"