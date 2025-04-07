from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
# Create your models here.
class Tag(models.Model):
    label=models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
    ContentType=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveBigIntegerField()
   

class LikedItem(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    ContentType=models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id=models.PositiveBigIntegerField()


