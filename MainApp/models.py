from email.policy import default
from django.db import models

# Create your models here.
class ToDoList(models.Model):
    options = (
        (0, 'NotDone'),
        (1, 'Done')
    )
    title = models.CharField(max_length=25)
    desc = models.CharField(max_length=50)
    status = models.IntegerField(default=0, choices=options)

    def __str__(self):
        return self.title