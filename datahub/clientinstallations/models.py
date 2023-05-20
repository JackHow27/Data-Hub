from django.db import models

class ApplicationInstance(models.Model):
    product = models.CharField(max_length=50, choices=[
        ('ECOI','ECOI'),
        ('CCR','CCR'),
        ('IAR','IAR'),
        ('Mobile','Mobile'),
        ('User Management', 'User Management')
    ])
    environment = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    version = models.CharField(max_length=200)
    client = models.ForeignKey('client', on_delete=models.CASCADE, related_name='applications')
    relationshipmanager = models.CharField(max_length=200, null=True, blank=True)
    live = models.BooleanField(default=False)
    server = models.ManyToManyField('Server')

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

class ServerGroup(models.Model):
    name = models.CharField(max_length=100)

class Server(models.Model):
    name = models.CharField(max_length=100)
    internalipv4 = models.CharField(max_length=100)
    externalipv4 = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100, choices=[
        ('WebServer', 'WebServer'),
        ('Database','Database'),
        ('Services','Services'),
        ('DC', 'DC'),
        ('FTP', 'FTP'),
        ('SMTP', 'SMTP'),
        ('WebProxy', 'WebProxy'),
        ('Other','Other')
    ] )
    trustlevel = models.CharField(max_length=50, choices=[
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High')
    ])
    description = models.CharField(max_length=200, null=True, blank=True)
    ServerGroup = models.ManyToManyField('ServerGroup')

class Customisation(models.Model):
    app = models.ForeignKey('ApplicationInstance', on_delete=models.CASCADE, related_name="customisations")
    language = models.CharField(max_length=50)
    adolink = models.CharField(max_length=100)
    ticketlink = models.CharField(max_length=100)
    
class Upgrade(models.Model):
    app = models.ForeignKey('ApplicationInstance', on_delete=models.CASCADE, related_name="upgrades")
    upgradedate = models.DateTimeField()
    versionfrom = models.CharField(max_length=50)
    versionto = models.CharField(max_length=50)
    engineer = models.CharField(max_length=100)
    ticketlink = models.CharField(max_length=100)
    note = models.CharField(max_length=300)