'''модуль отвечающий за валидацию данных'''

flower_db = {
    "rose": {"price": 5, "stock": 10},
    "tulip": {"price": 3, "stock": 15},
    "lily": {"price": 4, "stock": 5}
}


def get_flowers_price(flower_name, quantity):
    """
    Функция для получения стоимости заданного количества цветов.
    Выбрасывает исключения при:
    - отсутствии цветка,
    - недостатке цветов на складе,
    - некорректном формате параметров.
    """
    try:
        if not isinstance(flower_name, str) or not isinstance(quantity, int):
            raise TypeError(
                "Неверный тип данных: название должно быть строкой, количество - целым числом.")
        if flower_name not in flower_db:
            raise ValueError(
                f"Цветок '{flower_name}' отсутствует в базе данных.")

        flower_info = flower_db[flower_name]

        if quantity > flower_info["stock"]:
            raise ValueError(f"Недостаточно цветов '{flower_name}' на складе. Доступно только {flower_info['stock']} шт.")

        total_price = flower_info["price"] * quantity
        return total_price

    except TypeError as te:
        print(f"Ошибка типа данных: {te}")
        return None

    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
        return None

    finally:
        print("Завершение работы функции get_flower_price.")


def add_to_stock(flower_name, quantity):
    """
    Функция для добавления цветов на склад.
    Выбрасывает исключения при:
    - некорректном имени цветка,
    - отрицательном или нулевом количестве,
    - превышении максимального лимита.
    """
    MAX_STOCK = 50
    try:
        if not isinstance(flower_name, str) or not isinstance(quantity, int):
            raise TypeError("Неверный тип данных для добавления на склад.")

        if flower_name not in flower_db:
            raise ValueError(
                f"Цветок '{flower_name}' отсутствует в базе данных.")

        if quantity <= 0:
            raise ValueError("Количество должно быть больше нуля.")

        new_stock = flower_db[flower_name]["stock"] + quantity
        if new_stock > MAX_STOCK:
            raise OverflowError(
                f"Невозможно добавить: превышен лимит в {MAX_STOCK} шт.")

        flower_db[flower_name]["stock"] = new_stock
        print(f"На складе теперь {new_stock} шт. цветка '{flower_name}'.")

    except TypeError as te:
        print(f"Ошибка типа данных: {te}")

    except ValueError as ve:
        print(f"Ошибка значения: {ve}")

    except OverflowError as oe:
        print(f"Ошибка переполнения: {oe}")

    finally:
        print("Завершение работы функции add_to_stock.")


def calculate_order_cost(order):
    """
    Функция для расчета стоимости заказа.
    Выбрасывает исключения при:
    - некорректном формате заказа,
    - отсутствии цветов в заказе,
    - недостатке цветов для выполнения заказа.
    """
    try:
        if not isinstance(order, dict):
            raise TypeError("Заказ должен быть представлен в виде словаря.")

        total_cost = 0
        for flower_name, quantity in order.items():
            if flower_name not in flower_db:
                raise ValueError(
                    f"Цветок '{flower_name}' отсутствует в базе данных.")

            if quantity > flower_db[flower_name]["stock"]:
                raise ValueError(f"Недостаточно цветов '{flower_name}' на складе для выполнения заказа.")

            total_cost += flower_db[flower_name]["price"] * quantity
            flower_db[flower_name]["stock"] -= quantity

        return total_cost

    except TypeError as te:
        print(f"Ошибка типа данных: {te}")
        return None

    except ValueError as ve:
        print(f"Ошибка значения: {ve}")
        return None

    finally:
        print("Завершение работы функции calculate_order_cost.")
