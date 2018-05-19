"""
Input: give a string consist bracket
Oupt: return a string that reverse inside bracket
example: input: abc(cd)nm
         output: abcdcnm
Ideal: sử dụng đệ quy để tính.(use recursive)
"""
def reverseParentheses(s):
    for i in range(len(s)):
        if s[i]=="(":
            start=i   #start sẽ là vị trí của '(' cuối cùng trước khi gặp ')' đầu tiên
        if s[i]==")":
            end=i     #start là vị trí của ')' đầu tiên
            return reverseParentheses(s[:start]+s[start+1:end][::-1]+s[end+1:]) #gọi đệ quy xử lý dấu ngoặc trong chuỗi mới.
    return s          # trả về chuỗi s không chứa bracket và đã đảo ngược.
print(reverseParentheses("abc(gf)"))      # show:  abcfg