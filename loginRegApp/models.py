from django.db import models
import re

class RegistrationManager(models.Manager):
    def i_am_the_validator(self, postData):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        emlTaken = RegistrationForm.objects.filter(email = postData['eml'])
        print(postData)
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['fname']) < 2:
            errors["FirstnameRequired"] = "First name must be aleast 2 characters long"
        if len(postData['lname']) < 3:
            errors["LastnameRequired"] = "Last name should be at least 3 characters long"
        if len(postData['eml']) == 0:
            errors["descriptionRequired"] = "Please add an email address"
        elif not EMAIL_REGEX.match(postData['eml']):    # test whether a field matches the pattern            
            errors['eml'] = "Invalid email address!"
        elif len(emlTaken)>0:
            errors['emlTaken'] = "This email is taken, Try again!"

        
        if len(postData['PW']) < 8:
            errors["PWRequired"] = "Password should be at least 8 characters long"
        return errors

    def loginVal(self, postData):    
        errors = {}
        emailMatch = RegistrationForm.objects.filter(email = postData['eml'])
        if len(emailMatch) == 0:
            errors['emailNotfound'] = "This email address is not found"

        

        elif emailMatch[0].password != postData ['PW']:
            errors['PWwrong'] = "incorrect password"
        return errors



# Create your models here.
class RegistrationForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = RegistrationManager()

    def __str__(self):
        return f"<User object: {self.first_name} {self.last_name}({self.id})>"
