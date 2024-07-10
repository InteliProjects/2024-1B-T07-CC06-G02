# Documentação de Testes Postman

Esta documentação descreve os testes realizados no Postman para validar a funcionalidade da integração do projeto Onda.


### Solicitação: Submit Simulated Annealing (submitsa)
<div align="center">
  <p><b>Figura 1 </b> - Submit SA</p>
  <img src="..\assets\submitsa.jpg">
  <p>Fonte: Elaboração Onda</p>
</div>

- **Método:** POST
- **URL:** `http://127.0.0.1:5000/submitsa`
- **Descrição:** Submete um arquivo para otimização de rotas utilizando o algoritmo Simulated Annealing.
- **Parâmetros:**
  - `file_path` (string): O caminho para o arquivo de dados.
  - `max_duration_hours` (integer): A duração máxima em horas para a otimização. (Opcional, padrão: 6)
  - `fraction` (float): A fração de dados a ser usada para a otimização. (Opcional, padrão: 0.01)

#### Testes

- Verifica se a resposta retorna um código de status 200 OK e, quando concluído, retorna a tabela com os resultados, isto é, a duração, a latitude, a longitude, a rota e a sequência.

### Solicitação: Submit Two-Opt (submitto)
<div align="center">
  <p><b>Figura 1 </b> - Submit TO</p>
  <img src="..\assets\submitto.jpg">
  <p>Fonte: Elaboração Onda</p>
</div>
- **Método:** POST
- **URL:** `http://127.0.0.1:5000/submitto`
- **Descrição:** Submete um arquivo para otimização de rotas utilizando o algoritmo Two-Opt.
- **Parâmetros:**
  - `file_path` (string): O caminho para o arquivo de dados.
  - `max_duration_hours` (integer): A duração máxima em horas para a otimização. (Opcional, padrão: 6)
  - `fraction` (float): A fração de dados a ser usada para a otimização. (Opcional, padrão: 0.01)

#### Testes

- Verifica se a resposta retorna um código de status 200 OK e, quando concluído, retorna a tabela com os resultados, que possui as colunas:

`DURAÇÃO`: Tempo de execução da rota.

`LATITUDE`: Latitude do ponto.

`lONGITUDE`: Longitude do ponto.

`ROTA`: Rota a qual o ponto pertence.

`SEQUÊNCIA`: Ordem em que o ponto será visitado na rota que pertence.


### Solicitação: Submit TSP (submittsp)
<div align="center">
  <p><b>Figura 3</b> - Submit TSP</p>
  <img src="..\assets\endpoint_tsp_1.png">
  <p>Fonte: Elaboração Onda</p>
</div>

- **Método:** POST
- **URL:** `http://127.0.0.1:5000/submittsp`
- **Descrição:** Submete um arquivo para otimização de rotas utilizando o algoritmo de Traveling Salesman Problem (TSP) adaptado.
- **Parâmetros:**
  - `file_path` (string): O caminho para o arquivo de dados.
  - `read_time` (integer): Tempo de leitura em segundos necessário antes de iniciar a otimização.
  - `speed` (float): Velocidade de deslocamento assumida para o cálculo da rota (em km/h).
  - `max_duration` (integer): Duração máxima em horas para a otimização.


#### Testes
- Os testes para o endpoint "submittsp" verificam a funcionalidade de submissão de tarefas de otimização de rotas usando o algoritmo Traveling Salesman Problem (TSP) adaptado. O primeiro teste, test_submittsp_task_success, utiliza a técnica de mock para substituir a função async_run_create_routes_for_cluster e verifica se, ao enviar um arquivo CSV corretamente através de uma solicitação POST, o servidor responde com um status 202 (Accepted) e retorna um ID de tarefa ('task_id'), indicando que a tarefa foi aceita para processamento. Este teste também confirma que a função mockada foi chamada exatamente uma vez. O segundo teste, test_submittsp_task_no_file, tenta enviar uma solicitação POST sem um arquivo anexado. Ele verifica se o servidor responde corretamente com um status 400 (Bad Request) e retorna uma mensagem de erro específica que indica que nenhum arquivo foi fornecido ou que o formato do arquivo é inválido, garantindo assim que o endpoint maneja adequadamente os erros de entrada.


### Solicitação: Check Status (checkstatus)
<div align="center">
  <p><b>Figura 1 </b> - Check Status</p>
  <img src="..\assets\status.jpg">
  <p>Fonte: Elaboração Onda</p>
</div>

- **Método:** GET
- **URL:** `http://127.0.0.1:5000/status/{{id_da_execucao}}`
- **Descrição:** Verifica o status de uma execução de otimização de rotas com base em seu ID.
- **Parâmetros:**
  - `id_da_execucao` (integer): O ID da execução de otimização.

#### Testes

- Verifica o status da execução e retorna `completed` quando a execução ocorre corretamente, `processing` quando o processamento ainda está ocorrendo e erro quando algo impede a execução. A mensagem de erro pode ser `Arquivo CSV não informado / Formato inválido`, indicando que o arquivo CSV não é fornecido no corpo da solicitação POST ou quando o formato do arquivo não termina com `.csv`; ou `Unexpected error`, que ocorre se algo der errado durante o processamento do envio da tarefa.

