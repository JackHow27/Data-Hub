from django.db import models

class ApplicationInstance(models.Model):
    product = models.CharField(max_length=50, choices=[
        ('ECOI','ECOI'),
        ('CCR','CCR'),
        ('IAR','IAR')
    ])
    environment = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    client = models.ForeignKey('client', on_delete=models.CASCADE, related_name='applications')
    relationshipmanager = models.CharField(max_length=200, null=True, blank=True)
    live = models.BooleanField(default=False)

class Client(models.Model):
    name = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Contact(models.Model):
    fullname = models.CharField(max_length=200)
    jobtitle = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    client = models.ForeignKey('client', on_delete=models.CASCADE, related_name='contacts')
