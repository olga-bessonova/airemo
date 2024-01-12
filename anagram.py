
def is_anagram(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    return s1_sorted == s2_sorted


print(is_anagram("aba", "baa"))
print(is_anagram("aba", "abaa"))