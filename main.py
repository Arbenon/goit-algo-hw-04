import timeit
import random

# Cортування злиттям:
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Cортування вставками:
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання
def measure_time(sort_func, data):
    timer = timeit.Timer(lambda: sort_func(data.copy()))
    return timer.timeit(number=1)

# Генерація випадкових даних для тестування
sizes = [100, 1000, 10000, 100000]
results = {'merge_sort': [], 'insertion_sort': [], 'timsort': []}

for size in sizes:
    data = [random.randint(0, 10000000) for i in range(size)]

    merge_time = measure_time(merge_sort, data)
    insertion_time = measure_time(insertion_sort, data)
    timsort_time = measure_time(sorted, data)

    results['merge_sort'].append(merge_time)
    results['insertion_sort'].append(insertion_time)
    results['timsort'].append(timsort_time)

# Виведення результатів
for size, merge_time, insertion_time, timsort_time in zip(sizes, results['merge_sort'], results['insertion_sort'], results['timsort']):
    print(f"Size: {size}")
    print(f"Merge Sort: {merge_time:.6f} seconds")
    print(f"Insertion Sort: {insertion_time:.6f} seconds")
    print(f"Timsort (Python's sorted): {timsort_time:.6f} seconds")
    print()

# Висновки:
# 1. Сортування Merge має складність O(n log n) і працює ефективно на великих наборах даних.
# 2. Сортування Insertion має складність O(n^2) і є неефективним на великих наборах даних.
# 3. Timsort поєднує сортування злиттям і сортування вставками, тому є швидким та ефективним для різних наборів даних.
