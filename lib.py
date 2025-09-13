def count_common_elements(*lists):
    """
    Функция принимает произвольное количество списков
    и возвращает количество элементов, которые встречаются во всех списках.

    Args:
        *lists: произвольное количество списков

    Returns:
        int: количество общих элементов
    """
    if not lists:
        return 0

    # Находим пересечение всех множеств
    common_elements = set(lists[0])
    for lst in lists[1:]:
        common_elements = common_elements.intersection(set(lst))

    return len(common_elements)


# Пример использования
if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    list3 = [5, 6, 7, 8, 9]

    result = count_common_elements(list1, list2, list3)
    print(f"Количество общих элементов: {result}")