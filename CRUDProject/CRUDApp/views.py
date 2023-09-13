from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import User
from .serializers import UserCreateSerializer, UserRetrieveDeleteSerializer, UserUpdateSerializer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
import re
class UserRetrieveUpdateDestroyView(APIView):
    def delete(self,request,**kwargs):
        identifier=kwargs['identifier']
        try:
            # Try to convert the identifier to an integer (assuming it's an id)
            pk = int(identifier)
            user = User.objects.get(pk=pk)
            user.delete()
            #userSerialized=UserRetrieveDeleteSerializer(user)
            return Response({"Success":"User deleted"})
        except ValueError:
            # If the conversion fails, assume it's a name
            try:
                user= User.objects.get(name=identifier)
                user.delete()
                return Response({"Success":"User deleted"})
            except User.DoesNotExist:
                try:
                    user=User.objects.get(email=identifier)
                    return Response({"Success":"User deleted"})
                    
                except User.DoesNotExist:
                    return Response({'Error': 'User does not exist'}, status=404)

        except User.DoesNotExist:
            return Response({'Error': 'User does not exist'}, status=404)

    def get(self, request, **kwargs):
        identifier=kwargs['identifier']
        try:
            # Try to convert the identifier to an integer (assuming it's an id)
            pk = int(identifier)
            user = User.objects.get(pk=pk)
            userSerialized=UserRetrieveDeleteSerializer(user)
            return Response(userSerialized.data)
        except ValueError:
            # If the conversion fails, assume it's a name
            try:
                user= User.objects.get(name=identifier)
                userSerialized=UserRetrieveDeleteSerializer(user)
                return Response(userSerialized.data)
            except User.DoesNotExist:
                try:
                    user= User.objects.get(email=identifier)
                    userSerialized=UserRetrieveDeleteSerializer(user)
                    return Response(userSerialized.data)
                except User.DoesNotExist:
                    return Response({'Error': 'User does not Exist'}, status=404)
      
        except User.DoesNotExist:
            return Response({'Error': 'User does not Exist'}, status=404)


        
    def put(self, request, identifier):
        try:
            # Try to convert the identifier to an integer (assuming it's an id)
            pk = int(identifier)
            instance = User.objects.get(pk=pk)
        except ValueError:
            # If the conversion fails, assume it's a name
            try:

                instance = User.objects.get(name=identifier)
            except User.DoesNotExist:
                try:
                    instance=User.objects.get(email=identifier)

                except User.DoesNotExist:
                    return Response({'Error':'User does not exist'}, status=404)
                    
        except User.DoesNotExist:
            return Response({'Error': 'User does not exist'}, status=404)

        serializer = UserUpdateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=404)

   

class CreateUserView(APIView):
    def post(self, request):
        name = request.data.get('name')
        email= request.data.get('email')
        # Check if name is a string
        if not re.match(r'^[A-Za-z\s]+$', name):
            return Response({'Error': 'name is not a string'}, status=404)
        try:
            user = User.objects.create(name=name, email=email)
            user.save()
            user_serialized = UserUpdateSerializer(user)

            return Response(user_serialized.data, status=201)
        except Exception as e:
            error_message = str(e) 
            return Response({'Error':error_message}, status=404)
