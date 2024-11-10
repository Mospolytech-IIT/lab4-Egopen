""""Задание 5"""

flower_db = {
    "rose": {"price": 5, "stock": 10},
    "tulip": {"price": 3, "stock": 15},
    "lily": {"price": 4, "stock": 5}
}


def place_order(flower_name, quantity):
    """
    Функция для размещения заказа на цветы.
    Генерирует исключения при:
    - Неверных типах параметров,
    - Отсутствии цветка в базе данных,
    - Недостатке цветов для выполнения заказа.
    """
    try:
        # Проверка типов параметров
        if not isinstance(flower_name, str):
            raise TypeError("Имя цветка должно быть строкой.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError(
                "Количество должно быть положительным целым числом.")

        # Проверка наличия цветка в базе данных
        if flower_name not in flower_db:
            raise KeyError(
                f"Цветок '{flower_name}' отсутствует в базе данных.")

        flower_info = flower_db[flower_name]

        # Проверка достаточности количества на складе
        if quantity > flower_info["stock"]:
            raise ValueError(f"Недостаточно цветов '{flower_name}' на складе. В наличии только {flower_info['stock']} шт.")

        # Списание цветов со склада и расчет стоимости
        flower_db[flower_name]["stock"] -= quantity
        total_price = flower_info["price"] * quantity
        print(f"Заказ на {quantity} шт. '{flower_name}' успешно оформлен. Общая стоимость: {total_price}.")

    except TypeError as te:
        print(f"Ошибка типа данных: {te}")

    except ValueError as ve:
        print(f"Ошибка значения: {ve}")

    except KeyError as ke:
        print(f"Ошибка ключа: {ke}")

    finally:
        # Гарантируем завершение работы функции
        print("Завершение работы функции place_order.")
