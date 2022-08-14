from rest_framework.decorators import api_view
from rest_framework.response import Response
from .core import response_codes, event_managment

@api_view(["GET"])
def GetAllEvents(request):
    context = {}
    try:
        evtObj = event_managment.EventManager()
        result = evtObj.ListAllEvents()
    except Exception as e:
        print(str(e))
        result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.GET_ALL_EVNTS_ERR_MSG}
    context.update(result)
    return Response(context)

@api_view(["POST"])
def CreateEvent(request):
    context = {}
    try:
        evtObj = event_managment.EventManager()
        result = evtObj.CreateEvent(request)
    except Exception as e:
        print(str(e))
        result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.CRT_EVNT_ERR_MSG}
    context.update(result)
    return Response(context)

@api_view(["GET"])
def GetSingleEvent(request, **kwargs):
    context = {}
    try:
        id = kwargs.get("id")
        evtObj = event_managment.EventManager()
        result = evtObj.GetSingleEvent(id)
    except Exception as e:
        print(str(e))
        result = {"ErrorCode": response_codes.ERROR, "ErrorMsg": response_codes.GET_EVNT_ERR_MSG}
    context.update(result)
    return Response(context)