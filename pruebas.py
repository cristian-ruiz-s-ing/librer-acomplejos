import unittest
import libreriacomplejos


class OpComplejosTestCase(unittest.TestCase):

    def test_suma(self):
        result=libreriacomplejos.suma((5,1),(4,3))
        self.assertEqual(result,'9+4i')

    def test_resta(self):
        result=libreriacomplejos.resta((5,1),(4,3))
        self.assertEqual(result,'1-2i')

    def test_multiplica(self):
        result=libreriacomplejos.mult((5,1),(4,3))
        self.assertEqual(result,'17+19i')

    def test_division(self):
        result=libreriacomplejos.div((5,1),(4,3))
        self.assertEqual(result,'23-11i/25')

    def test_modulo(self):
        result=libreriacomplejos.modulo((5,1))
        self.assertEqual(result,5.099)

    def test_conjugado(self):
        result=libreriacomplejos.conj((5,1))
        self.assertEqual(result,'5-1i')

    def test_polar(self):
        result=libreriacomplejos.polar((5,1))
        self.assertEqual(result,(5.099,0.197))

    def test_cartesiano(self):
        result=libreriacomplejos.cart((5,1))
        self.assertEqual(result,'2.702+4.207i')


if __name__ == "__main__":
    unittest.main()
