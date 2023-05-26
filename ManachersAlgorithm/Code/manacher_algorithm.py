

class Solution:
    BOGUS_CHAR = '|'

    def longestPalindrome(self, s: str) -> str:
        return self.manacherAlgorithm(s)

    def manacherAlgorithm(self, str):
        str = self.insertBogusCharacter(str)

        stringLength = len(str)
        palindromeRadii = [0 for _ in range(stringLength)]

        center = 0
        radius = 0
        while center < stringLength:

            while ((center - (radius + 1)) >= 0 and (center + radius + 1) < stringLength and str[center - (radius + 1)] == str[center + radius + 1]):
                radius += 1

            palindromeRadii[center] = radius

            oldCenter = center
            oldRadius = radius

            center += 1

            radius = 0
            while center <= (oldCenter + oldRadius):

                mirrorCenter = oldCenter - (center - oldCenter)
                maxMirrorRadius = oldCenter + oldRadius - center

                if (palindromeRadii[mirrorCenter] < maxMirrorRadius):
                    palindromeRadii[center] = palindromeRadii[mirrorCenter]
                    center += 1

                elif (palindromeRadii[mirrorCenter] > maxMirrorRadius):
                    palindromeRadii[center] = maxMirrorRadius
                    center += 1
                else:
                    radius = maxMirrorRadius
                    break

        maxRadius = float('-inf')
        maxIndex = None
        for index, radius in enumerate(palindromeRadii):
            if maxRadius < radius:
                maxRadius = radius
                maxIndex = index

        return str[maxIndex - maxRadius:maxIndex + maxRadius + 1].replace(self.BOGUS_CHAR, '')

    def insertBogusCharacter(self, str):
        stringList = [self.BOGUS_CHAR]
        for char in str:
            stringList.append(char)
            stringList.append(self.BOGUS_CHAR)
        return ''.join(stringList)


# Cool Test cases
print('😎 Cool Test Cases 😎')
print(Solution().longestPalindrome('abcbpbcba'))  # abcbpbcba
print(Solution().longestPalindrome('ababc'))  # aba
print(Solution().longestPalindrome('abcbpbcbp'))  # bcbpbcb

print('\n')
print('💡 Additional Test Cases 💡')
# Additional Test cases
print(Solution().longestPalindrome('abacaba'))  # abacaba
print(Solution().longestPalindrome('1234321098'))  # 1234321
print(Solution().longestPalindrome('aaaaaaa'))  # aaaaaaa
print(Solution().longestPalindrome('abcbpbcbammmmmmmmmmmmmmmmmmmm')) # mmmmmmmmmmmmmmmmmmmm
print(Solution().longestPalindrome('abaxyzzyxf'))  # xyzzyx
print(Solution().longestPalindrome('ababa'))  # ababa
print(Solution().longestPalindrome('abazaqa'))  # aba
