from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.CharField(max_length=30, choices={('Mystery','Mystery'), ('Thriller','Thriller'), ('Humor','Humor'), ('Horror','Horror'), ('Sci-Fi','Sci-Fi'), ('Novel','Novel'), ('Computer Science','Computer Science'), ('Drama','Drama'), ('Comedy','Comedy'), ('Religious','Religious'), ('Adventure','Adventure'), ('Poetry','Poetry') })
    isbn = models.CharField(max_length=64, default='null')
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    no_of_books = models.IntegerField(default=1)
    
    def __str__(self):
        return f'Name: {self.title}, Author: {self.author}'