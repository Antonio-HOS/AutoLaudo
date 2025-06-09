from django.shortcuts import render

from rest_framework import viewsets, routers, serializers
from .models import *

from .serializers import *

class ProprietarioViewSet(viewsets.ModelViewSet):
    queryset = Proprietario.objects.all()
    serializer_class = ProprietarioSerializer

class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer

class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class PessoaInstitucionalViewSet(viewsets.ModelViewSet):
    queryset = PessoaInstitucional.objects.all()
    serializer_class = PessoaInstitucionalSerializer

class AgenteViewSet(viewsets.ModelViewSet):
    queryset = Agente.objects.all()
    serializer_class = AgenteSerializer

class ColaboradorViewSet(viewsets.ModelViewSet):
    queryset = Colaborador.objects.all()
    serializer_class = ColaboradorSerializer

class MetodoViewSet(viewsets.ModelViewSet):
    queryset = Metodo.objects.all()
    serializer_class = MetodoSerializer

class MetodoPericiaViewSet(viewsets.ModelViewSet):
    queryset = MetodoPericia.objects.all()
    serializer_class = MetodoPericiaSerializer

class LaudoViewSet(viewsets.ModelViewSet):
    queryset = Laudo.objects.all()
    serializer_class = LaudoSerializer

class EvidenciaViewSet(viewsets.ModelViewSet):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer

class ResultadoPericiaViewSet(viewsets.ModelViewSet):
    queryset = ResultadoPericia.objects.all()
    serializer_class = ResultadoPericiaSerializer

class HistoricoStatusLaudoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoStatusLaudo.objects.all()
    serializer_class = HistoricoStatusLaudoSerializer

# class AvaliacaoResponsabilidadeViewSet(viewsets.ModelViewSet):
#     queryset = AvaliacaoResponsabilidade.objects.all()
#     serializer_class = AvaliacaoResponsabilidadeSerializer

