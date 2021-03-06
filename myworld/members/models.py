from django.db import models

class Age(models.Model):
    member_age = models.IntegerField()

    def __str__(self):
        return str(self.member_age)

class Members(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.ForeignKey(Age, on_delete=models.CASCADE, default=1)

class Profile(models.Model):
    name = models.CharField(max_length=50)
    picture = models.ImageField(upload_to = 'media')    



