# int整數
print(123)

print(123*456)

print(123-999)

# float小數
# 因為二進位所以小數會有誤差，其他程式語言也會遇到
print(0.2-0.3)
print(0.1+0.2)

# bool布林
# bool() 會將 0, None, False 與 空的內容 轉換為 False, 其他的值轉換成 True
print(bool(123))
print(bool(123-32145/1235))

# str字串 '' 或 "" 不會做運算 字串內容不能換行
print('123*456')
print('0.1+0.2')
print('''bool(123-32145/1235)''')
# 多行字串
print('''bool(123-32145
      /1235)''')