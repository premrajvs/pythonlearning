def validPalindrome(s):
    def is_pali(left, right):
        while left < right:
            if s[left] != s[right]: return False
            left += 1; right -= 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            # The "One-Deletion" Logic: Skip left OR skip right
            return is_pali(l + 1, r) or is_pali(l, r - 1)
        l += 1; r -= 1
    return True

if __name__ == "__main__":
    print(validPalindrome("acddba"))