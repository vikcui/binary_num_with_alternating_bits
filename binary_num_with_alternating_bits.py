# author: YANG CUI
"""
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.
"""

def hasAlternatingBits(n):
    """
    Time Complexity: O(1)O(1). For arbitrary inputs, we do O(w)O(w) work,
    where ww is the number of bits in n. However, w \leq 32w≤32.
    :param n: the input number
    :return: True if it has alternating bits false if it doesn't.
    """
    resultList = []
    # first generate the binary representation of n O(logn)
    while n != 0:
        reminder = n % 2
        resultList.insert(0,reminder)
        n = n // 2
    # one pass to check if there exists repeating bits O(logn)
    for i in range(1,len(resultList)):
        if resultList[i] == resultList[i-1]:
            return False
    return True

# print(hasAlternatingBits(5))