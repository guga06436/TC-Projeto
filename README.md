# TC-Projeto
Simulação de um Autômato Finito Não-determinístico desenvolvido para a disciplina Teoria da Computação no período 2021.1.

## Objetivo

Desenvolver um programa para simular o processamento de Autômatos Finitos Não-determinísticos (AFNs). O programa deve receber como entrada um arquivo contendo o seguinte formato:

```
alfabeto=a, b, c, d # Lista de símbolos do alfabeto aceita pelo autômato
estados=q0,q1,q1 # Lista de estados no autômato
inicial=q0 # Indica qual é o estado inicial
finais=q1, q2 # Especifica os estados finais do autômato
transicoes
q0,q1,a # Representa uma transição de q0 para q1 com o símbolo "a"
q1,q2,epsilon # Transição de cadeia vazia de q1 para q2
...
```

Alguns exemplos de arquivos seguindo o formato especificado estão disponíveis na pasta teste. Além disso, é importante ressaltar que o simulador leva em consideração casos em que não há estados finais.

## Execução

Na função main será requisitado o nome do arquivo do autômato. Caso o arquivo exista, o programa utiliza a função `read_afn(arq)`, a qual verifica se ele segue o formato proposto acima e retorna um dicionário com as suas características. Após essa etapa, o usuário informa a cadeia que ele almeja utilizar na simulação. Caso a cadeia seja válida ele chama a função `processa_cadeia(afn, cadeia, estado_atual, resultado='')`, essa função realiza o processamento da cadeia de forma recursiva e, ao final, imprime todas as possibilidades.
