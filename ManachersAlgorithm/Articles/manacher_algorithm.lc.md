# Intuition
To solve it in a better way by reusing the pre-computed palindrome 

# Approach
[Manacher's Algorithm](https://en.wikipedia.org/wiki/Longest_palindromic_substring)

In Manacher's Algorithm, we will be reusing the previously identified palindrome by exploiting the palindrome inside another palindrome.


# Complexity
- Time complexity: `O(n)`
    -   This algorithm runs at O(n) time because the inner loop will also increment the center variable based on the pre-computed palindrome with the previous center
- Space complexity: `O(n)`
    -   Since the extra space is due to the palindromeRadii, which stores the radius of the longest palindrome centered at its index


# Limitation
This algorithm won't work if the longest palindrome is of even length, to make it work for an even palindrome we need to insert a bogus character ('|' -> Bogus character) in between each character including the boundaries

# Code
`Python3`
```
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


```

# Cool Test cases
There are three cases that are if | else-if | else

When the palindrome at mirroed center
- lies inside the old center ('abcbpbcba')
- extends outside the old center ('ababc')
- equal to the old center ('abcbpbcbp')


You can get the additional test cases and souce code [here](https://github.com/nirmalraj2000/Leetcode-Solution/tree/main/ManachersAlgorithm)