def find_duplicate(nums):
    if len(nums) < 2:
        return False
    # numberDuplicate = []
    numberDuplicate = set()
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if number in numberDuplicate:
            return number
        # numberDuplicate.append(number)
        numberDuplicate.add(number)
    return False
