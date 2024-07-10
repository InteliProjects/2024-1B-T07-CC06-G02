# Complexidade e corretude do algoritmo

## Introdução

&emsp;&emsp; A empresa Aegea deseja otimizar as rotas de leitura dos hidrômetros, equipamentos que medem o uso de água nas residencias. Essa medição é feita por meio de leituristas, que trabalham, em média, 22 dias por mês e 6h por dia. Nesse documento, considerando o problema e a limitação passada, o grupo Onda apresenta a solução e a análise de sua complexidade.

## Algoritmos escolhidos

&emsp;&emsp;Para a solução idealizada, foram usadas 2 algortimos:

 - Christofides, através da biblioteca [NetworkX](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.approximation.traveling_salesman.christofides.html)
 - MiniBatchKMeans, através da biblioteca [SciKit learn](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.MiniBatchKMeans.html)

 ##### MiniBatchKMeans
&emsp;&emsp;O algoritmo K-Means é um método de clusterização que agrupa dados em k clusters distintos. Começando com a seleção aleatória de k pontos como centróides iniciais, cada ponto de dado é atribuído ao cluster cujo centróide é mais próximo, seguido pela atualização dos centróides com base na média dos pontos atribuídos a cada cluster. Esse processo de atribuição e atualização é repetido iterativamente até que os centróides se estabilizem. 

&emsp;&emsp;O MiniBatchKMeans é uma variação do algoritmo KMeans. Enquanto o algoritmo KMeans padrão atualiza os centróides de cada cluster utilizando todo o conjunto de dados a cada iteração, o MiniBatchKMeans atualiza os centróides utilizando apenas um subconjunto (mini-batch) dos dados. Isso o torna mais eficiente computacionalmente, especialmente para grandes conjuntos de dados como o que foi passado pela Aegea.

##### Christofides 
&emsp;&emsp;O algoritmo de Christofides é uma técnica aproximada para resolver o Problema do Caixeiro Viajante (TSP), conhecido por garantir uma solução cujo custo não excede mais que 50% do custo ótimo. Desenvolvido por Nicos Christofides em 1976, o método combina várias estratégias de otimização combinatorial.  Começando pela criação de uma árvore geradora mínima, ele seleciona um conjunto de vértices de grau ímpar nessa árvore, garantindo que haja um número par deles de acordo com o Lema do Aperto de Mãos. Em seguida, busca um emparelhamento perfeito de peso mínimo entre esses vértices. Com as arestas desse emparelhamento e da árvore geradora mínima, forma-se um multigrafo onde todos os vértices têm grau par. A partir desse multigrafo, é construído um circuito euleriano. Por fim, esse circuito euleriano é convertido em um circuito hamiltoniano, eliminando vértices repetidos. Essa abordagem, embora não garanta a solução ótima, geralmente produz soluções próximas em tempo polinomial, tornando-a útil em muitas situações práticas. Veja a seguir um exemplo de como o algoritmo funciona:
<div align="center">
  <p><b>Tabela 1 </b> - Esquema de funcionamento do algoritmo Christofides</p>
  
| | | |
| --- | --- | --- |
| ![Metrischer Graph mit 5 Knoten](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Metrischer_Graph_mit_5_Knoten.svg/300px-Metrischer_Graph_mit_5_Knoten.svg.png)Gráfico completo cujas arestas obedecem a desigualdade triangular | ![Christofides MST](https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/Christofides_MST.svg/300px-Christofides_MST.svg.png) Calcula a árvore geradora mínima T | ![V'](https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/V%27.svg/300px-V%27.svg.png) Calcula o conjunto de vértices O com grau ímpar em T|
| ![G V'](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/G_V%27.svg/300px-G_V%27.svg.png)Forma o subgrafo de G usando apenas os vértices de O | ![Christofides Matching](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Christofides_Matching.svg/300px-Christofides_Matching.svg.png)Constrói um acoplamento perfeito de peso mínimo no subgrafo M | ![TuM](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b4/TuM.svg/300px-TuM.svg.png) Une o emparelhamento e a árvore geradora  T ∪ M para formar um multigrafo Euleriano.|
| ![Eulertour](https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Eulertour.svg/300px-Eulertour.svg.png) Calcula o ciclo Euleriano | ![Eulertour bereinigt](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Eulertour_bereinigt.svg/300px-Eulertour_bereinigt.svg.png) Remove vértices repetidos, dando a saída do algoritmo | |  
<p>Fonte: https://handwiki.org/wiki/Christofides_algorithm</p>
</div>

## Análise dos algoritmos escolhidos

#### Prova de Corretude para o Kmeans**

&emsp;&emsp;Segundo (OSTROVSKY et al., 2013) o KMeans pelo método de Lloyd possui complexidade $O(i \times  n \times k \times d)$, sendo $i =$  Número máximo de iterações, $n=$ Número de pontos, $k =$ Número de clusters, $d =$ número de atributos em cada ponto.

- **Melhor Caso:**  ocorre quando  o algoritmo converge rapidamente. Nesse caso, a complexidade se aproxima de $O(n \times k \times d)$, onde $n$ é o número de pontos, $k$ é o número de clusters e $d$ é o número de atributos em cada ponto.

- **Pior Caso:** O pior caso ocorre quando  o algoritmo leva muitas iterações para convergir. Nesse caso, a complexidade é mais próxima de $O(i \times n \times k \times d)$, onde $i$ é o número máximo de iterações.
  
#### Invariante com justificativa
$C_i$ é o conjunto de pontos pertencentes ao cluster $i$, e $\mu_i$ o centroide do cluster $i$. 

$$ I_t = \sum_{i=1}^{k} \sum_{x \in C_i} ||x - \mu_i||^2$$
  $$I_{t+1} \leq I_t$$


&emsp;&emsp;Essa expressão mostra a soma das distâncias ao quadrado de todos os pontos $x$ pertencentes aos clusters $C_i$ até seus respectivos centroides $\mu_i$. A cada iteração do algoritmo KMeans MiniBatch, os centroides são atualizados e os pontos são realocados para os clusters mais próximos. Essa soma das distâncias ao quadrado dos pontos aos centroides permanece constante ou diminui a cada iteração.

#### Demonstração da corretude

- **Passo base:** Para $k = 1$, temos apenas um cluster. O centróide desse cluster será o centróide inicial e não haverá atribuição de pontos ou atualização de centróides. Portanto, o algoritmo retorna o centróide inicial, que é a solução correta para $k = 1$.

- **Hipótese de Indução:** Suponha que o algoritmo KMeans MiniBatch seja correto para $k = m$, ou seja, após a $m$-ésima iteração, os centróides convergem para uma solução correta com $m$ clusters.

- **Passo de Indução:** Vamos provar que o algoritmo também é correto para $k = m + 1$.
   - Após a $(m+1)$-ésima iteração, os centróides são atualizados para os $m+1$ clusters. Os pontos serão atribuídos aos clusters correspondentes com base nos novos centróides.
   - Como a atribuição de pontos é baseada na proximidade dos centróides, cada ponto é atribuído ao cluster mais próximo de acordo com os novos centróides.
   - Os centróides são recalculados como a média dos pontos atribuídos a cada cluster.
   - Se os novos centróides estiverem próximos o suficiente aos centróides anteriores, consideramos que o algoritmo convergiu e retorna a solução com $m + 1$ clusters.
   - Caso contrário, o algoritmo continua iterando até a convergência ou até atingir o número máximo de iterações.

#### Christofides
&emsp;&emsp; De acordo com Christofides (1976), a complexidade de tempo desse algoritmo é $O(n^3)$, o que significa que a o tempo cresce exponenicialmente com o número de hidrômetros a serem avaliados. Nesse algoritmo em específico, tanto o pior quanto o melhor caso possuem coplexidade de tempo $O(n^3)$, pois a disposição dos hidrômetros não afeta as decisões do algoritmo. Independente dos resultados obtidos até o momento, ele passará por todos os pontos, mesmo que já tenha encontrado a solução ótima.

#### Invariante com justificativa:
Seja $T$ o conjunto de arestas pertencentes à árvore de extensão mínima (AEM) parcial construída até o momento. A invariante do laço pode ser expressa como:

$|T| \leq |V|$


 indicando que o número de arestas na árvore de extensão mínima parcial $T$ é menor ou igual ao número de vértices no grafo $G$.


### Prova do Algoritmo de Christofides

De acordo com D. Arun(ARUN; PANDU RANGAN), a razão de aproximação de 3/2 é derivada da seguinte maneira:

1. *Árvore Geradora Mínima (MST)*:
   - O peso da MST, $w(T)$, é no máximo o peso do percurso TSP ótimo, $w(OPT)$. Isso porque removendo qualquer aresta do percurso TSP obtemos uma árvore geradora.
   - Portanto, $w(T) \leq w(OPT)$.

2. *Emparelhamento de Peso Mínimo (M)*:
   - Seja $O$ o conjunto de vértices de grau ímpar em $T$.
   - Pelo Lema do Aperto de Mãos, o número de vértices de grau ímpar é par, então existe um emparelhamento perfeito.
   - O peso do emparelhamento de peso mínimo $M$ em $O$, $w(M)$, é no máximo metade do peso do percurso TSP ótimo, $w(OPT)$. Isso se deve ao fato de que em qualquer percurso, o emparelhamento ótimo dos vértices dá, pelo menos, o emparelhamento de peso mínimo.
   - Portanto, $w(M) \leq 0.5 \cdot w(OPT)$.

3. *Circuito Euleriano e Eliminação de Vértices Repetidos*:
   - O grafo combinado $G'$ com arestas $T \cup M$ é euleriano, com todos os vértices tendo grau par.
   - Encontrar um circuito euleriano em $G'$ dá um percurso que visita cada vértice pelo menos uma vez.
   - A eliminação dos vértices repetidos resulta em um ciclo hamiltoniano cujo peso é no máximo o peso do circuito euleriano.
   - Assim, o peso do ciclo hamiltoniano é no máximo $w(T) + w(M) \leq w(OPT) + 0.5 \cdot w(OPT) = 1.5 \cdot w(OPT)$.

### Indução para Generalização da Prova
A prova pode ser generalizada usando indução no número de vértices, ou hidrômetros. Por exemplo, os pontos 
**1** : (-22.858956, -43.338632)
 **2** : (-22.830781, -43.39501)
 **3** : (-22.821902;-43.415018;)


**Caso Base**: Para um pequeno número de vértices (por exemplo, $n = 3$), o algoritmo constrói diretamente um percurso, o único possível.

**Hipótese de indução**:
   - Assuma que o algoritmo fornece uma aproximação de 3/2 para qualquer grafo com $n$ vértices.
   - Considere um grafo com $n+1$ vértices:
     - Remova um vértice e aplique o algoritmo aos $n$ vértices restantes.
     - A hipótese de indução garante uma aproximação de 3/2 para o grafo de $n$ vértices.

**Passo de indução**
     - Reinsira o vértice removido e ajuste a MST, emparelhamento, e circuito euleriano conforme necessário.
     - A adição de um vértice não aumentará a razão de aproximação além de 3/2, pois os passos adicionais seguem os mesmos princípios delineados acima.

### Conclusão
&emsp;&emsp;O algoritmo de Christofides garante um ciclo hamiltoniano dentro de 1.5 vezes o comprimento do percurso ótimo ao combinar MST, emparelhamento de peso mínimo e circuitos eulerianos, aproveitando as propriedades das árvores geradoras e emparelhamentos para limitar o peso total.

### Referências

Christofides, Nico. **Worst-case analysis of a new heuristic for the travelling salesman problem**, Report 388, Graduate
School of Industrial Administration, Carnegie-Mellon University, Pittsburgh, PA. Disponível em:  https://apps.dtic.mil/sti/pdfs/ADA025602.pdf Acesso em 2 jun 2024


OSTROVSKY, R. et al. **The effectiveness of lloyd-type methods for the k-means problem.** Disponível em:
http://users.cms.caltech.edu/~schulman/Papers/ostrovskyRSS12.pdf. Acesso em:  2 jun 2024

AN, H.-C.; KLEINBERG, R.; SHMOYS, D. B. **Improving Christofides’ Algorithm for the s-t Path TSP**.Acesso em 3 jun 2024. Disponível em: https://arxiv.org/pdf/1110.4604

BLÄSER, M.; PANAGIOTOU, K.; RAO, B.**A Probabilistic Analysis of Christofides’ Algorithm.** Disponível em: <http://www.cse.iitm.ac.in/~bvrr/conf/swat12.pdf>. Acesso em: 4 jun. 2024.

ARUN, D.; PANDU RANGAN, K. INFORMATIQUE THÉORIQUE ET APPLICATIONS **Approximation algorithms for the traveling salesman problem with range condition.**  Disponível em: <http://www.numdam.org/item/ITA_2000__34_3_173_0.pdf>. Acesso em: 6 jun. 2024.
