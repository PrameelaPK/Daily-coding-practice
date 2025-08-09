class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Step 1: Start from the end of the string
        i = len(s) - 1

        # Step 2: Skip trailing spaces
        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0  # To store the length of last word

        # Step 3: Count characters until we hit a space or reach start of string
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length


if __name__ == "__main__":
    # Example test cases
    solution = Solution()
    print(solution.lengthOfLastWord("Hello World"))  # Output: 5
    print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
    print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6