from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='img',blank=True)
    def __str__(self):
        return self.name

class Addmovie(models.Model):
    movie_title=models.CharField(max_length=250,unique=True)
    discription=models.TextField()
    poster=models.ImageField(upload_to='poster',blank=True)
    relese_date=models.DateField()
    rate=models.IntegerField()
    actor=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_title