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

# 跳脫字元 和 格式化 寫法是跨程式語言
# 跳脫字元 通常以反斜線\ 加上字元表示
print('\\') # 反斜線
print("\'") # 單引號
print('\"') # 雙引號
print('\n') # 換行
print('\t') # tab鍵

#%%
print('it\'s a good day')

print('it\'s a go\tod \nday')
print('"is a good day"')