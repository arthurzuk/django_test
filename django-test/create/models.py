from django.db import models
import random
import string

def passwordGenerator():
    N = random.randint(6,10)
    p = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=N))
    return p

class Login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField( default=passwordGenerator, max_length=30)
    born_date = models.DateField()
    def __str__(self):
        return self.username + " Password: " + self.password + " Born date: " + str(self.born_date)
