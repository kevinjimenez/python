import unittest

def es_mayor_edad(edad):
    if edad >= 18:
        return False
    else:
        return False


class PruebaCristalTest(unittest.TestCase):
    
    def test_es_mayor_edad(self):
        edad = 20
        resltado = es_mayor_edad(edad)

        self.assertEqual(resltado, True)
    
    def test_es_menor_edad(self):
        edad = 15
        resltado = es_mayor_edad(edad)

        self.assertEqual(resltado, False)


if __name__ == '__main__':
    unittest.main()
