# Relatório Inicial de Análise de Algoritmos de Otimização de Rotas

## Introdução

&emsp;&emsp;O objetivo deste estudo é avaliar o desempenho de três algoritmos distintos de otimização de rotas aplicados a um conjunto de dados representativo das operações logísticas de um parceiro comercial. A análise foca em identificar o algoritmo que maximiza a eficiência das rotas em termos de duração média e pontos por rota, ao mesmo tempo que minimiza o tempo de processamento necessário.

## Descrição dos Algoritmos

### 1. Bad Algorithm

&emsp;&emsp;Este algoritmo serve como um ponto de referência inicial, operando com uma lógica de otimização básica. Ele simplesmente sequencia os pontos de rota conforme são apresentados no conjunto de dados, sem qualquer heurística avançada para otimização de percurso.

### 2. Two-Opt Algorithm

&emsp;&emsp;O algoritmo Two-Opt é uma heurística de refinamento que visa melhorar uma rota existente trocando iterativamente dois vértices. O objetivo é reduzir o percurso total ao eliminar cruzamentos de rotas e, assim, encurtar a distância de viagem. Este método é amplamente utilizado para resolver problemas do caixeiro-viajante e tem uma boa performance para problemas de tamanho moderado.

### 3. Simulated Annealing

&emsp;&emsp;Simulated Annealing é uma técnica probabilística para aproximar o mínimo global de uma função dada. Inspirado por processos de annealing em metalurgia, este algoritmo busca escapar de mínimos locais permitindo, em temperaturas mais altas, movimentos que podem piorar a solução, e gradualmente diminuindo a "temperatura" para estabilizar em uma solução ótima ou próxima do ótimo. É particularmente útil quando a paisagem de busca é irregular, com muitos mínimos locais.

## Metodologia

&emsp;&emsp;Os dados foram processados inicialmente através de `process_data`, selecionando um conjunto aleatório de rotas baseado no parâmetro, garantindo uma análise mais abrangente e menos enviesada. Após os processamentos, cada algoritmo foi executado algumas vezes com diferentes conjuntos de rotas e uma combinação específica de parâmetros para explorar as respostas dos algoritmos sob diferentes condições:

- **Bad Algorithm**: Executado com parâmetros padrão, utilizando apenas os dados e a duração máxima como entrada. Esta abordagem básica serviu como linha de base para as comparações.

- **Two-Opt**: Implementado inicialmente com a função de inicialização usando o método `nearest_neighbor`, seguido pela otimização Two-Opt. Este algoritmo foi testado em diferentes iterações com diferentes conjuntos de rotas para avaliar sua consistência em variados cenários.

- **Simulated Annealing**: Configurado com parâmetros específicos para controle de temperatura e iterações. Duas combinações de parâmetros foram testadas inicialmente, e nas próximas *sprints* haverão mais testes, e o algoritmo foi testado com vários conjuntos de dados para verificar a influência das variações nos resultados.

&emsp;&emsp;Cada execução foi cronometrada usando a biblioteca `time`, e as métricas de desempenho, incluindo duração média da rota, pontos médios por rota, e tempo total de processamento, foram coletadas meticulosamente para garantir uma análise abrangente.

## Resultados

&emsp;&emsp;Após iterações com diferentes conjuntos de dados e duas combinações de parâmetros para o Simulated Annealing, os resultados mostraram que:

- O **Bad Algorithm** apresentou resultados viáveis, porém consistentemente inferiores aos outros métodos em todas as iterações. Ele serviu como uma linha de base para comparações e demonstrou a importância de técnicas mais sofisticadas para a otimização de rotas.

- O **Two-Opt** consistentemente teve o melhor desempenho em termos de eficiência da rota, com a maior média de pontos por rota e a menor duração média, mesmo quando aplicado a diferentes conjuntos de rotas. No entanto, seu tempo de processamento foi significativamente maior, o que sublinha a necessidade de otimização computacional para reduzir o tempo de execução.

- O **Simulated Annealing** ofereceu um compromisso atraente entre tempo de execução e eficiência. Apesar de ligeiramente inferior ao Two-Opt em termos de eficácia em todas as iterações, seu tempo de processamento substancialmente menor o torna uma alternativa viável, especialmente em cenários onde a rapidez é crítica.

&emsp;&emsp;Estes resultados sugerem que, enquanto o Two-Opt pode ser o melhor em termos de minimização de duração da rota e maximização de pontos, a eficiência temporal do Simulated Annealing não deve ser subestimada, especialmente quando o tempo de processamento é uma consideração crítica.

<div align="center">
  <p><b>Figura 1 </b>- Iteração 1 </p>
  <img src="..\assets\iteration1.png">
  <p>Fonte: Elaboração Aegea</p>
</div>

<div align="center">
  <p><b>Figura 1 </b>- Iteração 2 </p>
  <img src="..\assets\iteration2.png">
  <p>Fonte: Elaboração Aegea</p>
</div>

## Conclusões e Recomendações

### Conclusões

&emsp;&emsp;A análise expõe que cada algoritmo possui suas forças e limitações, com o Two-Opt mostrando potencial para os melhores resultados de otimização de rota, enquanto o Simulated Annealing oferece um balanço entre qualidade e tempo de execução.

### Planejamento para Ações Futuras

- **Optimização do Two-Opt com Numba**: Explorar a otimização do código para reduzir o tempo de processamento, mantendo a qualidade dos resultados.

- **Ajuste Fino do Simulated Annealing**: Experimentar com diferentes configurações de temperatura e taxas de resfriamento para potencialmente melhorar tanto a eficácia quanto o tempo de execução.

- **Análise de Dados Mais Profunda**: Investigar os dados subjacentes para entender melhor como as características específicas dos dados influenciam o desempenho dos algoritmos.
