from django.db import models


class ToDoList(models.Model):
    title = models.CharField(max_length=250)
    # status = models.CharField(max_length=20, choices=(('done', 'Done'),
    #                                    ('not_done', 'Not done')))
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    objects = models.Manager()


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
