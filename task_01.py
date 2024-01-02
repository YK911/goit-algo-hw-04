import timeit
import random
import string


def generate_random_word(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))


def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи,
    # додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


range_of_data = 1000  # Сhange this variable to get different input range of data

arr_to_sort = [random.randint(1, range_of_data) for _ in range(range_of_data)]
random_words = [
    generate_random_word(random.randint(3, 10)) for _ in range(range_of_data)
]

print("Calculating in progress...")

# Numbers sorting
insertion_sort_nums = timeit.timeit(
    "insertion_sort(arr_to_sort.copy())", globals=globals(), number=100
)
merge_sort_nums = timeit.timeit(
    "merge_sort(arr_to_sort.copy())", globals=globals(), number=100
)
timsort_1_nums = timeit.timeit(
    "sorted(arr_to_sort.copy())", globals=globals(), number=100
)
timsort_2_nums = timeit.timeit(
    "arr_to_sort.copy().sort()", globals=globals(), number=100
)

# Words sorting
insertion_sort_words = timeit.timeit(
    "insertion_sort(random_words.copy())", globals=globals(), number=100
)
merge_sort_words = timeit.timeit(
    "merge_sort(random_words.copy())", globals=globals(), number=100
)
timsort_1_words = timeit.timeit(
    "sorted(random_words.copy())", globals=globals(), number=100
)
timsort_2_words = timeit.timeit(
    "random_words.copy().sort()", globals=globals(), number=100
)

print("\n" + "=" * 29 + "\n" + "|  Numbers sorting results  |" + "\n" + "=" * 29)
print(
    "{:<24}".format("Insertion sort time:"),
    f"{insertion_sort_nums:.6f} sec",
)
print("{:<24}".format("Merge sort time:"), f"{merge_sort_nums:.6f} sec")
print("{:<24}".format("Timsort-1 time:"), f"{timsort_1_nums:.6f} sec")
print("{:<24}".format("Timsort-2 time:"), f"{timsort_2_nums:.6f} sec")

print("\n" + "=" * 29 + "\n" + "|   Words sorting results   |" + "\n" + "=" * 29)
print(
    "{:<24}".format("Insertion sort time:"),
    f"{insertion_sort_words:.6f} sec",
)
print("{:<24}".format("Merge sort time:"), f"{merge_sort_words:.6f} sec")
print("{:<24}".format("Timsort-1 time:"), f"{timsort_1_words:.6f} sec")
print("{:<24}".format("Timsort-2 time:"), f"{timsort_2_words:.6f} sec")
