# Referência Merge Sort: https://github.com/tryber/sd-021-b-live-lectures/pull/104/files#diff-32efdbb5e489278def2e2f091a67da0e920308253823c0197923c41e485d5915
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
    if not isinstance(first_string, str) or not isinstance(second_string, str):
        return False
    
    str1 = first_string.lower()
    str2 = second_string.lower()
    
    str1_sorted = merge_sort(str1)
    str2_sorted = merge_sort(str2)

    if str1_sorted != str2_sorted:
        return False
    return str2_sorted, str1_sorted, True