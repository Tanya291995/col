from django.db import models

class State(models.Model):
    name = models.CharField(max_length=50)
    head = models.CharField(max_length=50)

    def publish(self):
        self.save()