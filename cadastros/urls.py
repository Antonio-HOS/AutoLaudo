from rest_framework import routers
from django.urls import path, include
from .views import *
# ================== URL ROUTER ==================

router = routers.DefaultRouter()
router.register(r'proprietarios', ProprietarioViewSet)
router.register(r'veiculos', VeiculoViewSet)
router.register(r'departamentos', DepartamentoViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'pessoas', PessoaInstitucionalViewSet)
router.register(r'agentes', AgenteViewSet)
router.register(r'colaboradores', ColaboradorViewSet)
router.register(r'metodos', MetodoViewSet)
router.register(r'metodos-pericia', MetodoPericiaViewSet)
router.register(r'laudos', LaudoViewSet)
router.register(r'evidencias', EvidenciaViewSet)
router.register(r'resultados-pericia', ResultadoPericiaViewSet)
router.register(r'historico-status', HistoricoStatusLaudoViewSet)
# router.register(r'avaliacoes', AvaliacaoResponsabilidadeViewSet)

urlpatterns = router.urls
