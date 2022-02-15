from django.db import models

# Create your models here.
class Destination(models.Model):
    
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    
    desc=models.TextField()
    long_desc=models.TextField()

    offer=models.BooleanField(default=False)
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Destinations'


class BookDestinations(models.Model):
    destination=models.ForeignKey(Destination,on_delete=models.CASCADE)
  
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='BookDestination'



class Booked(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    phone_no=models.TextField()
    

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name_plural='Booked'
    




class TrekkingGuide(models.Model):

    name=models.CharField(max_length=100)
    desc=models.TextField()
    phoneno=models.CharField(max_length=20)
    img=models.ImageField(upload_to='pics')
    status=models.BooleanField()
    email=models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Trekking guide'

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    testimonial=models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='Testimonials'

class News(models.Model):
    title=models.CharField(max_length=100)
    short_desc=models.TextField()
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='News'

    

    


