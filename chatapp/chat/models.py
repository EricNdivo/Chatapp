from django.db import models

from django.db import models

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    def __str__(self):
        return f'{self.user.username} Profile' 