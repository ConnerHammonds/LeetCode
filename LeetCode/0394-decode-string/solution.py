class Solution:
    def decodeString(self, s: str) -> str:
      stk = []
      cur_num = 0
      cur_str = ''

      for c in s:
        if c == '[':
          stk.append(cur_num)
          stk.append(cur_str)
          cur_num = 0
          cur_str = ''
        elif c == ']':
          prev_str = stk.pop()
          num = stk.pop()
          cur_str = prev_str + cur_str * num
        elif c.isdigit():
          cur_num = cur_num*10 + int(c)
        else:
          cur_str += c

      return cur_str

