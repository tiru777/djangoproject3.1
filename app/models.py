from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField(blank=True,null=True)
    age = models.IntegerField()
    photo = models.FileField(blank=True,null=True)

    def __str__(self):
        return self.first_name


class Department(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=200)
    dp_id = models.IntegerField()
    dp_info = models.TextField()

    def __str__(self):
        return self.dep_name +" " +self.employee.first_name


class Topping(models.Model):
    recipe_name = models.CharField(max_length=110)
    size = models.IntegerField()

    def __str__(self):
        return self.recipe_name


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    recipe = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name

SHIRT_SIZES = [
    ("S", "Small"),
    ("M", "Medium"),
    ("L", "Large"),
]

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField()
    address = models.TextField()
    dob = models.DateField(blank=True,null=True)
    age = models.IntegerField()
    photo = models.FileField(blank=True,null=True)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES,blank=True,null=True)

    def __str__(self):
        return self.first_name


class University(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    dep_name = models.CharField(max_length=200)
    dp_id = models.IntegerField()
    dp_info = models.TextField()

    def __str__(self):
        return self.dep_name +" " +self.student.first_name
