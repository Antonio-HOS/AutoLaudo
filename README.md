# API do Projeto Auto Laudos

O projeto **Auto Laudos** tem como objetivo o desenvolvimento de uma **API** para integrar e dar suporte a um sistema completo de **gestão e emissão de laudos veiculares**. A API foi construída com **Django Rest Framework (DRF)** e é responsável por fornecer os serviços necessários para:

- Registro completo das informações dos veículos;
- Registro completo das informações dos usuários;
- Emissão de laudos;
- Autenticação e controle de acesso por **diferentes perfis de usuários** (como usuários e gestores regionais);
- Monitoramento do **fluxo de trabalho**.

---

> **Tecnologias utilizadas:**
>
> - Python
> - Django
> - Django Rest Framework (DRF)

## Como Usar a API

### 1. **Clonar o Repositorio**

Clone o repositório

```bash
git clone https://github.com/Antonio-HOS/AutoLaudo.git
cd AutoLaudo
```

### 2. **Criar e Ativar o Ambiente Virtual**

Para criar o ambiente virtual, navegue até o diretório do seu projeto e execute o seguinte comando:

```bash
py -m venv venv
```

Ativar o Ambiente Virtual

No Windows:
```bash
.\venv\Scripts\activate
```

No macOS/Linux:
```bash
source venv/bin/activate
```

### 3. **Instalar as dependências**

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

### 4. **Configurar o banco de dados**

Migrate o banco de dados:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

### 5. **Criar Superusuário (opcional)**

Se você quiser criar um superusuário para acessar o Django Admin, use o seguinte comando:

```bash
python manage.py createsuperuser
```

### 6. **Rodar o servidor**

Para rodar o servidor localmente, execute:

```bash
python manage.py runserver
```

A API estará disponível em `http://127.0.0.1:8000/admin/`.
User: antonio
Password: antonio
