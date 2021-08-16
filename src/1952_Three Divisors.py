"""
1952. Three Divisors
https://leetcode.com/problems/three-divisors/

Example 1:

Input: n = 2
Output: false
Explantion: 2 has only two divisors: 1 and 2.

Example 2:

Input: n = 4
Output: true
Explantion: 4 has three divisors: 1, 2, and 4.
"""

import math


class Solution:
    """
    TC: O(logN) / SC: O(N)
    Runtime: 28 ms, faster than 94.08%
    Memory Usage: 14.2 MB, less than 72.88%
    """

    def isThree(self, n: int) -> bool:
        divisors = []
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                divisors.append(i)
                if i * i != n:
                    divisors.append(int(n / i))
        return len(divisors) == 3
