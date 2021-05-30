from django.db import models
import bcrypt

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["fname"] = "First name should be at least 2 characters"
        if len(postData['lname']) < 2:
            errors["lname"] = "Last name should be at least 2 characters"
        if len(postData['passwd']) < 8:
            errors["passwd"] = "Password should be at least 8 characters"
        if len(postData['email']) < 4:
            errors["email"] = "Bruh..."
      
        return errors


    
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    password = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BlogManager()



def check_email(postemail):
    users = Users.objects.filter(email=postemail)
    if len(users)>0:
        return users[0]
    return False
        
