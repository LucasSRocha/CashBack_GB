# CashBack Grupo Boticário
[![Actions Status](https://github.com/LucasSRocha/CashBack_GB/workflows/Python%20application/badge.svg)](https://github.com/LucasSRocha/CashBack_GB/actions)
[![codecov](https://codecov.io/gh/LucasSRocha/CashBack_GB/branch/master/graph/badge.svg)](https://codecov.io/gh/LucasSRocha/CashBack_GB)

## Requisitos
- [docker](https://docs.docker.com/engine/install/)
- [docker-compose](https://docs.docker.com/compose/install)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)
- [python 3.8](https://www.python.org/downloads/3.8)

## Uso
### Instalação
```
$ git clone https://github.com/LucasSRocha/CashBack_GB.git
$ cd CashBack_GB
```
#### Local
Para utilizar o serviço local execute o comando:
```
$ make local-setup
$ make runserver
```
#### Docker
Para utilizar o serviço utilizando docker é necessário executar o comando abaixo:
```
$ make docker-setup
$ make run-docker
```

Dois contêineres serão criados (Postgres e Web).
Você pode acessar os contêineres da seguinte forma:
- Web: ``` $ docker-compose exec web bash ```
- Postgres:  ``` $ docker-compose exec db bash ```

### Testes
Dentro da venv execute:
```
$ make runtests
```

### Endpoints
#### Autenticação
Para realizar requisições na API é necessário validar o usuário no endpoint /users/auth/ descrito abaixo e utilizar o token de resposta no header das requisições da seguinte forma:
```Authorization: Bearer <token>```
#### Users
- /users/
    - Utilizado para criar novos usuários
    - metodo: POST
    - payload: 
    ```
    {
        "cpf": "string",
        "email": "string",
        "password": "string",
        "full_name": "string"
    }
    ```
- /users/<id>
    - Utilizado para obter os detalhes do usuário
    - metodo: GET
    
- /users/auth/
    - Utilizado para obter o token de acesso.
    - metodo: POST
    - payload: 
    ```
    {
        "email": "string",
        "password": "string"
    }
    ```
    - retorno:
      ```
      {
      "refresh": "string",
      "access": "string"
      }
      ```
- /users/auth/refresh/
    - metodo: POST
    - payload: 
    ```
    {
       "refresh": "string"
    }
    ```
#### Cashback
- /cashback/preapproved
    - metodo: POST
    - payload: 
    ```
    {
        "cpf": "string"
    }
    ```
 - /cashback/preapproved/<id>
     - metodo: [GET, DELETE, PUT]

- /cashback/sale
    - metodo: POST
    - payload: 
    ```
    {
        "code": "string",
        "value": float,
        "date": date(YYYY-MM-DD)
    }
    ```
 - /cashback/sale/<id>
     - metodo: [GET, DELETE, PUT]

 - /cashback/total
     - metodo: GET
