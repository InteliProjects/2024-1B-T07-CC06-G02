# Entendimento do contexto do problema

&emsp;&emsp;Nesta seção, serão abordados os desafios enfrentados pela Aegea no que diz respeito às rotas de leitura de hidrômetros. A compreensão detalhada do contexto operacional, das limitações de recursos e dos objetivos específicos da empresa tem o objetivo de auxiliar a desenvolver uma solução eficaz.
## Contexto do Problema

&emsp;&emsp;A empresa Aegea Saneamento e Participações S.A. está buscando formas de otimizar as rotas de leitura de hidrômetros. Isso é crucial para garantir que os dados de consumo mensal de água dos clientes sejam coletados de forma eficiente. Atualmente, essa tarefa é realizada por leituristas que visitam as residências e registram o consumo de água. No entanto, o processo atual envolve uma grande quantidade de leituristas e rotas, o que exige uma logística complexa e consome muito tempo.

O principal objetivo da otimização é reduzir a distância percorrida pelos leituristas. Isso não só economizaria tempo e recursos, mas também teria um impacto direto no faturamento da empresa e na entrega das contas de água. Além disso, uma melhoria na eficiência do processo pode influenciar positivamente a adimplência dos clientes.

É importante considerar também outros aspectos relevantes do domínio do problema, como a necessidade de realizar a leitura dentro do prazo de 22 dias, que representam em média os dias úteis do mês, com carga de trabalho de até 6 horas por dia. Além disso, é desejável diminuir as travessias de rua para garantir maior segurança e eficiência para os leituristas.

## Dados Disponíveis:

&emsp;&emsp;Os dados fornecidos pelo parceiro de projeto para esta solução incluem informações geográficas e operacionais para cada ponto de leitura. Foram disponibilizados dois conjuntos de dados: "AMOSTRA_MENOR" e "AMOSTRA_TOTAL", a amostra menor possuí uma quantidade significantemente menor de pontos de leitura, que também estão mais estruturados no mapa, enquanto a amostra maior contemplava um registro bem mais abrangente de pontos, possuindo uma variedade de distribuição de rotas, coordenadas e endereços.

Esses dados incluem os seguintes campos:

- **ÍNDICE**: Um identificador único para cada registro de leitura, que pode ser usado para referenciar específicas entradas de dados.

- **LATITUDE** e LONGITUDE: Coordenadas geográficas de cada local de leitura, essenciais para calcular distâncias e traçar rotas entre os pontos de leitura.

- **CÓDIGO_ROTA**: Um identificador que agrupa pontos de leitura em rotas específicas, o qual pode ser utilizado para entender agrupamentos prévios e otimizar baseado nas configurações existentes.

- **SEQUÊNCIA**: Uma numeração que indica a ordem em que os pontos devem ser visitados dentro da rota.

- **LOGRADOURO**: O nome da rua ou local onde o hidrômetro está localizado.

- **NÚMERO**: O número do local no logradouro onde o hidrômetro está instalado.

## Objetivo do Problema

&emsp;&emsp;Para o atual problema, o objetivo é desenvolver um otimizador que possa determinar a melhor configuração de agrupamentos e sequenciamento das rotas de leitura de hidrômetros. Especificamente, o otimizador deve concentrar-se em minimizar a distância percorrida pelos leituristas e possivelmente reduzir as travessias de rua durante as rotas. Isso contribuirá para uma operação mais eficiente, reduzindo o tempo necessário para concluir as rotas e potencialmente diminuindo o risco de acidentes. A implementação bem-sucedida dessa solução tem o potencial de aumentar a eficácia geral do processo, mesmo que alguns outros objetivos não sejam trabalhados neste momento, futuramente poderão ser implementados na estruturação do problema.

&emsp;&emsp;O desenvolvimento do otimizador busca resolver essas questões ao proporcionar uma forma consistente e eficiente de traçar as rotas:

1. **Automatização**: Agrupa e sequencia as rotas de forma ideal através de algoritmos, garantindo a otimização das visitas.

2. **Gestão Flexível**: Permite ajustar o número de leituristas e simular cenários variados, adaptando-se às mudanças nas necessidades operacionais.

3. **Análise de Impacto**: Facilita simulações de mudanças, como reduzir leituristas ou alterar tempos de leitura, avaliando rapidamente os efeitos nas métricas de desempenho.

## Recursos que Apresentam Limitações no Sistema

&emsp;&emsp;Um recurso que apresenta limitação em um sistema é um componente ou fator cujas restrições afetam a eficiência ou capacidade operacional do sistema. Tais recursos podem ser tangíveis, como equipamentos e materiais, ou intangíveis, como tempo e capacidade de trabalho. As limitações desses recursos frequentemente definem o escopo dentro do qual o sistema pode operar efetivamente e influenciam diretamente a estratégia de gestão e planejamento. No contexto atual de sistemas operacionais e logísticos, entender e gerenciar essas limitações é crucial para otimizar processos, maximizar a produtividade e evitar gargalos que possam comprometer o desempenho e os resultados esperados. Para este projeto, dois recursos críticos que apresentam limitações significativas são:

1. **Tempo de Trabalho Diário dos Leituristas**: Conforme o projeto descreve, cada leiturista tem um limite de 6 horas de trabalho por dia para completar as rotas. Essa limitação impacta diretamente a quantidade de ligações que um leiturista pode efetivamente visitar em um único dia, bem como a extensão das rotas que podem ser atribuídas. Se o tempo necessário para completar uma rota excede o limite diário de trabalho, isso exigiria a redistribuição das ligações para outros dias ou outros leituristas, potencialmente aumentando o número de dias necessários para completar todas as leituras ou o número de leituristas necessários.

2. **Dias de Leitura**: O domínio do problema estabelece que todas as leituras devem ser concluídas em um intervalo máximo de 22 dias. Esta restrição temporal é um fator importante que influencia a programação das rotas e a alocação de recursos. Se as rotas não forem otimizadas para maximizar a eficiência dentro deste período, a Aegea pode enfrentar problemas com o atraso na verificação de hidrômetros, o que afetaria subsequentemente o faturamento e a adimplência dos clientes. Portanto, é fundamental que o algoritmo de otimização considere essa restrição para garantir que todas as ligações sejam atendidas dentro do prazo estipulado, sem comprometer a qualidade e a precisão das leituras.

## Expressões Matemáticas

&emsp;&emsp;A fim de relacionar o contexto, os dados disponíveis, as restrições e o objetivo do problema, são formuladas expressões matemáticas que representam de forma objetiva as influencias de cada um no resultado buscado.

##### Parâmetros

$a$: Dias de leitura

$b$: Horas de trabalho diárias

$c$: Velocidade de leiturista

$d$: Tempo de leitura

$e$: Quantidade de leituristas

$f:$ Número total de rotas

$g_{ij}:$ Distância entre clientes $i-j$

##### Variáveis de decisão:

$x_{ij}=  1$, se o cliente j for visitado após i; 0 caso não seja visitado.

#### Função objetivo

Minimizar a distância percorrida por cada leiturista:
$$Min D = \sum_{x=0}^{x} \sum_{g=0}^{g} x_{ij} \cdot g_{ij}$$

&emsp;&emsp;onde $x_{ij}$ representa se o leiturista visitará o cliente $j$ após $i$, isto é, percorrerá o trecho $i-j$ e $g_{ij}$ representa a distância entre o cliente $i$ e $j$. Para simplificar o problema, foi considerado o modelo do caixeiro viajante para modelar a distância percorrida para cada rota. A soma das distâncias de cada rota será incluída em breve.

#### Restrições

- O número de dias deve ser menor que 22: $$a \leq 22$$
- O número de horas trabalhadas por dia deve ser menor que 6 horas: $$b \leq 6$$
- Assim, o tempo $T$ disponível para completar todas as rotas devem ser menores que o número de dias vezes as horas diárias:
  $$T \leq a \cdot b $$

- O tempo de leitura de cada rota é calculado pela distância entre os clientes e a velocidade do leiturista, e a soma de todos os tempos de leitura deve ser menor que o tempo disponível para completar todas as rotas:

$$t_{ij} = \frac{g_{ij}}{c}$$

  $$\sum_{x=0}^{x} \sum_{g=0}^{g} x_{ij} \cdot t_{ij} \leq a \cdot b \cdot e $$
- Todos os clientes devem ser visitados uma vez:
  $$\sum_{j=1}^{N} x_{ij} = 1, \quad \forall i
  \sum_{i=1}^{N} x_{ij} = 1, \quad \forall j$$
  
- Não pode haver subciclos :

  S é o subconjunto de nós, $i$ e $j$ são nós em $S$ e $i \neq j$:
$$\sum_{i \in S} \sum_{j \in S, j \neq i} x_{ij} \geq 1$$

### Condições para Parâmetros de Entrada

- Dias de leitura, horas de trabalho diárias, velocidade de leiturista, tempo de leitura e quantidade de leituristas não podem possuir valores negativos:
  $$a, b, c, d, e, f, g > 0$$
- O número de leituristas é um número inteiro:
  $$e \in \mathbb{Z}^{+}$$


&emsp;&emsp;Em conclusão, as expressões matemáticas apresentadas são do processo de resolução de problemas de otimização, fornecendo uma descrição mais precisa do problema e permitindo a aplicação de técnicas matemáticas e computacionais para encontrar soluções eficientes. Esse processo ajuda a montar um possível caminho de resolução.


## Análise de sensibilidade

&emsp;&emsp;A análise de sensibilidade permite perceber a importância de cada variável no valor final e avaliar o impacto de mudar cada uma.

&emsp;&emsp;Para fazer a análise de sensibilidade, foram escolhidos 5 pontos aleatórios dos dados. Veja a seguir:

| Ponto | LATITUDE    | LONGITUDE    |
|--------|-------------|--------------|
| 1      | -22.815.031 | -43.323.595  |
| 2      | -22.802.546 | -43.327.089  |
| 3      | -22.802.738 | -43.324.031  |
| 4      | -22.810.612 | -43.317.281  |
| 5      | -22.804.028 | -43.326.706  |

&emsp;&emsp;Para utilizar a função solver do Excel, foi feito um relaxamento da restrição de integralidade. A partir do resultado obtido nas primeiras iterações, os valores foram arredondados. Veja a seguir os valores das variáveis de decisão considerando a restrição de integralidade:
<div align="center">
  <p><b>Figura 1 </b>- Variáveis de decisão relaxadas </p>
  <img src="..\assets\decisao.png">
  <p>Fonte: Elaboração Onda</p>
</div>


<div align="center">
  <p><b>Figura 2 </b>- Variáveis de decisão respeitando a integralidade </p>
  <img src="..\assets\decisao2.png">
  <p>Fonte: Elaboração Onda</p>
</div>

&emsp;&emsp;Com esses pontos, foram calculadas as distancias entre um e outro e aplicado uma função que resolver problemas lineares no Excel, chamada Solver, e foi analisado o relatorio de sensibilidade gerado:

<div align="center">
  <p><b>Figura 3 </b>- Relatório de sensibilidade </p>
  <img src="..\assets\sensibilidade.png">
  <p>Fonte: Elaboração Onda</p>
</div>

&emsp;&emsp;Considerando as colunas de Valor Final e Custo Reduzido, são possíveis extrair algumas conclusões. Por exemplo, a célula E12, rota 1-4, possui valor final 1, o que significa que já está na resposta final; no caso da célula C12, o valor final igual a 0 indica que a célula, rota 1-2, não faz parte da solução e o custo reduzido indica quanto aumentaria na solução final caso esse trecho fosse adicionado na solução final.
De maneira geral, o custo reduzido demonstra o quanto cada uma das variáveis, cada trecho na rota montada, impacta na solução final. Nesse relatório, os valores são uma aproximação do valor real, já que são resultados do simplex relaxado.


