from rest_framework import serializers
from app.models import *

class SongModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        # fields = ['Sname']
