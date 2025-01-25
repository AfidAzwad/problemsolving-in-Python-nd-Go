def reverseVowels(s):
    L, R = 0, len(s) - 1

    # vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    vowels = set('aeiouAEIOU') # optimized - check why using set() is optimized here ?

    s = list(s)

    while L < R:
        if s[L] not in vowels:
            L += 1

        if s[R] not in vowels:
            R -= 1

        if s[L] in vowels and s[R] in vowels:
            s[L], s[R] = s[R], s[L]
            L += 1
            R -= 1
    return ''.join(s)


s = "IceCreAm"
print(reverseVowels(s))

"""
Optimized Approach:
- Use a `set` for vowels to achieve faster membership checks.
- Use two pointers (`L` and `R`) to traverse the string from both ends, swapping vowels when both pointers point to vowels.

Why is using a `set` optimized?
- Membership checks with a `set` are O(1), compared to O(n) with a `list`.
- For larger strings, this results in significant performance improvements when repeatedly checking if a character is a vowel.

Time Complexity (TC):
- O(n), where n is the length of the string `s`.
- Traversal through the string takes O(n), and membership checks using a `set` are O(1).

Space Complexity (SC):
- O(n) for the list version of the string.
- O(1) for the `set` of vowels, as the set size remains constant (10 vowels).
"""
