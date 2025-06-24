from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from accounts.models import *
from .serializers import *
from django.forms.models import model_to_dict
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

def createUser(data, entity):
    data['user_type'] = entity
    serializer = UserSerializer(data = data)
    if serializer.is_valid():
        new_user = serializer.save()
        return new_user
    else:
        return JsonResponse(serializer.errors, status=400)

def createCompany(data, new_user):
    if isinstance(new_user,JsonResponse):
         return JsonResponse( status=400)
    else:
        data['user_id'] = new_user.id
        serializer = CompanySerializer(data=data)

        if serializer.is_valid():
            new_company = serializer.save()
            return new_company
        else:
            return JsonResponse(serializer.errors, status=400)

def createTelephone(data):
    serializer = TelephoneSerializer(data=data)
    if serializer.is_valid():

        new_telephone = serializer.save()
        return new_telephone
    else:
        return JsonResponse(serializer.errors, status=400)

def relationTelephone(new_telephone, new_entity):
    if isinstance(new_telephone,JsonResponse) or isinstance(new_entity, JsonResponse):
         return JsonResponse( status=400)
    else:
        new_manyToManyTelephone = ManyToManyTelephone(telephone_id = new_telephone, entity_object = new_entity)
        new_manyToManyTelephone.save()
    
def createAdress(data):
    serializer = AddressSerializer(data=data)
    if serializer.is_valid():
        new_adress = serializer.save()
        return new_adress
    else:
        return JsonResponse(serializer.errors, status=400)
    
def relationAdress(new_adress, new_entity):
    if isinstance(new_adress,JsonResponse) or isinstance(new_entity, JsonResponse):
         return JsonResponse( status=400)
    else:
        new_manyToManyAdress = ManyToManyAdress(adress_id = new_adress, entity_object = new_entity)
        new_manyToManyAdress.save()

@api_view(['POST'])
def cadastrationCompany(request):
    data = request.data
    entity = 'Company'
    new_user = createUser(data, entity)
    if isinstance(new_user,JsonResponse):
         return JsonResponse( status=400) 
    new_company = createCompany(data, new_user)
    if isinstance(new_company,JsonResponse):
         return JsonResponse( status=400)
    new_telephone = createTelephone(data)
    if isinstance(new_telephone,JsonResponse):
         return JsonResponse( status=400)
    relationTelephone(new_telephone, new_company)
    new_adress = createAdress(data)
    relationAdress(new_adress, new_company)
    serializer_cadastration_company = {'new_user': UserSerializer(new_user).data,
                                       'new_company': CompanySerializer(new_company).data,
                                       'new_telephone': TelephoneSerializer(new_telephone).data}
    return JsonResponse(serializer_cadastration_company, status=201)

@api_view(['GET'])
@permission_classes([IsAdminUser])
def listUser(request):
    user = User.objects.all()
    serializer = UserSerializer(user, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listCompany(request):
    company = Company.objects.all()
    serializer = CompanySerializer(company, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listTelephone(request):
    telephone = Telephone.objects.all()
    serializer = TelephoneSerializer(telephone, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def listAdress(request):
    adress = Adress.objects.all()
    serializer = AddressSerializer(adress, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def takeToken(request):
    data = request.data
    user = UserSerializer(data = data)
    token = TokenObtainPairSerializer(user)
    return Response(token.data)
'''
@api_view(['GET'])
def listUserCompany_view(request):
    listUser()
    listCompany()
    listTelephone()

    return HttpResponse(status=201)
'''