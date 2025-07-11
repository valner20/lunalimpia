from rest_framework import serializers
from .models import Cliente, Profesional, Turno
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['is_staff'] = user.is_staff

        return token
    
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','nombre', 'direccion','cedula','correo', 'video']


class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = ["id","username"]

class CitaCrearSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id','fecha', 'hora', 'cliente', 'profesional', 'valor']

class CitaSerializer(serializers.ModelSerializer):
    profesional = ProfesionalSerializer()
    cliente = ClienteSerializer() 
       
    class Meta:
        model = Turno
        fields = ['id','fecha', 'hora', 'cliente', 'profesional', 'valor']  
class RegistroProfesionalSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Profesional
        fields = ['username', 'password']

    def create(self, validated_data):
        password = validated_data.pop('password')
        profesional = Profesional(**validated_data)
        profesional.set_password(password)
        profesional.save()
        return profesional

