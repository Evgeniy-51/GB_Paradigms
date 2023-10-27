def bin_search(lst: list, res: float) -> int:
    start_index = 0
    end_index = len(lst) - 1
    while start_index <= end_index:
        current = start_index + (end_index - start_index) // 2
        if lst[current] == res:
            return current
        elif lst[current] > res:
            end_index = current - 1
        else:
            start_index = current + 1

    return -1


if __name__ == '__main__':
    my_list = [1, 4, 6, 8, 9, 11, 14, 22, 34, 56]
    res = 11
    print(bin_search(my_list, res))
