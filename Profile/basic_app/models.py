from django.db import models

# Create your models here.

class Product(models.Model):

    name=models.CharField(max_length=264)
    description=models.CharField(max_length=264)
    location=models.CharField(max_length=264)
    document = models.FileField(upload_to='documents/')
    quantity=models.IntegerField()


    def __str__(self):

        return self.name

  #  def get_post_url(self):
    #    return reverse('update', kwargs={'pk': self.pk})

    #def get_post_url(self):
     #   return reverse('delete', kwargs={'pk': self.pk})
