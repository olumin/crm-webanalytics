from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name= models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    current_date =datetime.datetime.now()
   
    def __str__(self):
        return self.name  
    
    
class Score(models.Model):
        
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

  
   
    
    state= (
            ('updated', 'Updated'),
            ('Pending','Pending'),
            )
    
    month = (
            ('January', 'January'),
            ('Feburary', 'February'),
            ('March','March'),
            ('April', 'April'),
            ('May','May'),
            ('June', 'June'),
            ('July', 'July'),
            ('August', 'August'),
            ('September', 'September'),
            ('October', 'October'),
            ('November', 'November'),
            ('December', 'December'),
            ) 
    month_s = (
            ('January', 'January'),
            ('Feburary', 'February'),
            ('March','March'),
            ('April', 'April'),
            ('May','May'),
            ('June', 'June'),
            ('July', 'July'),
            ('August', 'August'),
            ('September', 'September'),
            ('October', 'October'),
            ('November', 'November'),
            ('December', 'December'),
            )
    
    date_created = models.DateTimeField(auto_now_add=True, null=False)    
    elements = models.CharField(max_length=50)
    partners_name = models.CharField(max_length=50)
    products = models.CharField(max_length=50)
    current_focus = models.FloatField()
    actual = models.FloatField()
    achieved = models.FloatField(null=False)
    points = models.FloatField(null=False)
    commission = models.FloatField(null=False)
    next_airtime_expectation= models.FloatField()
    topit_expectation = models.FloatField()
    topit_focus = models.FloatField(null=False)
    topit_actual = models.FloatField(null=False)
    topit_achieved = models.FloatField()
    state = models.CharField(max_length=50, null=True)
    currentmonth = models.CharField(max_length=50, null=True)
    monthsec = models.CharField(max_length=50, null=True)
    total_airtime = models.CharField(max_length=50)
    total_topit = models.CharField(max_length=50)

    def __str__(self):
        return self.partners_name 
    
    
    
class Score_hist(models.Model):
           
    user = models.ManyToManyField(User)
    name= models.CharField(max_length=50)
    state = (
            ('updated', 'Updated'),
            ('Pending','Pending'),
            )
    
    month = (
            ('January', 'January'),
            ('Feburary', 'February'),
            ('March','March'),
            ('April', 'April'),
            ('May','May'),
            ('June', 'June'),
            ('July', 'July'),
            ('August', 'August'),
            ('September', 'September'),
            ('October', 'October'),
            ('November', 'November'),
            ('December', 'December'),
            ) 
    month_s = (
            ('January', 'January'),
            ('Feburary', 'February'),
            ('March','March'),
            ('April', 'April'),
            ('May','May'),
            ('June', 'June'),
            ('July', 'July'),
            ('August', 'August'),
            ('September', 'September'),
            ('October', 'October'),
            ('November', 'November'),
            ('December', 'December'),
            )
    
    date_created = models.DateTimeField(auto_now_add=True, null=True)
     
    elements = models.CharField(max_length=50)
    products = models.CharField(max_length=50)
    current_focus = models.FloatField()
    actual = models.FloatField()
    achieved = models.FloatField(null=False)
    point = models.FloatField(null=False)
    commission = models.FloatField(null=False)
    next_airtime_expectation= models.FloatField()
    topit_expectation = models.FloatField()
    topit_focus = models.CharField(max_length=50, null=False)
    topit_actual = models.CharField(max_length=50, null=False)
    topit_achieved = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=True)
    currentmonth = models.CharField(max_length=50, null=True)
    monthsec = models.CharField(max_length=50, null=True)
# Create your models here.
  
    def __str__(self):
        return self.name