"""
В модуле processing напишите функцию filter_by_state,
которая принимает список словарей и опционально значение для ключа
state (по умолчанию 'EXECUTED'). Функция возвращает новый список словарей,
содержащий только те словари, у которых ключ
state соответствует указанному значению.
"""

"""
В том же модуле напишите функцию sort_by_date,
которая принимает список словарей и необязательный параметр,
задающий порядок сортировки (по умолчанию — убывание).
Функция должна возвращать новый список, отсортированный по дате (date).
"""
import ast

"Сортируем данные по state"


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    filtered_list = [item for item in data if item.get("state") == state]
    return filtered_list


"Сортируем данные по data"


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)


if __name__ == "__main__":
    # Запрашиваем данные
    print("Введите список")
    user_input = input()

    try:
        # Выводим данные
        data = ast.literal_eval(user_input)

        executed_data = filter_by_state(data)
        canceled_data = filter_by_state(data, "CANCELED")
        sorted_data = sort_by_date(data)

        print(f"EXECUTED:\n{executed_data}")
        print(f"\nCANCELED:\n{canceled_data}")
        print(f"\nОтсортировано по дате (от новых):\n{sorted_data}")

    except Exception as e:
        print(f"\nОшибка: {e}")
