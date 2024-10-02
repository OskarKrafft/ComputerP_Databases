def min_all(L, C):
    """
    Finds the minimum number of consecutive elements needed to take from the list `L` 
    such that at least one of each number in the range `[0, C-1]` is included.

    Args:
    L (list of int): A list of non-negative integers in the range `[0, C-1]`.
    C (int): The number of unique integers to cover (from 0 to C-1).

    Returns:
    int: The minimum length of the consecutive subarray that contains at least one of each number in the range `[0, C-1]`.
    """
    left_pointer = 0
    min_length = len(L)
    count = [0] * C
    unique_count = 0 

    for right_pointer in range(len(L)):
        count[L[right_pointer]] += 1
        if count[L[right_pointer]] == 1:
            unique_count += 1

        while unique_count == C:
            min_length = min(min_length, right_pointer - left_pointer + 1)
            count[L[left_pointer]] -= 1
            if count[L[left_pointer]] == 0:
                unique_count -= 1
            left_pointer += 1

    return min_length

def strings_from_number(n: int) -> list[str]:
    """
    Generates all possible strings from the digits of the given number `n`, 
    where each digit corresponds to specific letters on a phone keypad.

    Args:
    n (int): A number, where digits map to letters like on a phone keypad (2 -> 'abc', 3 -> 'def', etc.).

    Returns:
    list of str: All possible letter combinations that correspond to the number `n`.
    """
    digit_to_letters = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    n_str = str(n)

    if not n_str:
        return []

    def backtrack(index, path):
        """
        Helper function for backtracking to generate letter combinations.
        
        Args:
        index (int): The current index of the digit being processed.
        path (list of str): The current string being built.
        """
        if index == len(n_str):
            combinations.append(''.join(path))
            return

        current_digit = n_str[index]
        possible_letters = digit_to_letters.get(current_digit, '')

        for letter in possible_letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    combinations = []
    
    backtrack(0, [])

    return combinations

def subsequence(s1: str, s2: str) -> bool:
    """
    Checks if the string `s1` is a subsequence of the string `s2`. 
    A subsequence means that all characters of `s1` appear in `s2` in the same order, but not necessarily consecutively.

    Args:
    s1 (str): The string that is checked to be a subsequence.
    s2 (str): The string in which `s1` is checked as a subsequence.

    Returns:
    bool: True if `s1` is a subsequence of `s2`, False otherwise.
    """
    if not s1:
        return True
    if not s2:
        return False
    if s1[0] == s2[0]:
        return subsequence(s1[1:], s2[1:])
    else:
        return subsequence(s1, s2[1:])