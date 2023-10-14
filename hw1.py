def sort_list_imperative(numbers):
    for k in range(len(numbers) - 1):
        for i in range(len(numbers) - 1 - k):
            if numbers[i] < numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    return numbers


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)


if __name__ == '__main__':
    numbers = [34, 4, 9, 65, 71, 12, 65, 17, 65, 22, 0, 3, 56, 44]
    sort_list_imperative(numbers)
    print(numbers)

    numbers = [34, 4, 9, 65, 71, 12, 65, 17, 65, 22, 0, 3, 56, 44]
    sort_list_declarative(numbers)
    print(numbers)
