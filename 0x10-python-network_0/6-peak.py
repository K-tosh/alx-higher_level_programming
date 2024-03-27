def find_peak(list_of_integers):
    """
    Finds a peak in a list of integers.

    This function takes a list of integers as input and returns a peak element
    in the list, or None if the input list is empty or invalid.

    Args:
        list_of_integers (list): A list of integers.

    Returns:
        int or None: A peak element in the input list, or None if the input list
        is empty or invalid.

    Raises:
        TypeError: If the input list does not contain only integers.
        ValueError: If the input list has less than two elements.
    """

    if not isinstance(list_of_integers, list):
        raise TypeError("Input list must be a list of integers.")

    if len(list_of_integers) < 2:
        raise ValueError("Input list must have at least two elements.")

    if list_of_integers is None or list_of_integers == []:
        return None

    lo = 0
    hi = len(list_of_integers)
    mid = ((hi - lo) // 2) + lo
    mid = int(mid)

    if hi == 1:
        return list_of_integers[0]

    if hi == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    