# LabReserva

Sistema web para reserva de laboratórios acadêmicos.

## Sobre o projeto

O **LabReserva** é uma aplicação web desenvolvida para auxiliar no gerenciamento de reservas de laboratórios em uma instituição de ensino.

A ideia do projeto surgiu a partir da dificuldade de organizar o uso dos laboratórios da faculdade, já que existem vários laboratórios disponíveis e muitos professores precisam utilizá-los em diferentes dias e horários.

Com o sistema, o usuário consegue selecionar um laboratório, escolher uma data, visualizar os horários disponíveis e realizar uma reserva. Após a reserva ser feita, aquele horário deixa de aparecer como disponível para o mesmo laboratório e data, evitando conflitos de agendamento.

## Problema que o sistema resolve

Em muitas faculdades, o controle de uso dos laboratórios ainda pode ser feito de forma manual, por mensagens ou planilhas. Isso pode causar problemas como:

* Dois professores reservando o mesmo laboratório no mesmo horário;
* Dificuldade para visualizar horários disponíveis;
* Falta de organização das reservas;
* Perda de informações importantes sobre agendamentos.

O **LabReserva** busca resolver esse problema com uma aplicação simples, funcional e centralizada.

## Funcionalidades

* Listagem de laboratórios disponíveis;
* Seleção de data para reserva;
* Exibição dos horários disponíveis;
* Cadastro de reserva com nome, e-mail, disciplina, laboratório, data e horário;
* Bloqueio automático de horários já reservados;
* Listagem das reservas cadastradas;
* Persistência das reservas em banco de dados SQLite;
* Interface web simples e objetiva.

## Tecnologias utilizadas

O projeto foi desenvolvido utilizando as seguintes tecnologias:

* Python
* Flask
* SQLite
* HTML
* CSS
* JavaScript
* Docker
* Git
* GitHub
* GitHub Actions

## Estrutura do projeto

```bash
labreserva/
│
├── app/
│   ├── app.py
│   ├── database.py
│   ├── requirements.txt
│   ├── .env.example
│   └── templates/
│       └── index.html
│
├── .github/
│   └── workflows/
│       └── docker-build.yml
│
├── Dockerfile
├── .dockerignore
├── .gitignore
└── README.md
```

## Pré-requisitos

Para rodar o projeto na sua máquina, você precisa ter instalado:

* Python 3.11 ou superior;
* Git;
* Docker Desktop;
* Visual Studio Code, opcional, mas recomendado.

## Como rodar o projeto localmente sem Docker

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO_AQUI
```

Depois entre na pasta do projeto:

```bash
cd labreserva
```

### 2. Criar o ambiente virtual

No Windows, rode:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

No PowerShell, rode:

```bash
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a execução, rode este comando uma vez:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Depois tente ativar novamente:

```bash
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar as dependências

```bash
python -m pip install -r app\requirements.txt
```

### 5. Rodar a aplicação

```bash
cd app
python app.py
```

### 6. Acessar no navegador

Abra o navegador e acesse:

```bash
http://localhost:5000
```

ou:

```bash
http://127.0.0.1:5000
```

## Como rodar o projeto com Docker

### 1. Verificar se o Docker está instalado

No terminal, rode:

```bash
docker --version
```

Se aparecer a versão do Docker, significa que está instalado corretamente.

### 2. Construir a imagem Docker

Na pasta principal do projeto, rode:

```bash
docker build -t labreserva .
```

### 3. Executar o container

```bash
docker run -p 5000:5000 labreserva
```

### 4. Acessar o sistema

Abra o navegador e acesse:

```bash
http://localhost:5000
```

Caso a porta 5000 já esteja sendo usada, rode com outra porta:

```bash
docker run -p 5001:5000 labreserva
```

E acesse:

```bash
http://localhost:5001
```

## Como testar o funcionamento

Após abrir o sistema no navegador:

1. Digite o nome do professor;
2. Digite o e-mail;
3. Digite a disciplina;
4. Escolha um laboratório;
5. Escolha uma data;
6. Selecione um horário disponível;
7. Clique em “Reservar laboratório”;
8. Veja a reserva aparecer na lista de reservas cadastradas;
9. Recarregue a página;
10. Confira se a reserva continua salva;
11. Tente reservar o mesmo laboratório, na mesma data e no mesmo horário.

O sistema não deve permitir reservas duplicadas para o mesmo laboratório, data e horário.

## GitHub Actions

O projeto possui uma automação com **GitHub Actions** para executar o build da imagem Docker automaticamente a cada push na branch principal.

O arquivo de configuração está em:

```bash
.github/workflows/docker-build.yml
```

Essa automação ajuda a validar se o projeto consegue ser construído corretamente em um ambiente externo.

## Boas práticas utilizadas

O projeto utiliza algumas boas práticas exigidas na disciplina, como:

* Uso de Git e GitHub para controle de versão;
* Uso de `.gitignore` para evitar envio de arquivos desnecessários;
* Uso de `requirements.txt` para listar as dependências do projeto;
* Uso de Docker para containerização da aplicação;
* Uso de GitHub Actions para automação de build;
* Separação entre frontend, backend e banco de dados;
* Banco SQLite para persistência das reservas.

## Membros da equipe

Amanda Victoria Araujo de Souza - Matrícula: 01698446  
Camilla Wanderley de Almeida Herrera - Matrícula: 01675618 
João Pedro Costa Lira - Matrícula: 01710065 

## Status do projeto

Projeto desenvolvido para a avaliação AV2 da disciplina de DevOps.

A aplicação está funcional e permite o cadastro, listagem e controle de reservas de laboratórios acadêmicos.
