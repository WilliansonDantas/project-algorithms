# Referência Merge Sort:
# https://github.com/tryber/sd-021-b-live-lectures/pull/104/
# Bloco de código visto na aula do dia 4.3, conforme referência acima.
def merge_sort(input_list: list):
    if len(input_list) <= 1:
        return input_list

    mid = len(input_list) // 2

    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])

    return merge(left, right)


def merge(left: list, right: list):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left == []:
        result += right
    else:
        result += left
    return result


# Bloco de código visto na aula do dia 4.3, conforme referência acima.


def is_anagram(first_string, second_string):
    if len(first_string) == 0 or len(second_string) == 0:
        return first_string, second_string, False

    str1 = first_string.lower()
    str2 = second_string.lower()

    str1_sorted = merge_sort(list(str1))
    str2_sorted = merge_sort(list(str2))

    str1Join = "".join(str1_sorted)
    str2Join = "".join(str2_sorted)

    if str1Join != str2Join:
        return str1Join, str2Join, False
    return str1Join, str2Join, True
