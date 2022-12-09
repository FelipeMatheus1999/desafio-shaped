# ------------------------- API Shaped ------------------------- 

## ENDPOINTS
> [GET] - `api/patient/` 
> 
> body: null <br><br>
> response:
> ```json
> [
>  {
>   "id": 1,
>   "name": "Keyla Alves da Silva",
>   "age": 23,
>   "address": "Rua Cecília Cavalcante"
>  }
> ]
> ```

<br>
<br>
<br>

> [POST] - `api/patient/` 
> 
> body:
> ```json
> {
> 	"name": "Keyla Alves da Silva",
> 	"age": 23,
> 	"address": "Some Address"
> }
> ```
> response:
> ```json
> {
>  "id": 1,
>  "name": "Keyla Alves da Silva",
>  "age": 23,
>  "address": "Rua Cecília Cavalcante"
> }
> ```

<br>
<br>
<br>

> [PATH] - `api/patient/` 
> 
> body:
> ```json
> {
> 	"name": "Some Name"
> }
> ```
> response:
> ```json
> {
>  "id": 1,
>  "name": "Some Name",
>  "age": 23,
>  "address": "Rua Cecília Cavalcante"
> }
> ```

<br>
<br>
<br>

> [DELETE] - `api/patient/` 
> 
> body: null <br><br>
> response: status 204 no content 

<br>
<br>
<br>

> [GET] - `api/exam/` 
> 
> body: null <br><br>
> response:
> ```json
> [
>  {
>   "id": 1,
>   "name": "Keyla Alves da Silva",
>   "age": 23,
>   "address": "Rua Cecília Cavalcante"
>  }
> ]
> ```

<br>
<br>
<br>

> [POST] - `api/exam/` 
> 
> body:
> ```json
> {
>  "professionals_name": "Some Name",
>  "weight": 70.5,
>  "height": 1.70,
>  "patient": 1
> }
> ```
> response:
> ```json
> {
>  "id": 1,
>  "professionals_name": "Some Name",
>  "weight": 70.5,
>  "height": 1.70,
>  "patient": {
>    "id": 1,
>    "name": "Some Name",
>    "age": 23,
>    "address": "Some Address" 
>  }
> }
> ```

<br>
<br>
<br>

> [PATH] - `api/exam/` 
> 
> body:
> ```json
> {
>  "professionals_name": "Some Name Patch"
> }
> ```
> response:
> ```json
> {
>  "id": 1,
>  "professionals_name": "Some Name Patch",
>  "weight": 23,
>  "height": "Rua Cecília Cavalcante",
>  "patient": {
>    "id": 1,
>    "name": "Some Name",
>    "age": "Some Age",
>    "address": "Some Address" 
>  }
> }
> ```

<br>
<br>
<br>

> [DELETE] - `api/exam/` 
> 
> body: null <br><br>
> response: status 204 no content 

<br>
<br>
<br>

## Rodando a aplicação
> 1 - Excute o comando `docker volume create --name=shaped_api_db` para criar o volume do docker. </br>
> 2 - Excute o comando `make migrate` para aplicar as migrações. </br>
> 3 - Excute o comando `make run` para rodar os serviços docker e leventar o servido na port 8000.

# -------------------------------------------------------------------- 