class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return 0
        if n < 10:
            return 1

        # t需要能被10整除
        def countPart(t):
            if t == 10:
                return 1
            s = t/10
            return 10 * countPart(t/10) + s
        ans = 0
        # 判断n是几位数，如n=388,l就是100
        y = 10
        while y <= n:
            y *= 10
        l = y / 10
        subn = n % l
        ans += self.countDigitOne(subn)
        c = n / l
        ans += c * countPart(l) + (l if c != 1 else subn+1) # 这里要注意下以1开头的情况
        return ans