import re;

class Solution:
    # @return an integer
    def myAtoi(self, str):
        str = str.strip()
        str = re.findall('(^[\+\-]*\d+)', str)

        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0

solu = Solution()
print(solu.myAtoi('   -123aa 23'))