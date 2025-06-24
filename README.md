# UniStage Backend

Este repositório contém o código-fonte do sistema de backend do projeto **UniStage**, desenvolvido com **Django** e **Django REST Framework**. Ele é responsável por gerenciar a API, banco de dados, autenticação e lógica de negócio.

---

## 📦 Tutorial de Instalação

Siga os passos abaixo para configurar o ambiente de desenvolvimento e instalar as dependências necessárias.

### 1. Inicie um Terminal

Abra o terminal do seu sistema operacional:

- **macOS:** Acesse `Aplicativos > Utilitários > Terminal` ou busque por "Terminal" no Spotlight.  
- **Windows:** Use o `Prompt de Comando (CMD)` ou `PowerShell`, buscados pelo menu Iniciar.

### 2. Navegue até a Pasta Raiz do Projeto

Utilize o comando `cd` para acessar a pasta onde está o arquivo `manage.py`:

```bash
cd /caminho/para/sua/pasta/do/projeto/backend
# Exemplo macOS: cd ~/Desktop/Faculdade/FTT/UniStageBack
# Exemplo Windows: cd C:\Users\SeuUsuario\Desktop\Faculdade\FTT\UniStageBack
```

### 3. Configure o Ambiente Virtual

Crie um ambiente virtual para isolar as dependências do projeto:

- **macOS:**

```bash
python3 -m venv venv
```

- **Windows:**

```bash
python -m venv venv
```

> Isso criará uma pasta chamada `venv` com o ambiente virtual.

### 4. Ative o Ambiente Virtual

Ative o ambiente virtual criado:

- **macOS:**

```bash
source venv/bin/activate
```

- **Windows (CMD):**

```bash
.\venv\Scripts\activate
```

- **Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

> Após ativado, você verá `(venv)` no início da linha de comando.

### 5. Instale os Requisitos

Com o ambiente virtual ativo, instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

---

## 🚀 Tutorial de Uso

Siga os passos abaixo para iniciar o servidor de desenvolvimento e acessar a API localmente.

### 1. Inicie um Terminal

Abra o terminal do seu sistema operacional.

### 2. Navegue até a Pasta Raiz do Projeto

Utilize o comando `cd` para acessar a pasta onde está o arquivo `manage.py`:

```bash
cd /caminho/para/sua/pasta/do/projeto/backend
```

### 3. Ative o Ambiente Virtual

Se o ambiente virtual ainda não estiver ativo, ative-o novamente:

- **macOS:**

```bash
source venv/bin/activate
```

- **Windows (CMD):**

```bash
.\venv\Scripts\activate
```

- **Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

### 4. Rode o Servidor de Desenvolvimento

Com o ambiente virtual ativo, execute:

```bash
python manage.py runserver
```

> O servidor será iniciado (geralmente em `http://127.0.0.1:8000/`) e você poderá acessar a API através dessa URL.

---

## ✅ Pronto!

Agora o backend está configurado e rodando localmente. Bom desenvolvimento!
