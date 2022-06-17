from typing import List

def sat191(summands: List[int], n=1234567890):
    return sum(summands) == n and min(summands) > 0 and len(summands) == 4 and all(s % 2 == 0 for s in summands)
def sol191(n=1234567890):
    """Find four positive even integers whose sum is n

    100 => [22, 24, 26, 28]"""
    return [2] * 3 + [n - 6]
# assert sat191(sol191())
