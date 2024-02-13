
# O Problema

O desafio que você deve resolver é a implantação da aplicação de Comentários em versão API (backend) usando ferramentas open source da sua preferência.

Você precisa criar o ambiente de execução desta API com o maior número de passos automatizados possível, inclusive a esteira de deploy.

A aplicação será uma API REST que está disponível neste repositório. Através dela os internautas enviam comentários em texto de uma máteria e acompanham o que outras pessoas estão falando sobre o assunto em destaque. O funcionamento básico da API consiste em uma rota para inserção dos comentários e uma rota para listagem.

Os comandos de interação com a API são os seguintes:

# Ideias 

Irei utilizar o github actions por ter uma integração já com o próprio github. 

Irei adotar um modelo de pastas que já trabalho usando o dockerfile dentro da pasta docker

Irei criar uma pasta de test e colocar o testes unitarios que será necessario para o projeto

Será feito os testes antes de iniciar propriamente o build/deploy para caso encotnre algum erro já faça o stop antes de iniciar o build.


# Inicio 

Comecei a fazer a contrução da estrutura de pastas 

REMOTE-JOBS-BRAZIL/
│
├── app.py
├── terraform/
|   └── main.tf
├── test/
│   └── test_app.py
└── docker/
    └── Dockerfile

Após o ajuste das pastas , foi feito pequenos ajustes na Api.py para que se "ajusta-se" a nova estrutura corretamente. 

Foi feito a criação o workflow no github actions para subir provisionar o ambiente (IAC)