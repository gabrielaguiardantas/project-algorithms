def find_duplicate(nums):
    """Faça o código aqui."""
    if not validate_nums(nums):
        return False
    nums.sort()
    i = 0
    for number in nums[:-1]:
        if number == nums[i + 1]:
            return number
        i += 1
    return False


def validate_nums(nums):
    if len(nums) <= 1:
        return False
    for number in nums:
        if type(number) != int:
            return False
        if number < 0:
            return False
    return True
