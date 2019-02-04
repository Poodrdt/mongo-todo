from .models import TodoList, TodoListEntry
from rest_framework import serializers


class TodoListSerializer(serializers.ModelSerializer):
    list_entrys = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TodoList
        fields = ('id', 'name', 'list_entrys')


class TodoListEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoListEntry
        fields = ('id', 'parent_list', 'text', 'due_date', 'finised')