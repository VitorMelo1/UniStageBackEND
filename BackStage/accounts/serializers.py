from rest_framework import serializers

from .models import User, EntityType, Telephone, Adress, University, Course, Employee, Student, Company

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'user_type', 'date_joined']

        extra_kwargs = {
           'password': {'write_only': True},
            'date_joined': {'read_only': True},
        }
        

class EntityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityType
        fields = ['entity_name']

        

class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = ['number', 'ddd', 'country']

        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adress
        fields = ['street', 'district', 'city', 'state', 'country', 'cep', 'number']

        

class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ['name', 'cnpj',]

        

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'university_id']

        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['name', 'cpf', 'user_id', 'course_id']

       

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'cpf', 'user_id', 'course_id']

        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'user_id']

        
