from django.db import models

# Create your models here.
books=[
    {"id":100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
    {"id":101,"book_name":"aarachar","author":"meera","price":580,"copies":250},
    {"id":102,"book_name":"the alchemist","author":"paulo","price":780,"copies":250},
    {"id":103,"book_name":"ranirising","author":"nirupama","price":1000,"copies":250},
    {"id":104,"book_name":"indhuleka","author":"chandhu menon","price":280,"copies":250},
    {"id":105,"book_name":"pazhassy","author":"mt","price":580,"copies":350},
]


class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    copies=models.PositiveIntegerField()
    published_date=models.DateField(null=True)
    image=models.ImageField(upload_to='images',null=True)
    def __str__(self):
        return self.book_name

class Employee(models.Model):
    employee_name=models.CharField(max_length=120)
    employee_desig=models.CharField(max_length=100)
    employee_exp=models.PositiveIntegerField()
    employee_salary=models.PositiveIntegerField()

    def __str__(self):
        return self.employee_name


# deleting all objects orms
# Modelname.objects.all().delete()


# CRUD operations
# ORM for creating new book object

# C=create
# ref=ModelName(field=value,field=value......)
# ref.save()
# book=Books(book_name="book1",author="authour1",price=130,copies=50)
# book.save()

# R=retrive
# ref=modelname.objects.all()
# books=Books.object.all()
# qs=Books.objects.filter(price__lt=500)
# qs=Books.objects.filter(book_name__contains='ha')
# qs=Books.objects.filter(author__endswith='a')
# qs=Books.objects.filter(book_name__startswith='ra')
# qs=Books.objects.get(id=5)

# U=update

# D=delete




