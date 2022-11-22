# FlyGraph

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0089792  |  João Victor Correia de Oliveira |
| 19/0020601  |  Victor Buendia Cruz de Alvim |

## Sobre 
O FlyGraph é uma aplicação web que tem como objetivo verificar a integridade de uma base de dados real de voos da ANAC utizando o conceito de grafos e encontrar o menor caminho entre dois aeroportos brasileiros. Convertendo os dados de uma planilha(.csv) pública para um grafo direcionado foi utilizado o algoritmo de reversão para checar a conectividade do grafo, caso ele não seja fortemente conectado existe um aeroporto inalcançável que será exibido. Para encontrar o menor caminho entre dois destinos foi aplicado o algoritmo de busca em largura(BFS). 

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python(Back-end) e JavaScript(Front-End) <br>
**Framework**: Django Rest e React <br>

#### Opção 1- Utilizando Docker
```
sudo docker-compose up --build
```
#### Opção 2- Para desenvolvimento 
```
cd djangoConfig/
pip install requirements.txt
```
 
Como desenvolvimento é necessário entrar no arquivo frontend/services/api.js e alterar a URL de requisições para a porta do Django: 
```
  baseURL: 'http://127.0.0.1:8000/'
```
```
cd frontend/
sudo npm i
npm run build

cd .. 

python3 manage.py runserver
```

## Uso 
Opção 1 - Após executar o comando de build do docker, basta acessar a url: http://localhost:3000/
Caso seja necessário subir novamente o container:
```
sudo docker-compose up 
```

Opção 2 - Após instalar as dependências e rodar o server python, basta acessar a url: http://127.0.0.1:8000/

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




