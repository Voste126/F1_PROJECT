from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    base = models.CharField(max_length=100)
    championships_won = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class LapTime(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    lap_number = models.IntegerField()
    lap_time = models.DurationField()

    def __str__(self):
        return f"{self.driver.name} - Lap {self.lap_number}"

class FantasyTeam(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return self.name

class FantasyScore(models.Model):
    fantasy_team = models.ForeignKey(FantasyTeam, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.fantasy_team.name} - {self.race.name}"


class HistoricalData(models.Model):
    hostorical_data = models.JSONField()
    
