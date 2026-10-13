class Calculator:
    """Простой калькулятор с бизнес-логикой для unit-тестирования."""

    def add(self, a, b):
        """Сложение двух чисел."""
        return a + b

    def subtract(self, a, b):
        """Вычитание: a - b."""
        return a - b

    def multiply(self, a, b):
        """Умножение двух чисел."""
        return a * b

    def divide(self, a, b):
        """Деление: a / b. Бросает ValueError при делении на ноль."""
        if b == 0:
            raise ValueError('Деление на ноль невозможно')
        return a / b

    def is_prime_number(self, n):
        """Проверяет, является ли число простым."""
        if not isinstance(n, int):
            raise TypeError('Число должно быть целым')
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_even(self, n):
        """Проверяет, является ли число чётным."""
        if not isinstance(n, int):
            raise TypeError('Число должно быть целым')
        return n % 2 == 0