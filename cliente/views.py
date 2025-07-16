from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Cliente, Profesional, Turno
from rest_framework.permissions import IsAuthenticated
from .serializer import ClienteSerializer, RegistroProfesionalSerializer, CitaSerializer, ProfesionalSerializer,CitaCrearSerializer, CustomTokenObtainPairSerializer
from .permissions import SoloSuperuserPuedeCrear
from rest_framework_simplejwt.views import TokenObtainPairView

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    permission_classes = [IsAuthenticated,SoloSuperuserPuedeCrear]

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
class CitaViewSet(viewsets.ModelViewSet):
    queryset = Turno.objects.all()
    permission_classes = [IsAuthenticated, SoloSuperuserPuedeCrear]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'get']:
            return CitaSerializer  
        return CitaCrearSerializer 
    def get_queryset(self):
        usuario = self.request.user
        if usuario.is_superuser:
            return Turno.objects.all()
        return Turno.objects.filter(profesional=usuario)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"detail": "Aún no tienes agenda"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        read_serializer = CitaSerializer(instance=serializer.instance, context={'request': request})
        return Response(read_serializer.data, status=201)


class RegistroProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = RegistroProfesionalSerializer

    