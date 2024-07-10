# Entendimento da Experiência do Usuário

## Personas

&emsp;&emsp;As personas<sup>1</sup> são representações fictícias do cliente ideal, construídas com base em dados reais e percepções sobre os comportamentos, motivações, desafios e aspirações dos consumidores. Essas ferramentas são fundamentais no marketing e no design, orientando o desenvolvimento de produtos, serviços e estratégias de comunicação que atendam às verdadeiras necessidades e desejos do público.

&emsp;&emsp;A importância das personas reside na capacidade de humanizar e segmentar o público de uma empresa, facilitando a compreensão por parte das equipes de marketing, vendas e desenvolvimento sobre quem são seus clientes e o que eles valorizam.<sup>2</sup> Isso permite que as empresas ofereçam experiências mais personalizadas e impactantes, aumentando a probabilidade de sucesso das iniciativas e a satisfação dos clientes. Utilizar personas também ajuda a focar os esforços, evitando ações genéricas ou dispersas e otimizando o uso de recursos.

<div align="center">
  <p><b>Figura 1 </b>- Persona : João Santos </p>
  <img src="..\assets\persona1.png">
  <p>Fonte: Elaboração G2</p>
</div>

<div align="center">
  <p><b>Figura 2 </b>- Persona : Adenor Barbosa </p>
  <img src="..\assets\persona2.png">
  <p>Fonte: Elaboração G2</p>
</div>


&emsp;&emsp;Assim, o estudo de personas é fundamental para o projeto, pois oferece uma compreensão profunda das necessidades, desafios e objetivos dos usuários. Isso permite a criação de soluções mais direcionadas, aumentando a eficácia e a satisfação do usuário. Ao entender quem são nossos usuários e o que eles valorizam, podemos desenvolver produtos e serviços que realmente atendam às suas expectativas, promovendo assim o sucesso do projeto de forma significativa.

## User Stories

&emsp;&emsp;As User Stories<sup>3</sup> são ferramentas essenciais no desenvolvimento ágil de software, representando requisitos funcionais sob a perspectiva dos usuários finais. Elas descrevem de maneira simples e concisa o que os usuários necessitam e por que, permitindo que a equipe de desenvolvimento alinhe as funcionalidades do sistema às expectativas reais dos usuários. Cada user story é estruturada em torno de uma necessidade específica e inclui critérios de avaliação e testes de aceitação que definem e verificam os requisitos para considerar a funcionalidade concluída. Este método não apenas garante que o sistema seja relevante e valioso para os usuários, mas também facilita a comunicação entre desenvolvedores e stakeholders, assegurando que todos os envolvidos tenham uma compreensão clara do que está sendo desenvolvido e do impacto esperado, tornando-se assim um investimento crucial na satisfação e na experiência do usuário final.

### Persona - Adenor Barbosa

#### User Story 1

| Campo | Descrição |
|----------------|-----------|
| *Número* | 001 |
| *História* | Como Adenor Barbosa, eu quero subir um arquivo CSV contendo as rotas e pontos de leitura atuais para o sistema, para que possam ser utilizados como base na otimização das rotas. |
| *Critério de Avaliação* | O sistema deve permitir o upload de um arquivo CSV e validar o formato e a integridade dos dados sem erros. |
| *Teste de Aceitação* | Resultado Esperado: O sistema aceita o arquivo CSV e confirma que os dados estão no formato correto. Resultado Indesejado: O sistema rejeita o arquivo inadequadamente ou não avisa sobre possíveis inconsitencia. |

#### User Story 2

| Campo | Descrição |
|----------------|-----------|
| *Número* | 002 |
| *História* | Como Adenor Barbosa, quero receber uma resposta processada pelo sistema que indique as rotas otimizadas para maximizar a eficiência das leituras. |
| *Critério de Avaliação* | O sistema deve processar o arquivo CSV e apresentar uma solução de rotas otimizadas dentro de um tempo razoável. |
| *Teste de Aceitação* | Resultado Esperado: O sistema apresenta uma solução de otimização de rotas em tempo viável para escolhas de operação após o upload do arquivo. Resultado Indesejado: O sistema demora muito para responder ou não apresenta solução possível e determinada. |

#### User Story 3

| Campo | Descrição |
|----------------|-----------|
| *Número* | 003 |
| *História* | Como Adenor Barbosa, quero visualizar os resultados da otimização na tela, para que eu possa fazer uma análise rápida e intuitiva das rotas sugeridas. |
| *Critério de Avaliação* | O sistema deve exibir na interface os resultados do processo de otimização de forma clara e compreensível. |
| *Teste de Aceitação* | Resultado Esperado: As rotas otimizadas são exibidas de forma organizada e visualmente acessível. Resultado Indesejado: As rotas e tabelas são difíceis de entender ou não são exibidas de maneira eficaz. |

#### User Story 4

| Campo | Descrição |
|----------------|-----------|
| *Número* | 004 |
| *História* | Como Adenor Barbosa, eu quero exportar os resultados otimizados para um arquivo CSV, para que eu possa carregá-los diretamente no sistema e aplicativo usado pelos leituristas. |
| *Critério de Avaliação* | O sistema deve permitir que o usuário exporte o resultado das rotas otimizadas em formato CSV. |
| *Teste de Aceitação* | Resultado Esperado: O sistema gera um arquivo CSV das rotas otimizadas que pode ser baixado e utilizado sem problemas. Resultado Indesejado: A exportação falha ou o arquivo não é compatível com o aplicativo dos leituristas. |

### Persona - João Santos

#### User Story 5

| Campo | Descrição |
|-------|-----------|
| *Número* | 005 |
| *História* | Como João Santos, eu quero monitorar as condições atuais das rotas em tempo real, para que eu possa tomar decisões rápidas sobre redirecionamentos em caso de imprevistos. |
| *Critério de Avaliação* | O sistema deve fornecer uma visão geral em tempo real das rotas e permitir a interação para a tomada de decisão instantânea. |
| *Teste de Aceitação* | Resultado Esperado: O sistema apresenta uma visualização atualizada em tempo real com interações possíveis para ajustes imediatos. Resultado Indesejado: O dashboard não reflete o estado atual ou é não-reativo a mudanças. |

#### User Story 6

| Campo | Descrição |
|----------------|-----------|
| *Número* | 006 |
| *História* | Como João Santos, eu quero poder escolher entre diferentes algoritmos de otimização no sistema, para testar e determinar qual apresenta os melhores resultados para nossas operações, ou então processamento mais rápidos. |
| *Critério de Avaliação* | O sistema deve oferecer uma seleção de algoritmos de otimização e permitir que o usuário escolha qual deseja aplicar. |
| *Teste de Aceitação* | Resultado Esperado: O usuário consegue selecionar entre algoritmos e executar a otimização desejada. Resultado Indesejado: O sistema não oferece opções ou falha ao aplicar o algoritmo selecionado. |

### User Story 7

| Campo | Descrição |
|-------|-----------|
| *Número* | 007 |
| *História* | Como João Santos, preciso personalizar os algoritmos de otimização de rotas para incluir parâmetros dinâmicos da nossa operação, tais como a prioridade de atendimento por região, variação de tráfego devido a obras e eventos locais, e padrões meteorológicos que afetam o tempo de leitura. Preciso que esses fatores sejam refletidos em um planejamento de rotas que se ajusta automaticamente, promovendo o uso eficaz do tempo dos leituristas e reduzindo os custos operacionais.|
| *Critério de Avaliação* | O sistema deve permitir que João insira dados operacionais variáveis e defina a importância de cada um no planejamento de rotas através de uma interface de usuário intuitiva. O sistema deve também calcular e sugerir rotas levando em consideração essas variáveis dinâmicas.|
| *Teste de Aceitação* | Resultado Esperado: João consegue definir e ponderar variáveis operacionais no sistema, que utiliza essas informações para calcular e sugerir rotas otimizadas. Resultado Indesejado: O sistema não aceita ou não aplica corretamente os parâmetros dinâmicos fornecidos por João, resultando em sugestões de rotas não otimizadas.|

### User Story 8

| Campo | Descrição |
|-------|-----------|
| *Número* | 008 |
| *História* | Como João Santos, preciso que os resultados dos algoritmos de otimização de rotas incluam métricas detalhadas como o tempo de execução do algoritmo, o trajeto específico, o tempo de permanência previsto em cada residência, e o tempo total estimado para o leiturista completar a rota. Isso é crucial para avaliar a eficiência operacional e alocar recursos de maneira efetiva.|
| *Critério de Avaliação* | O sistema deve calcular e apresentar um relatório detalhado após a execução de qualquer algoritmo de otimização. Este relatório deve incluir o tempo que o sistema levou para executar o algoritmo, a sequência das residências na rota otimizada, o tempo estimado de permanência em cada ponto de leitura, e o tempo total de percurso para a rota completa.|
| *Teste de Aceitação* | Resultado Esperado: Após a execução da otimização, João recebe um relatório que detalha todas as métricas solicitadas e pode usar esses dados para ajustar operações e expectativas. Resultado Indesejado: O relatório está incompleto, omite métricas cruciais, ou apresenta dados de forma que não suporta decisões operacionais informadas.|

&nbsp;&nbsp;As user stories apresentadas para João Santos e Adenor Barbosa são fundamentais para entender como o sistema de otimização de rotas deve ser projetado e desenvolvido para atender às necessidades específicas do usuário. João, como gestor operacional, exige funcionalidades que lhe permitam não apenas monitorar e ajustar rotas em tempo real mas também testar e personalizar algoritmos de otimização conforme os desafios dinâmicos do dia a dia. As user stories de Adenor Barbosa refletem uma necessidade clara de gerenciar e otimizar rotas de leitura de forma eficiente, integrando facilmente os dados no sistema e permitindo análises rápidas e ajustes operacionais. Adenor, como um administrador ou coordenador de operações, depende de um sistema que não apenas processa dados de entrada, mas também facilita a visualização e a exportação dos resultados para uso prático.

## Jornada do Usuário

&emsp;&emsp;A jornada do usuário<sup>4</sup> é um mapeamento detalhado da experiência de uma pessoa ao interagir com um produto ou serviço, destacando os diversos pontos de contato e interações ao longo do caminho. Este conceito é vital no design e na melhoria de sistemas, pois permite aos criadores visualizar e entender as experiências, necessidades e desafios enfrentados pelos usuários. Ao examinar cada etapa da jornada, desde o primeiro contato até a conclusão de uma tarefa, é possível identificar oportunidades para aprimorar a funcionalidade, usabilidade e satisfação geral do usuário com o produto. Em suma, a jornada do usuário é a história completa da experiência do usuário, usada para criar soluções mais alinhadas com as expectativas e necessidades reais dos usuários.

&emsp;&emsp;Assim, nota-se a jornada dos usuários das personas envolvidas:

<div align="center">
  <p><b>Figura 3 </b>- Jornada do Usuário : Adenor Barbosa </p>
  <img src="..\assets\jornada-adenor.png">
  <p>Fonte: Elaboração G2</p>
</div>

<div align="center">
  <p><b>Figura 4 </b>- Jornada do Usuário : João Santos </p>
  <img src="..\assets\jornada-js-att.png">
  <p>Fonte: Elaboração G2</p>
</div>



&emsp;&emsp;A jornada dos usuários destaca a necessidade de uma interação simplificada e eficaz com o sistema de otimização de rotas. As etapas delineadas - desde o upload de dados até a exportação das rotas otimizadas - mostram um ciclo de uso que deve ser intuitivo e produtivo para se alinhar com as expectativas de Adenor e João. Refletindo sobre as oportunidades e responsabilidades identificadas, é evidente que os usuários têm papéis cruciais a desempenhar para garantir a eficiência operacional e a satisfação no uso da ferramenta. Implementações focadas em usabilidade, feedback claro e validação de dados podem significativamente melhorar a experiência de Adenor, tornando o sistema uma solução robusta e confiável para otimização de rotas.


### Referências
1. Rock Content. Personas: o que são, como criar e exemplos para usar. Disponível em: https://rockcontent.com/br/blog/personas/#:~:text=Persona%20%C3%A9%20um%20personagem%20fict%C3%ADcio,%2C%20problemas%2C%20desafios%20e%20objetivos.. Acesso em: 20 abr. 2024.
2. NORMAN, D. User Experience Design. Disponível em: https://www.basicbooks.com. Acesso em: 23 abr. 2024.
3. CursoSPM3. User Story. Disponível em: https://www.cursospm3.com.br/glossario/user-story/. Acesso em: 20 abr. 2024. 
4. MJV Innovation. Jornada do usuário: o que é? Disponível em: https://www.mjvinnovation.com/pt-br/blog/jornada-do-usuario-o-que-e/. Acesso em: 20 abr. 2024.

