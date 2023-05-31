from rest_framework import serializers
from . import models

#####################################################################################

class settings_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Settings
        fields = '__all__'

#####################################################################################

class subjects_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subjects
        fields = '__all__'

#####################################################################################

class links_serializer(serializers.ModelSerializer):
    class Meta:
        model = models.Links
        fields = '__all__'

#####################################################################################
