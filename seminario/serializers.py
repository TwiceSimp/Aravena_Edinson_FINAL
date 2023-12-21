from rest_framework import serializers
from seminario import models

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instituciones
        fields = '__all__'


class InscritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Inscritos
        fields = '__all__'