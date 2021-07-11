class Solution:
    def reverseWords(self, s) :
        """
        Do not return anything, modify s in-place instead.
        """
        sol = ''.join(s).split(' ')[::-1] # ['blue', 'is', 'sky','the']
        k = len(s)
        n = 0
        for i in range(len(sol)):
            string = sol[i]
            m=len(string)
            s[n:n+m]= string
            if n+m < k:
                s[n+m] = ' '
            n += m+1


if __name__ == '__main__':
    sol = Solution()
    s = ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"]
    print(sol.reverseWords(s))