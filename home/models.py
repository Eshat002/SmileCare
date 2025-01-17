from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,  )
    phone = models.CharField(max_length=15, )

    def __str__(self):
        return self.name



 

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
