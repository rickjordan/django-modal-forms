from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Console(models.Model):
    name = models.CharField(max_length=64)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.company, self.name)

    def games(self):
        return Game.objects.filter(console=self).order_by('title')

class Game(models.Model):
    title = models.CharField(max_length=128)
    release_date = models.DateField()
    console = models.ForeignKey(Console, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
