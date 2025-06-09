from django.db import models

# ========================
# Proprietário e Veículos
# ========================

class Proprietario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    proprietario = models.ForeignKey(Proprietario, on_delete=models.CASCADE)

    def __str__(self):
        return self.placa

# ========================
# Departamentos e Cargos
# ========================

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

# ========================
# Pessoas Institucionais
# ========================

class PessoaInstitucional(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=50, unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome

class Agente(models.Model):
    pessoa = models.OneToOneField(PessoaInstitucional, on_delete=models.CASCADE)

    def __str__(self):
        return f"Agente: {self.pessoa.nome}"

class Colaborador(models.Model):
    pessoa = models.OneToOneField(PessoaInstitucional, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Colaborador: {self.pessoa.nome}"


# ========================
# Laudo
# ========================

class Laudo(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    agente = models.ForeignKey(Agente, on_delete=models.SET_NULL, null=True)
    data_emissao = models.DateField(null=True, blank=True)
    descricao = models.TextField()
    status = models.CharField(max_length=50)
    envolvido = models.ForeignKey(PessoaInstitucional, on_delete=models.SET_NULL, null=True, related_name='laudo_perito')
    tipo_laudo = models.CharField(max_length=50)
    resultado = models.CharField(max_length=100, null=True, blank=True)
    valor_estimado_dano = models.DecimalField(max_digits=10, decimal_places=2)
    data_conclusao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Laudo {self.id} - {self.veiculo.placa}"

# ========================
# Métodos e Métodos por Perícia
# ========================

class Metodo(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MetodoPericia(models.Model):
    colaborador = models.ForeignKey(Colaborador, on_delete=models.CASCADE)
    metodo = models.ForeignKey(Metodo, on_delete=models.CASCADE)
    resultado = models.CharField(max_length=100, null=True, blank=True)
    laudo = models.ForeignKey('Laudo', on_delete=models.CASCADE, null=True, blank=True)
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.colaborador.pessoa.nome} - {self.metodo.name} - {self.resultado[:50]}"

# ========================
# Evidência
# ========================

class Evidencia(models.Model):
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)
    tipo_evidencia = models.CharField(max_length=50)
    descricao = models.TextField()
    caminho_arquivo = models.TextField()

    def __str__(self):
        return f"Evidência {self.id} - Laudo {self.laudo.id}"

# ========================
# Resultado Pericial
# ========================

class ResultadoPericia(models.Model):
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)
    categoria = models.CharField(max_length=50)
    resultado = models.TextField()
    descricao = models.TextField()

    def __str__(self):
        return f"Resultado {self.id} - Laudo {self.laudo.id}"

# ========================
# Histórico de Status
# ========================

class HistoricoStatusLaudo(models.Model):
    laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)
    status_anterior = models.CharField(max_length=50)
    status_novo = models.CharField(max_length=50)
    data_status = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Status {self.status_anterior} → {self.status_novo} (Laudo {self.laudo.id})"

# ========================
# Avaliação de Responsabilidade
# ========================

# class AvaliacaoResponsabilidade(models.Model):
#     laudo = models.ForeignKey(Laudo, on_delete=models.CASCADE)
#     agente = models.ForeignKey(Agente, on_delete=models.CASCADE, null=True)
#     tipo_responsabilidade = models.CharField(max_length=50)
#     descricao_responsabilidade = models.TextField()

#     class Meta:
#         unique_together = ('laudo', 'agente')  # impede duplicação

#     def __str__(self):
#         return f"Laudo {self.laudo.id} - {self.agente.pessoa.nome} - {self.tipo_responsabilidade}"
