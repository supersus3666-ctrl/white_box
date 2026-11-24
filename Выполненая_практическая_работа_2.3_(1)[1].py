# Практическая работа № 2.3. Задание 1.
# Определение вида треугольника по сторонам и его площади (с контролем ввода).
import math


def parse_number(text):
    """Преобразует строку в число; при некорректном вводе бросает ValueError."""
    text = text.strip().replace(",", ".")
    if not text:
        raise ValueError("пустой ввод, нужно ввести число")
    try:
        value = float(text)
    except ValueError:
        raise ValueError(f"«{text}» не является числом")
    if not math.isfinite(value):
        raise ValueError(f"«{text}» — недопустимое значение (бесконечность или NaN)")
    return value


def check_sides(a, b, c):
    """Возвращает None, если a, b, c могут быть сторонами треугольника,
    иначе — текст ошибки."""
    if a <= 0 or b <= 0 or c <= 0:
        return "стороны должны быть положительными числами (больше 0)"
    if a + b <= c or a + c <= b or b + c <= a:
        return "сумма любых двух сторон должна быть больше третьей"
    return None


def triangle_area(a, b, c):
    """Площадь по формуле Герона."""
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def type_by_sides(a, b, c):
    ab = math.isclose(a, b)
    ac = math.isclose(a, c)
    bc = math.isclose(b, c)
    if ab and bc:
        return "Равносторонний"
    if ab or ac or bc:
        return "Равнобедренный"
    return "Разносторонний"


def process(sa, sb, sc):
    """Полная обработка трёх введённых строк.
    Возвращает (вид, площадь) или бросает ValueError с понятным сообщением."""
    a, b, c = parse_number(sa), parse_number(sb), parse_number(sc)
    error = check_sides(a, b, c)
    if error:
        raise ValueError(error)
    return type_by_sides(a, b, c), triangle_area(a, b, c)


def main():
    print("Определение вида треугольника по сторонам (для выхода введите q)")
    while True:
        raw = []
        for name in "abc":
            value = input(f"Сторона {name}: ")
            if value.strip().lower() == "q":
                return
            raw.append(value)
        try:
            kind, area = process(*raw)
        except ValueError as err:
            print(f"Ошибка: {err}. Повторите ввод.\n")
            continue
        print(f"Вид треугольника: {kind}")
        print(f"Площадь: {area:.4f}\n")


if __name__ == "__main__":
    main()
