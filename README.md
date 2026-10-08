# EngenhariaSoftware

## Classificacao de triangulos

`triangulo.py` implementa `classificar_triangulo(a, b, c)`. A funcao
retorna `equilatero`, `isosceles` ou `escaleno` e rejeita lados que nao
formam um triangulo valido.

### Casos de teste

| Entradas `(a, b, c)` | Saida esperada | Objetivo |
| --- | --- | --- |
| `(5, 5, 5)` | `equilatero` | Tres lados iguais |
| `(5, 5, 3)` | `isosceles` | Primeiro par de lados iguais |
| `(5, 3, 5)` | `isosceles` | Segundo par de lados iguais |
| `(3, 5, 5)` | `isosceles` | Terceiro par de lados iguais |
| `(4, 5, 6)` | `escaleno` | Tres lados diferentes |
| `(6, 4, 5)` | `escaleno` | Ordem dos lados permutada |
| `(1, 2, 3)` | Erro | Soma de dois lados igual ao terceiro |
| `(0, 1, 1)` | Erro | Lado nulo |
| `(-1, 2, 2)` | Erro | Lado negativo |
| `(2, 2.5, 3)` | Erro | Valor nao inteiro |

Execute os testes com:

```bash
python3 -m unittest -v
```