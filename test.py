from lib import count_common_elements

print("Тестирование count_common_elements:")
print("-" * 30)

# Тест 1
test1 = count_common_elements([1,2,3], [2,3,4], [3,4,5])
print(f"Тест 1: {test1} (ожидается 1)")

# Тест 2
test2 = count_common_elements([1,2], [2,3], [3,4])
print(f"Тест 2: {test2} (ожидается 0)")

# Тест 3
test3 = count_common_elements([1,2,3])
print(f"Тест 3: {test3} (ожидается 3)")

# Тест 4
test4 = count_common_elements()
print(f"Тест 4: {test4} (ожидается 0)")

print("-" * 30)
print("Тестирование завершено!")