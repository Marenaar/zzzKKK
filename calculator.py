
class Calculator:

    def scitani(self, a: int, b: int) -> int:
        """
        Sečte zadané hodnoty "a" a "b"
        :param int a: Zadané číslo "a"
        :param int b: Zadané číslo "b"
        :return: int Vrátí součet "a" a "b"
        """
        return a + b

    def odcitani(self, a: int, b: int) -> int:
        """
        Odečte od čísla "a" číslo "b"
        :param int a: Zadané číslo "a"
        :param int b: Zadané číslo "b"
        :return: int Vrátí rozdíl čísel "a" a "b"
        """
        return a - b

    def nasobeni(self, a: int, b: int) -> int:
        """
        Vynásobí zadané hodnoty "a" a "b"
        :param int a: Zadané číslo "a"
        :param int b: Zadané číslo "b"
        :return: int
        """
        return a * b

    def deleni(self, a, b):
        """
        Vydělí
        :param a: Zadané číslo "a"
        :param b: Zadané číslo "b"
        :return: int Vrátí podíl čísel "a" a "b"
        """
        if b == 0:
            return f"!{b}! není vhodným dělitelem: NELZE DĚLIT NULOU!"
        else:
            return a / b

