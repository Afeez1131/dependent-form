from django.db import models


class State(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name
    

class Town(models.Model):
    name = models.CharField(max_length=155)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.state}"

class Person(models.Model):
    name = models.CharField(max_length=155)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name