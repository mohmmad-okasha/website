import os
from os import path

from django.http import HttpResponse, JsonResponse
from .models import Subjects
from .models import Links
from .models import Settings
from . import serializers

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins

from django.db.models import Max
from django.db.models import Q

from django.core.files.storage import default_storage

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken




#####################################################################################

# Login


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    return Response({'access': access_token}, status=status.HTTP_200_OK)

#####################################################################################

# to upload files


class FileUploadView(APIView):
    parser_classes = (MultiPartParser,)

    def post(self, request, format=None):
        file_name = self.request.query_params.get('file_name')
        image_file = request.FILES.get('image')
        file_path = path.abspath(
            'frontend/dist/media/'+path.curdir)+file_name
        # to remove last img for this customer
        if (os.path.exists(file_path)):
            os.remove(os.path.join(file_path))

        default_storage.save(file_path, image_file)
        return Response({'success': True})

#####################################################################################

# to get max id from any table


@api_view(['GET'])
def get_max_id(request):
    table_name = request.query_params['table_name']
    max_id = eval(table_name).objects.aggregate(Max('id'))
    return Response({'data': max_id})



#####################################################################################
# to get subject id

@api_view(['GET'])
def get_subject_id(request):
    sent_subject_name = request.query_params['subject']

    subject_id = Subjects.objects.filter(name=sent_subject_name).first()
    if subject_id:
        return JsonResponse({'subject_id': subject_id.id})
    else:
        return JsonResponse({'subject_id': None})

#####################################################################################
# to get_links

@api_view(['GET'])
def get_links(request):
    subject = request.query_params['subject']
    links = Links.objects.filter(subject_id_id=subject).all()
    serial= serializers.links_serializer(links,many=True)
    return Response(serial.data)


#####################################################################################

# to remove files

@api_view(['GET'])
def remove_file(request):
    file_name = request.query_params['file_name']
    file_path = path.abspath('frontend/dist/media/'+path.curdir)+file_name
    if (os.path.exists(file_path)):
        os.remove(os.path.join(file_path))
        return Response({'removed': 1})
    else:
        return Response({'removed': 0})

#####################################################################################


class subjects(ModelViewSet, mixins.DestroyModelMixin):

    queryset = Subjects.objects.all()
    serializer_class = serializers.subjects_serializer

    def get_queryset(self):
        queryset = Subjects.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(Q(name__contains=search))
        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#####################################################################################


class links(ModelViewSet, mixins.DestroyModelMixin):

    queryset = Links.objects.all()
    serializer_class = serializers.links_serializer

    def get_queryset(self):
        queryset = Links.objects.all()
        id = self.request.query_params.get('id')
        if id is not None:
            queryset = queryset.filter(id=id)
        subject_id = self.request.query_params.get('subject_id')
        if subject_id is not None:
            queryset = queryset.filter(subject_id=subject_id)
        search = self.request.query_params.get('search')
        if search is not None:
            queryset = queryset.filter(Q(title__contains=search),subject_id=subject_id)

        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#####################################################################################

class settings(ModelViewSet):

    queryset = Settings.objects.all()
    serializer_class = serializers.settings_serializer

    def get_queryset(self):
        queryset = Settings.objects.all()
        return queryset

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

#####################################################################################
