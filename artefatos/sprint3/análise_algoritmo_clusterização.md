# Análise de Resultados Algoritmo de Clusterização e Roteamento 
## Introdução

&emsp;&emsp;A empresa Aegea Saneamento e Participações S.A. está focada em otimizar as rotas de leitura de hidrômetros para coletar os dados de consumo de água dos clientes de forma mais eficiente. Isso é vital para economizar recursos e tempo, impactando diretamente o faturamento e a entrega das contas de água. Para isso, aqui foi aplicada a estratégia de clusterização e roteamento por TSP.

&emsp;&emsp; Caminho para o algoritmo : `codigo\algoritmo\cluster_tsp.py`

&emsp;&emsp;A aplicação dessa abordagem de clusterização e roteirização traz diversos benefícios, entre eles:

- **Redução da Distância Percorrida:** A clusterização agrupa pontos próximos, minimizando as distâncias percorridas pelos leituristas.
- **Otimização do Tempo:** A divisão das rotas em subclusters diários permite uma melhor gestão do tempo, respeitando o limite de 6 horas de trabalho por dia.
- **Segurança:** Diminuir as travessias de rua reduz o risco de acidentes, proporcionando maior segurança aos leituristas.
- **Eficiência Operacional:** A eficiência na coleta de dados de consumo pode aumentar a satisfação dos clientes e melhorar a adimplência.

A subdivisão em subclusters e a roteirização otimizada são alinhadas com os objetivos do projeto, promovendo uma operação mais eficiente e econômica, com impactos positivos na logística e no faturamento da empresa.

 
## Metodologia 

1. **Leitura e Pré-processamento de Dados**:
   
   * O código começa importando as bibliotecas necessárias, como pandas para manipulação de dados, MiniBatchKMeans para clusterização, StandardScaler para normalização de dados, haversine para cálculo de distância entre coordenadas geográficas e networkx para resolver o Problema do Caixeiro Viajante (TSP).
   * Em seguida, é feita a leitura do arquivo CSV que contém os dados dos hidrômetros, onde as coordenadas de latitude e longitude são normalizadas para facilitar o processamento.

2. **Função `calculate_route_duration`**:
   
   * Esta função calcula a duração total de uma rota, levando em consideração o tempo gasto em cada leitura e a velocidade média de deslocamento entre os pontos.

3. **Função `solve_tsp_networkx`**:
   
   * A função solve_tsp_networkx é descrita como uma implementação para resolver o Problema do Caixeiro Viajante (TSP) utilizando a biblioteca NetworkX. A função cria um grafo completo onde cada nó corresponde a um local a ser visitado e cada aresta representa a distância entre dois locais, calculada pela fórmula de haversine que considera a curvatura da Terra. Dentro desta implementação do TSP, é utilizado especificamente o algoritmo de Christofides, fornecido pela biblioteca NetworkX, para encontrar uma solução aproximada eficiente para o problema.
   * O algoritmo de Christofides é uma técnica aproximada para resolver o Problema do Caixeiro Viajante (TSP), conhecido por garantir uma solução cujo custo não excede mais que 50% do ótimo. Desenvolvido por Nicos Christofides em 1976, o método combina várias estratégias de otimização combinatorial. Primeiramente, constrói-se a mínima árvore geradora do grafo, garantindo a conexão de todos os vértices com o menor custo possível. Em seguida, identificam-se os vértices de grau ímpar dentro da árvore, e realiza-se um emparelhamento mínimo desses vértices para formar um subgrafo onde todos os graus são pares. Combinando a árvore geradora mínima e o emparelhamento, obtém-se um multigrafo no qual é possível encontrar um circuito euleriano, que percorre cada aresta uma única vez. Por fim, o circuito é transformado em um ciclo hamiltoniano, passando por cada vértice uma única vez, através do processo de eliminação de repetições de vértices, resultando em uma solução viável e eficiente para o TSP.

4. **Clustering e Roteirização**:
   
   * O código então realiza duas etapas de clusterização e roteirização:
       * Primeiro, ele faz a clusterização dos hidrômetros em clusters de leituristas (350 clusters).
       * Em seguida, dentro de cada cluster de leituristas, ele faz uma segunda clusterização para criar subclusters diários (22 subclusters), representando os dias de leitura.
       * Para cada subcluster diário, é resolvido o TSP usando a função `solve_tsp_networkx`.
       * Se a duração da rota exceder 6 horas (limite estabelecido), a rota é dividida em partes menores para garantir a eficiência operacional.

5. **Armazenamento e Exportação de Resultados**:

&emsp;&emsp; Caminho para o resultado : `codigo\results\rotas_clusters.py`
   
   * As rotas otimizadas são armazenadas em um DataFrame e exportadas para um arquivo CSV chamado "rotas_clusters.csv".
   * Além disso, um arquivo Excel é gerado com informações detalhadas, incluindo índices, coordenadas geográficas, códigos de rota, sequências, logradouros, números, indicação de novas rotas se a duração exceder 6 horas e o dia da rota.

### 4. Resultados


- *Armazenamento das Rotas*: As rotas otimizadas são armazenadas em um DataFrame e, em seguida, exportadas para um arquivo CSV. Isso facilita a implementação das rotas no processo diário de leitura dos hidrômetros.
- *Exportação para Excel*: Um arquivo Excel é gerado com os clusters, incluindo colunas detalhadas para uma análise aprofundada e aplicação prática:
- **`CLUSTER_LEITURISTA`**: Representa o agrupamento de leituristas, associando cada ponto de leitura a um grupo específico de trabalhadores, o que facilita a organização e distribuição das tarefas.

- **`CLUSTER_DIA`**: Indica a associação de cada ponto de leitura a um dia específico, organizando o trabalho por dias para melhor distribuição do tempo e recursos ao longo do mês.

- **`ROTA`**: Identificador de rota específica para o conjunto de pontos de leitura, fundamental para direcionar os leituristas ao longo de seu percurso diário.

- **`INDICE`**: Identificador único para cada registro ou ponto de leitura no conjunto de dados, útil para referenciar pontos específicos durante análises ou operações subsequentes.

- **`LATITUDE`** e **`LONGITUDE`**: Coordenadas geográficas de cada ponto de leitura, essenciais para mapear a localização física de cada hidrômetro ou ponto de serviço.

- **`CODIGO_ROTA`**: Identificador que representa uma rota específica à qual o ponto de leitura pertence, facilitando a organização das rotas e a atribuição de leituristas.

- **`SEQUENCIA`**: Número que indica a sequência em que os pontos devem ser visitados dentro de uma rota específica, otimizando o caminho percorrido.

- **`LOGRADOURO`**: Nome da rua ou localização onde o ponto de leitura está situado, proporcionando informações contextuais para a localização física.

- **`NUMERO`**: Número do edifício ou endereço específico onde o ponto de leitura está localizado, fornecendo precisão adicional para a localização.

- *Métricas de Avaliação*:

  - **Tempo Médio de Rota:** Cada rota durar 6 horas.
  - **Leituras por Mês:** 22 leituras por mês.
  - **Tempo de Execução do Algoritmo:** em média de 1 minuto.
  - **Kilometragem Diária:** Em média são percorridos 13.6 km por dia, em um ritmo de 5 km/h.


<div align="center">
<sub>Figura 1 - Tempo de Distância Percorrida Por Dia </sub>
<img src="..\assets\result_1.png" width="100%" >
<sup>Fonte: Elaboração G2</sup>
</div>

<div align="center">
<sub>Figura 2 - Distância Percorrida</sub>
<img src="..\assets\result_2.png" width="100%" >
<sup>Fonte: Elaboração G2</sup>
</div>

## Conclusão

&emsp;&emsp;Através da análise e avaliação dos resultados obtidos com a aplicação do algoritmo de clusterização e roteirização no projeto de otimização de rotas de leitura de hidrômetros, podemos concluir que a implementação foi bem-sucedida em vários aspectos fundamentais para a melhoria das operações da Aegea Saneamento e Participações S.A.P rimeiramente, a redução significativa na distância total percorrida pelos leituristas é um indicativo claro de eficiência operacional. Ao minimizar as distâncias entre os pontos de leitura, não apenas se economiza tempo, mas também se reduzem os custos operacionais associados ao transporte. Este resultado se alinha diretamente com os objetivos estratégicos da empresa de aumentar a eficiência enquanto reduz custos.

&emsp;&emsp;Adicionalmente, o algoritmo demonstrou uma capacidade robusta de organizar as rotas de forma que cada leiturista consiga completar suas leituras diárias dentro do limite de 6 horas de trabalho. Esta organização não só assegura a conformidade com as normas trabalhistas, mas também contribui para o bem-estar dos funcionários, evitando jornadas exaustivas e potencialmente perigosas.


&emsp;&emsp;Em conclusão, os resultados do projeto não apenas atendem às expectativas iniciais, mas também estabelecem uma base sólida para futuras melhorias. A Aegea Saneamento e Participações S.A. está agora melhor equipada para enfrentar os desafios operacionais e logísticos, promovendo uma maior satisfação do cliente e uma operação mais sustentável e econômica. Embora ainda haja espaço para ajustes finos — como aperfeiçoar o algoritmo para garantir que todas as rotas se mantenham rigorosamente dentro do tempo estipulado — os avanços já realizados são notáveis e promissores para futuras iterações do projeto.

