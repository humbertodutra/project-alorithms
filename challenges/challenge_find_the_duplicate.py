def is_input_none(nums):
    return nums is None


def is_input_list(nums):
    return isinstance(nums, list)


def has_sufficient_elements(nums):
    return len(nums) > 1


def is_input_positive_integer(num):
    return isinstance(num, int) and num >= 0


def is_valid_input(nums):
    if is_input_none(nums) or not is_input_list(nums):
        return False
    if not has_sufficient_elements(nums):
        return False
    for num in nums:
        if not is_input_positive_integer(num):
            return False
    return True


def find_duplicate(nums):
    """Faça o código aqui."""
    if not is_valid_input(nums):
        return False
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return False
