import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    """Фикстура: создаёт объект Calculator перед каждым тестом."""
    return Calculator()


# ============================================================
# add
# ============================================================

@pytest.mark.parametrize('a, b, expected', [
    (2, 3, 5),
    (0, 0, 0),
    (-5, 5, 0),
    (-3, -7, -10),
    (1.5, 2.5, 4.0),
    (1000000, 2000000, 3000000),
])
def test_add(calc, a, b, expected):
    """Сложение: параметризованный тест с разными наборами данных."""
    assert calc.add(a, b) == expected


# ============================================================
# subtract
# ============================================================

@pytest.mark.parametrize('a, b, expected', [
    (10, 3, 7),
    (0, 5, -5),
    (5, 5, 0),
    (-5, -5, 0),
    (2.5, 1.5, 1.0),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


# ============================================================
# multiply
# ============================================================

@pytest.mark.parametrize('a, b, expected', [
    (3, 4, 12),
    (0, 100, 0),
    (-2, 5, -10),
    (-3, -3, 9),
    (1.5, 2, 3.0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ============================================================
# divide
# ============================================================

@pytest.mark.parametrize('a, b, expected', [
    (10, 2, 5),
    (9, 3, 3),
    (1, 4, 0.25),
    (0, 5, 0),
    (-10, 2, -5),
])
def test_divide_valid(calc, a, b, expected):
    """Деление с валидными данными."""
    assert calc.divide(a, b) == expected


def test_divide_by_zero_raises(calc):
    """Деление на ноль → ValueError."""
    with pytest.raises(ValueError, match='Деление на ноль'):
        calc.divide(10, 0)


def test_divide_by_zero_raises_zero(calc):
    """Деление нуля на ноль тоже → ValueError."""
    with pytest.raises(ValueError):
        calc.divide(0, 0)


# ============================================================
# is_prime_number
# ============================================================

@pytest.mark.parametrize('n, expected', [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (13, True),
    (17, True),
    (4, False),
    (6, False),
    (9, False),
    (15, False),
    (1, False),
    (0, False),
    (-5, False),
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected


def test_is_prime_number_with_string_raises(calc):
    """Передача строки вместо числа → TypeError."""
    with pytest.raises(TypeError):
        calc.is_prime_number('abc')


def test_is_prime_number_with_float_raises(calc):
    """Передача float вместо int → TypeError."""
    with pytest.raises(TypeError):
        calc.is_prime_number(2.5)


# ============================================================
# is_even
# ============================================================

@pytest.mark.parametrize('n, expected', [
    (2, True),
    (4, True),
    (0, True),
    (-2, True),
    (1, False),
    (3, False),
    (-3, False),
    (101, False),
])
def test_is_even(calc, n, expected):
    assert calc.is_even(n) == expected


def test_is_even_with_string_raises(calc):
    with pytest.raises(TypeError):
        calc.is_even('abc')