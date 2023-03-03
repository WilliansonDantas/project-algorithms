# Outra forma de fazer utilizando o método selection_sort
# Referência Selection Sort:
# https://github.com/tryber/sd-021-b-live-lectures/pull/104/
# Bloco de código visto na aula do dia 4.3, conforme referência acima.
# def selection_sort(input_list: list):
#     for i in range(len(input_list)):
#         min_i = i
#         for j in range(i + 1, len(input_list)):
#             if input_list[j] < input_list[min_i]:
#                 min_i = j
#         input_list[min_i], input_list[i] = input_list[i], input_list[min_i]
#     return input_list
# Bloco de código visto na aula do dia 4.3, conforme referência acima.

# Outra forma de fazer utilizando o método selection_sort
# numberSorted = selection_sort(nums)
# for index in range(len(numberSorted)-1):
#     if numberSorted[index] == numberSorted[index + 1]:
#         return numberSorted[index]
# return False


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    numberDuplicate = []
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if number in numberDuplicate:
            return number
        numberDuplicate.append(number)
    return False
