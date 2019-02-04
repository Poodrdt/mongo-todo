from django.db import models


class TodoList(models.Model):
    name        = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class TodoListEntry(models.Model):
    parent_list = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='list_entrys')
    text        = models.CharField(max_length=255)
    due_date    = models.DateField()
    finised     = models.BooleanField(default=False)

    def __str__(self):
        return self.text

