from backend.core import response_codes
from backend.serializers import *
from backend.models import *

class EventManager(object):
    def CreateEvent(self, request):
        result = {}
        try:
            name = request.data["name"]
            dates = request.data["dates"]
            event = Event.objects.create(name=name)
            for date in dates:
                EventDate.objects.create(date=date, event=event)
            result = {"id": event.id}
        except Exception as e:
            result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.CRT_EVNT_ERR_MSG}
            print("Exception in CreateEvent: ", str(e))
        return result

    def ListAllEvents(self):
        result = {}
        try:
            result = { "events": EventSerializer(Event.objects.all(), many=True).data}
        except Exception as e:
            result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.GET_ALL_EVNTS_ERR_MSG}
            print("Exception in ListAllEvents: ", str(e))
        return result

    def GetSingleEvent(self, id):
        result = {}
        try:
            event = EventSerializer(Event.objects.get(id=id)).data
            event.update({"dates": EventDate.objects.filter(event=event["id"]).values_list("date", flat=True)})
            # event.update({"votes": EventVote.objects.filter(date__in=event["date"]).values("date", "name")})
            result = event
        except Exception as e:
            result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.GET_EVNT_ERR_MSG}
            print("Exception in GetSingleEvent: ", str(e))
        return result