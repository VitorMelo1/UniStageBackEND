from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class User(AbstractUser):
    user_type = models.CharField(max_length=20)

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_name="%(app_label)s_%(class)s_group",
        related_query_name="%(app_label)s_%(class)s_user",
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_("user permissions"),
        blank=True,
        help_text=_("Specific permissions for this user."),
        related_name="%(app_label)s_%(class)s_permission",
        related_query_name="%(app_label)s_%(class)s_user",
    )

    def __str__(self):
        return self.username


class EntityType(models.Model):
    entity_name= models.CharField(max_length= 50, unique= True)

    def __str__(self):
        return self.entity_name

class Telephone(models.Model):
    number = models.CharField(max_length= 20)    
    ddd = models.CharField(max_length= 5)
    country = models.CharField(max_length= 10)

    def __str__(self):
        return self.number
   
class ManyToManyTelephone(models.Model):
    telephone_id = models.ForeignKey(Telephone, on_delete= models.CASCADE, db_column='telephone_id') 
    
    entity_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    entity_id = models.PositiveIntegerField()
    entity_object = GenericForeignKey('entity_type', 'entity_id') 

    def __str__(self):
        return f"Telefone {self.telephone} relacionado a {self.entity_object}"

class Adress(models.Model):
    street = models.CharField(max_length= 100)
    district = models.CharField(max_length= 60)
    city = models.CharField(max_length= 60)
    state = models.CharField(max_length= 60)
    country = models.CharField(max_length= 60)
    cep = models.CharField(max_length= 20) 
    number = models.CharField(max_length= 20) 

    def __str__(self):
        return self.cep

class ManyToManyAdress(models.Model):
    adress_id = models.ForeignKey(Adress, on_delete=models.CASCADE, db_column='adress_id') 

    entity_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    entity_id = models.PositiveIntegerField()
    entity_object = GenericForeignKey('entity_type', 'entity_id') 


class University(models.Model):
    name = models.CharField(max_length= 60)
    cnpj = models.CharField(max_length= 20) 
    

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=60)
    university_id = models.ForeignKey(University, on_delete= models.CASCADE, db_column= 'university_id')
    
    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length= 60)
    cpf = models.CharField(max_length= 20) 
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, db_column= 'user_id')
    course_id = models.ForeignKey(Course, on_delete= models.CASCADE, db_column= 'course_id')
    

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length= 60)
    cpf = models.CharField(max_length= 20) 
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, db_column= 'user_id')
    course_id = models.ForeignKey(Course, on_delete= models.CASCADE, db_column= 'course_id') 

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length= 60)
    cnpj = models.CharField(max_length= 20) 
    user_id = models.ForeignKey(User, on_delete= models.CASCADE, db_column= 'user_id')

    def __str__(self):
        return self.name
    

