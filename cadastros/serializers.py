from rest_framework import viewsets, routers, serializers
from .models import *

# ================== SERIALIZERS ==================

class ProprietarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proprietario
        fields = '__all__'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class PessoaInstitucionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PessoaInstitucional
        fields = '__all__'

class AgenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agente
        fields = '__all__'

class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = '__all__'

class MetodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metodo
        fields = '__all__'

class MetodoPericiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPericia
        fields = '__all__'

class LaudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laudo
        fields = '__all__'

class EvidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evidencia
        fields = '__all__'

class ResultadoPericiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResultadoPericia
        fields = '__all__'

class HistoricoStatusLaudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoStatusLaudo
        fields = '__all__'

# class AvaliacaoResponsabilidadeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AvaliacaoResponsabilidade
#         fields = '__all__'

