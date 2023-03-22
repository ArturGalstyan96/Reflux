from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField('User Name ', max_length=50)
    prof = models.CharField('User Prof ' ,max_length=50)
    img = models.ImageField('User Page ', upload_to='images')


    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = 'Users Info'

    

class AboutMe(models.Model):
    name = models.CharField('About Name ', max_length=50)
    aboutText = models.TextField('About Text ')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'AboutMe'
        verbose_name_plural = 'About Me'


class Content(models.Model):
    name = models.CharField('Content Name ', max_length=50)
    text = models.TextField('Content Text ')
    img = models.ImageField('Content Image ', upload_to='images')
    buttonName = models.CharField('Content Button Name ', max_length=100)


    def __str__(self):
        return self.name
    

class Skill(models.Model):
    skillName = models.CharField('Skill Name ', max_length=50)
    skillText = models.TextField('Skill Text ')

    def __str__(self):
        return self.skillName
    


class Prof(models.Model):
    name = models.CharField('Prof Name ', max_length=50)
    text = models.TextField('Prof Text ')
    img = models.ImageField('Prof Image ', upload_to='images')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Prof'
        verbose_name_plural = 'Prof'


class Work(models.Model):
    name = models.CharField('Work Name ', max_length=50)
    text = models.TextField('Prof Text ')

    def __str__(self):
        return self.name


class Image(models.Model):
    name1 = models.CharField('Image Name1 ', max_length=50)
    name2 = models.CharField('Image Name2 ', max_length=50)
    img = models.ImageField('Image', upload_to='images')

    def __str__(self):
        return self.name1
    

class Contact(models.Model):
    name = models.CharField('Your Name ', max_length=50)
    email = models.EmailField('Your Email ')
    subject = models.CharField('Subject ', max_length=200)
    message = models.TextField('Your massage ')

    def __str__(self):
        return self.name
