# NomedoProjeto

**Número da Lista**: 3<br>
**Conteúdo da Disciplina**: Grafos 1<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 19/0089792  |  João Victor Correia de Oliveira |
| 19/0020601  |  Victor Buendia Cruz de Alvim |

## Sobre 
O _Nome do Projeto_ tem como objetivo verificar a integridade de uma base de dados real de voos da ANAC utizando o conceito de grafos e encontrar o menor caminho entre dois aeroportos brasileiros. Convertendo os dados de uma planilha(.csv) pública para um grafo direcionado foi utilizado o algoritmo de reversão para checar a conectividade do grafo, caso ele não seja fortemente conectado existe um aeroporto inalcançável que será exibido. Para encontrar o menor caminho entre dois destinos foi aplicado o algoritmo de busca em largura(BFS). 

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação 
**Linguagem**: Python(Back-end) e JavaScript(Front-End) <br>
**Framework**: Django Rest e React <br>


```
sudo docker-compose up --build
```

## Uso 
Após executar o comando de build do docker, basta acessar a url: http://localhost:3000/
Caso seja necessário subir novamente o container:
```
sudo docker-compose up 
```

## Outros 
Quaisquer outras informações sobre seu projeto podem ser descritas abaixo.




