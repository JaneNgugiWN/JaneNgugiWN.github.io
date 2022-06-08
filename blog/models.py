from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=20)
    
    def __str__(self):
        return self.caption

class Author(models.Model):
    firstname=models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"
    def __str__(self):
        return self.get_full_name()
    
    
class Post(models.Model):
    title=models.CharField(max_length=100)
    image = models.CharField(max_length=200)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    excerpt=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    tags=models.ManyToManyField(Tag)
    
    # def get_post_details(self):
    #     return f"{self.title}       {self.author}  {self.date}"

    # def __str__(self):
    #     return self.get_post_details()
