from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)    #blog's topic
    category=models.CharField(max_length=50,blank=True) #blog's lable
    date_time=models.DateTimeField(auto_now_add=True)  #blog's date
    content=models.TextField(blank=True,null=True)     #blog's content

    def __str__(self):
        return self.title  #tell the objects how to show itself(default is '',here is self.title)
    
    def get_absolute_url(self):
        return reverse('views.ArticleListView.as_view()', args=[str(self.id)])
        
    class Meta:
        ordering=['-date_time']





