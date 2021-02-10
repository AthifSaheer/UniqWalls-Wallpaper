from django.db import models

class Category(models.Model):
    title  = models.CharField(max_length=99)

    def __str__(self):
        return self.title

    # def __itr__(self):
    #     return [field.value_to_string(self) for field in Householdmember._meta.fields]

    

class Image(models.Model):
    image = models.ImageField(upload_to='dynamic_img')
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    view_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    