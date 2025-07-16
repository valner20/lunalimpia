from rest_framework import serializers
from .models import Cliente, Profesional, Turno
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'cedula'

    def validate(self, attrs):
        cedula = attrs.get('cedula')
        if not cedula:
            raise serializers.ValidationError({'cedula': 'Este campo es obligatorio.'})

        return super().validate(attrs)
    
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
        fields = ["id","username", "cedula","is_staff"]

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

    class Meta:
        model = Profesional
        fields = ["id",'username', 'cedula']

    def create(self, validated_data):
        cedula = validated_data['cedula']
        profesional = Profesional(**validated_data)
        profesional.set_password(cedula)
        profesional.save()
        return profesional

