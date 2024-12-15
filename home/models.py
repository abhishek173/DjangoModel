from django.db import models


# Create your models here.
class Student(models.Model):
    gender_choices = (("Male","Male"),("Female","Female"))
    name = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=12)
    email = models.EmailField()
    gender = models.CharField(max_length=10,choices=gender_choices,default="Male")
    age = models.IntegerField(null=True,blank=True)
    date_of_birth = models.DateField()
    profile_image = models.ImageField(null=True,blank=True,upload_to="student/")
    file = models.FileField(upload_to="files/")
    student_bio = models.TextField()
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Author(models.Model):
    author_name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.OneToOneField(Author,on_delete=models.CASCADE)
    book_name = models.CharField(max_length=100)

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100,default="IN")

    def __str__(self):
        return self.brand_name

class Products(models.Model):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.product_name} ({self.brand})"

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)

    def __str__(self):
        return self.skill_name

class Person(models.Model):
    person_name = models.CharField(max_length=100)
    skill = models.ManyToManyField(Skills)

