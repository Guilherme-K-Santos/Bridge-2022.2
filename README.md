# Bridge-Desafio
Código-fonte da segunda etapa do processo seletivo do Bridge.

Olá, chamo-me Guilherme Santos e atualmente estou no terceiro semestre de SIN.
Nesse arquivo vou explicar e analisar um pouco sobre o meu código para o desafio.

Para começo, vou explicar um pouco sobre o código. Eu implementei o desafio usando
totalmente Python, como disse na fase 1, eu ainda não estudei sobre react, js, css e MySql
explicitamente. Portanto, eu usei tecnologias e bibliotecas em python para "imitar"/fazer a
mesma função tanto no frontend com o backend. Espero que gostem :D

Para realizar o frontend, eu usei a biblioteca "PySimpleGUI", que cria interfaces gráficas
costumizáveis. No sistema existem 3 telas principais: a tela inicial (pode levar o usuário
para a tela de cálculo ou para a screen de histórico), a tela cálculo (onde o algoritmo
realiza o desafio em si) e a tela de histórico (armazena os números calculados e seus respec
tivos resultados). 

Já no backend, utilizei a biblioteca "pickle", que se comporta como um banco de dados bem
básico. Eu usei dois DAO (Data Access Object): um abstrato (falando as funções gerais do
banco de dados improvisado) e o focado em guardar/armazenar os números e resultados.
Para armazená-los eu usei dicionários, onde a chve é o próprio número, e o "objeto" guardado
é o resultado. O processamento do algoritmo se dá no controlador sistema, que conversa com o
banco de dados e com as telas, ou seja, não há conexão direta entre os dois. Todos os cálculos
são efetuados no backend.

Nesse parágrafo vou explicar um pouco da minha ideia de como implementar o algoritmo.
Primeiramente, o usuário coloca o número que deseja calcular na "tela cálculo", ela manda
para a função "calculo" do controlador sistema. O número em questão entra em um ciclo com
regra "> 1" (dado no pdf). A primeira linha de código é "divisor = 2", fiz isso para não 
desperdiçar poder computacional calculando sempre divisões por 1 (sempre serão divisores).
Além disso, inclui no algoritmo "num_divisores_n = 2" em várias partes, porque, tirando divisões por
1, todos os números são divididos por eles mesmos, os famosos primos.
A partir de tudo isso, usei os "critérios de divisibilidade" para ganhar tempo nos cálculos,
não tenho certeza se devo explicar isso aqui, mas, em resumo, a regra utilizada foi:

Números que são divisiveis por 2, sempre terão como último divisor (tirando a si próprio) a
sua exata metade (ex: o último divisor de 40 inteiro, tirando 40, é o 20).

Números que são divisiveis por 3, sempre terão como último divisor (tirando a si próprio) o
seu exato terço (ex: o último divisor de 999 inteiro, tirando 999, é o 333).

Números que são divisiveis por 5, sempre terão como último divisor (tirando a si próprio) o
seu exato quinto (ex: o último divisor de 25 inteiro, tirando 25, é o 5).

Números que são divisiveis por 7, sempre terão como último divisor (tirando a si próprio) o
seu exato sétimo (ex: o último divisor de 49 inteiro, tirando 49, é o 7).

Para os números restantes, segue as regras: 

- 4, 6 e 8 são divisiveis por 2.
- 9 é divisivel por 3.

- Qualquer outro número que não é dividido por esses algarismos primários (exceção do 1), são
  números primos. Portatno só têm dois divisores distintos: 1 e ele mesmo.

Após terminar o cálculo de cada número, eu comparo o resultado anterior ao atual, com as váriaveis
"num_divisores_n1 == num_divisores_n". Caso eles sejam iguais, o "resultado_final" é acrescido em 1.

OBS: na primeira tentativa "num_divisores_n1" é igual a -math.inf, pois ainda não foi calculado
mais de dois números para a comparação.

Quando o algoritmo finalmente acaba, a contagem de tempo para e as váriaveis número, resultado e
tempo são enviadas para as telas e "printadas" para o usuário através de uma interface gráfica
customizavel.

Para fazer o programa funcionar, basta dar run no arquivo "main.py". Isso inicializará o sis-
tema.

Link da Pipeline no Heroku:
https://dashboard.heroku.com/pipelines/b4d39764-a2e1-4ed1-8365-c61bebc92081
