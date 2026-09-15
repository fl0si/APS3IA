Integrantes: Lorenzo Gouveia Flosi

# Problema das N-Rainhas 

Implementação do problema das N-Rainhas para tabuleiros 4x4, 5x5, 6x6, 7x7 e 8x8, usando busca em largura 

## Como rodar

```bash# Problema das N-Rainhas (BFS com aigyminsper)

## Como rodar

```bash
pip install requirements.txt
python n_rainhas.py
```

## Como o código funciona

- **Estado (`NRainhas`)**: cada estado guarda uma lista `tabuleiro`, onde o índice é a linha e o valor é a coluna da rainha naquela linha. Ex.: `[1, 3, 0, 2]` = rainha na linha 0/coluna 1, linha 1/coluna 3, etc.
- **`successors()`**: a partir de um estado com `k` rainhas posicionadas, gera um sucessor para cada coluna da linha `k` em que a rainha não seja atacada pelas rainhas já colocadas (mesma coluna ou mesma diagonal). Isso evita gerar estados inválidos.
- **`is_goal()`**: o estado é solução quando o tabuleiro tem `N` rainhas.
- A busca é feita com `BuscaLargura().search(estado_inicial)` da `aigyminsper`.

## Resultados

| N | Solução (coluna por linha) | Tempo (s) |
|---|---|---|
| 4 | [1, 3, 0, 2] | 0,0002 |
| 5 | [0, 2, 4, 1, 3] | 0,0004 |
| 6 | [1, 3, 5, 0, 2, 4] | 0,0011 |
| 7 | [0, 2, 4, 6, 1, 3, 5] | 0,0041 |
| 8 | [0, 4, 7, 5, 2, 6, 1, 3] | 0,0165 |

### Tabuleiros

**N = 4**
```
. Q . .
. . . Q
Q . . .
. . Q .
```

**N = 5**
```
Q . . . .
. . Q . .
. . . . Q
. Q . . .
. . . Q .
```

**N = 6**
```
. Q . . . .
. . . Q . .
. . . . . Q
Q . . . . .
. . Q . . .
. . . . Q .
```

**N = 7**
```
Q . . . . . .
. . Q . . . .
. . . . Q . .
. . . . . . Q
. Q . . . . .
. . . Q . . .
. . . . . Q .
```

**N = 8**
```
Q . . . . . . .
. . . . Q . . .
. . . . . . . Q
. . . . . Q . .
. . Q . . . . .
. . . . . . Q .
. Q . . . . . .
. . . Q . . . .
```

O tempo de execução cresce conforme N aumenta, já que o número de tabuleiros parciais válidos que o BFS mantém em memória cresce combinatoriamente com o tamanho do tabuleiro. Ainda assim, para N de 4 a 8 o algoritmo encontra a solução em poucos milissegundos.

