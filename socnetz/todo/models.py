from django.db  import models

class Todo (models.Model):
    description = models.CharField(max_length=160)
    deadline = models.CharField(max_length=160)
    percent = models.IntegerField()

    def getDescription(self):
        return self.description
    def getDeadline(self):
        return self.description
    def getPercent(self):
        return self.description

    def __str__(self):
        return self.description


