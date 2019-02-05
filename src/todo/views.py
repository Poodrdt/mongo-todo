from django.http import HttpResponse
from rest_framework.reverse import reverse

def index(request):
    api_url = 'api/v1/'
    return HttpResponse(f"<h3>Go to <a href={api_url}> API </a></h3>")

from .models import TodoList, TodoListEntry
from rest_framework import viewsets
from .serializers import TodoListSerializer, TodoListEntrySerializer


class TodoListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todo Lists to be viewed or edited.
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer


class TodoListEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Todo Lists Entrys to be viewed or edited.
    """
    queryset = TodoListEntry.objects.all()
    serializer_class = TodoListEntrySerializer

