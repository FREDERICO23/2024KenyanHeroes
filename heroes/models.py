from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from cloudinary.models import CloudinaryField
# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    photo =ProcessedImageField(upload_to='avatars',
                                 processors=[ResizeToFill(400, 400)],
                                 format='JPEG',
                                 options={'quality': 90},
                                 blank=True,
                                 null=True)
    dob = models.DateField()
    killed = models.DateField()
    familynumber = models.IntegerField()

    def __str__(self):
        return self.name
