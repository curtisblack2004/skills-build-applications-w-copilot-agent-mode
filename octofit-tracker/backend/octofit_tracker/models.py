from djongo import models

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    members = models.ArrayReferenceField(to='User', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

    class Meta:
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        verbose_name = "Leaderboard"
        verbose_name_plural = "Leaderboards"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = "Workout"
        verbose_name_plural = "Workouts"