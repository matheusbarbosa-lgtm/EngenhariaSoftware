import unittest

from triangulo import classificar_triangulo


class TestClassificacaoDeTriangulos(unittest.TestCase):
    def test_classificacoes(self):
        casos = [
            ((5, 5, 5), "equilatero"),
            ((5, 5, 3), "isosceles"),
            ((5, 3, 5), "isosceles"),
            ((3, 5, 5), "isosceles"),
            ((4, 5, 6), "escaleno"),
            ((6, 4, 5), "escaleno"),
        ]

        for lados, esperado in casos:
            with self.subTest(lados=lados):
                self.assertEqual(classificar_triangulo(*lados), esperado)

    def test_entradas_invalidas(self):
        casos = ((1, 2, 3), (0, 1, 1), (-1, 2, 2), (2, 2.5, 3))

        for lados in casos:
            with self.subTest(lados=lados):
                with self.assertRaises(ValueError):
                    classificar_triangulo(*lados)


if __name__ == "__main__":
    unittest.main()
