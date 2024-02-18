Histórico de Desenvolvimento
O Problema:

O desafio consiste na implantação da aplicação de Comentários em versão API (backend) utilizando ferramentas open source de preferência do desenvolvedor.

O objetivo é criar um ambiente de execução para esta API com o máximo de automação possível, incluindo a criação da esteira de deploy.

A aplicação será uma API REST disponível neste repositório. Através dela, os usuários podem enviar comentários em texto sobre uma matéria e acompanhar o que outras pessoas estão falando sobre o assunto em destaque. A funcionalidade básica da API consiste em uma rota para inserção dos comentários e uma rota para listagem.

Os comandos de interação com a API são os seguintes:

Ideias:

Utilização do GitHub Actions devido à integração com o próprio GitHub.
Adoção de um modelo de pastas já utilizado, colocando o Dockerfile dentro da pasta docker.
Criação de uma pasta de testes e inclusão dos testes unitários necessários para o projeto.
Execução dos testes antes de iniciar o build/deploy para identificar e corrigir erros previamente.

Início:

O desenvolvedor iniciou a construção da estrutura de pastas da seguinte maneira:

REMOTE-JOBS-BRAZIL/
│
├── app/
│    └── api.py
├── terraform/
|   └── main.tf
├── test/
│   └── test_app.py
└── docker/
    └── Dockerfile
Após algumas tentativas de build e deploy sem sucesso, o provisionamento da infraestrutura usando Terraform com main.tf não foi satisfatório. O desenvolvedor não conseguiu manter a mesma instância criada com todas as informações e enfrentou problemas relacionados à perda de DNS para conexão.

Seguindo a abordagem de pastas mencionada anteriormente, ao criar a pasta docker, o desenvolvedor encontrou problemas de permissões para enviar a imagem para dentro da EC2.

Após várias tentativas de build para enviar a imagem via SSH, SCP e SFTP, o desenvolvedor desistiu dessa abordagem e optou por copiar os arquivos da pasta raiz para dentro de outra pasta na EC2 para então construir a pasta docker.

Mesmo tentando enviar apenas a imagem .tar, o GitHub Actions não conseguia salvar na pasta temporária e enviá-la para a EC2. Quando a pasta docker era salva em qualquer outra pasta usando mkdir, a conexão falhava e o arquivo não era encontrado dentro da pasta solicitada.

Desenvolvimento e Testes
Após conseguir fazer a conexão via SSH e enviar os arquivos para dentro da EC2, foram criados testes unitários para api.py. Uma task de teste foi adicionada ao GitHub Actions para garantir que os testes fossem executados antes da construção da imagem Docker. A construção da imagem só ocorria se todos os testes unitários passassem.

Após ajustar essa tarefa, surgiram problemas na subida da imagem Docker e na estrutura de pastas criada anteriormente. Mesmo conseguindo localizar o contexto de pastas, faltava a pasta /app fora do contexto ou a pasta docker, resultando em erros na montagem dos arquivos dentro da EC2.

Ajustes Finais e Conclusão
O desenvolvedor optou por centralizar tudo na pasta app com todos os arquivos necessários e fazer a construção da imagem Docker a partir de uma pasta única. Após todos os ajustes necessários, foi finalizado o projeto, que está respondendo corretamente para os endpoints conforme os requisitos iniciais.

Ideias de Melhorias
Como melhorias para o processo, o desenvolvedor sugere:

Criação de um ECS com nome de cluster, IP e instâncias fixos.
Utilização do bucket S3 da Amazon para armazenar as imagens diretamente, fazendo apenas um push da imagem e montando diretamente dentro do cluster.