'''задание 3'''

flower_db = {
    "rose": {"price": 5, "stock": 10},
    "tulip": {"price": 3, "stock": 15},
    "lily": {"price": 4, "stock": 5}
}


def get_flower_price(flower_name, quantity):
    """
    Функция для получения стоимости заданного количества цветов.
    При недостаточном количестве или отсутствии цветка выбрасывается исключение.
    """
    try:
        # Проверка наличия цветка в базе данных
        if flower_name not in flower_db:
            raise ValueError(f"Цветок '{flower_name}' отсутствует в базе.")

        flower_info = flower_db[flower_name]

        # Проверка достаточности количества на складе
        if quantity > flower_info["stock"]:
            raise ValueError(f"Недостаточно цветов '{flower_name}' на складе. В наличии: {flower_info['stock']} шт.")

        # Подсчет стоимости
        total_price = flower_info["price"] * quantity
        return total_price

    except Exception as e:
        # Логика обработки исключения
        print(f"Ошибка: {e}. Проверьте правильность данных.")
        # Возвращаем None как индикацию ошибки
        return None

    finally:
        # Логика завершения функции
        print("Завершение работы функции get_flower_price.")
        # Гарантируем, что функция завершится корректно
