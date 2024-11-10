"""Задание 6,7"""


class FlowerNotFoundError(Exception):
    """Исключение для ошибки при отсутствии цветка в базе данных."""
    pass


class InsufficientStockError(Exception):
    """Исключение для ошибки при недостаточном количестве цветов на складе."""
    pass


class InvalidOrderQuantityError(Exception):
    """Исключение для ошибки при неверном количестве заказа (ноль или отрицательное значение)."""
    pass


# Имитация базы данных с цветами
flower_db = {
    "rose": {"price": 5, "stock": 10},
    "tulip": {"price": 3, "stock": 15},
    "lily": {"price": 4, "stock": 5}
}


def plc_order(flower_name, quantity):
    """
    Функция для размещения заказа на цветы.
    Генерирует пользовательские исключения при:
    - Отсутствии цветка в базе данных,
    - Недостаточном количестве цветов на складе,
    - Неверном количестве для заказа.
    """
    try:
        # Проверка количества на корректность
        if quantity <= 0:
            raise InvalidOrderQuantityError(
                "Количество должно быть положительным числом.")

        # Проверка наличия цветка в базе данных
        if flower_name not in flower_db:
            raise FlowerNotFoundError(
                f"Цветок '{flower_name}' не найден в базе данных.")

        flower_info = flower_db[flower_name]

        # Проверка достаточности количества на складе
        if quantity > flower_info["stock"]:
            raise InsufficientStockError(f"Недостаточно цветов '{flower_name}' на складе. В наличии только {flower_info['stock']} шт.")

        # Списание цветов со склада и расчет стоимости
        flower_db[flower_name]["stock"] -= quantity
        total_price = flower_info["price"] * quantity
        print(f"Заказ на {quantity} шт. '{flower_name}' успешно оформлен. Общая стоимость: {total_price}.")

    except FlowerNotFoundError as fnfe:
        print(f"Ошибка: {fnfe}")

    except InsufficientStockError as ise:
        print(f"Ошибка: {ise}")

    except InvalidOrderQuantityError as ioqe:
        print(f"Ошибка: {ioqe}")
    except Exception as ex:
        print(f"Ошибка: {ex}")
    finally:
        print("Завершение работы функции place_order.")
