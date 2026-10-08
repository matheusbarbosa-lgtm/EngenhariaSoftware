"""Classificacao de triangulos."""


def classificar_triangulo(lado_a: int, lado_b: int, lado_c: int) -> str:
    """Retorna a classificacao do triangulo ou rejeita lados invalidos."""
    if not all(isinstance(lado, int) for lado in (lado_a, lado_b, lado_c)):
        raise ValueError("Os lados devem ser inteiros.")

    if lado_a <= 0 or lado_b <= 0 or lado_c <= 0:
        raise ValueError("Os lados devem ser positivos.")

    if (lado_a + lado_b <= lado_c or
            lado_a + lado_c <= lado_b or
            lado_b + lado_c <= lado_a):
        raise ValueError("Os lados nao formam um triangulo.")

    if lado_a == lado_b == lado_c:
        return "equilatero"
    if lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
        return "isosceles"
    return "escaleno"
