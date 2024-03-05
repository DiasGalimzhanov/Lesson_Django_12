from django.db import models

class Person(models.Model):
    class GenderChoices(models.TextChoices):
        F = 'F', 'Женский'
        M = 'M', 'Мужской'

    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    work_place = models.CharField(max_length=100)
    salary = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GenderChoices.choices)

    def __str__(self):
        return self.name

