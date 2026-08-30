class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        words = []
        for c in s:
            if c != ' ':
                word += c
            else:
                if word != '':
                    words.append(word)
                    word = ''
        
        if word != '' and word != ' ':
            words.append(word)
        
        words = words[::-1]
        
        ans = ''
        for word in words:
            ans += word
            ans += ' '
            
        return ans[:-1]
        


