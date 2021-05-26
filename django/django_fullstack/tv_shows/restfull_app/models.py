from django.db import models
class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "show title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "show network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "show description should be at least 10 characters"
        return errors
# Create your models here.
class Shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField(default="description field")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()



