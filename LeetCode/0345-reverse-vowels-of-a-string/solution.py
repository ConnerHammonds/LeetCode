class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # Convert to list since strings are immutable
        word = list(s)
        l = 0
        r = len(s) - 1

        # Move pointers towards each other until they each find a vowel
        while l < r:
            while l < r and word[l] not in vowels:
                l += 1
            while l < r and word[r] not in vowels:
                r -= 1
            
            # Swap the vowels
            word[l], word[r] = word[r], word[l]

            # Move the pointers after swapping
            l += 1
            r -= 1
        
        # Join the word list together using join() which returns a string
        return "".join(word)
