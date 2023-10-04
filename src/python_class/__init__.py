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

# 命名規則 第一個字元可以是英文字母、中文、或底線_，第二個字元之後可以是英文字母、數字、中文或底線_
# 英文字母有大小寫之分
# 不能包含空白、＠、特殊符號

# Spyder ide 右邊 Help 視窗點擊換成 Variable Explorer
#%%
# 命名規則 上課範例
num1=123
num1=12.3
num1=12>3
num1='12>3'
num1
print(num1)

num2=567
num1=789
num3=num1+num2

del num2 # del 變數刪除 刪除num2
print(num3)

# %%
# = 賦值 右邊運算的結果帶到左邊
a=b=c='abc'   # 同時賦值 a='abc' b='abc' c='abc'
d="defg"      # 只賦值給 d
# k                     # k未賦值 提示錯誤
x,y,z=1,2,3    # x=1 y=2 z=3

#%%
# 型態變換
int('10')
int(3.14)
int(True)
int(False)
str(1.23)

# %%
# 運算式(運算元與運算子組成的敘述) = 運算元(運算式進行運算的對象) ＋ 運算子(進行運算的符號)
# Expression = Operands + Operators
# 常用運算子
# 算數運算子 +(加) -(減) *(乘) /(浮點數除法) //(整數除法) %(餘數) **(指數)
# 比較(關係)運算子 < > <= >= == != is not in
# 邏輯運算子 & and  | or  ! not()
# 指派運算子 = += -= *= /= %= //= **=
# << >>  ^  ~
# <<= >>= &= ^= |=
# 注意：// 除法整數部份的餘數，**

# %%
print(1, 2.5, True, 'xyz')
name='Bob'
print('Hello', name, sep='***')
print(1,2,3,4,5, sep='6')
print(1,2,3,4,5, end='---')
print(1,2,3,4,5)

# %%
# 輸入
# input()輸入後型態為字串
# eval()其他型態轉成數值型態
# num=eval(input()) 或 num=int(input()) 或 num=float(input())

# %%
# 格式化字串(通用型)
s="%s: %d %s: %f" % ("Number整數", 123, "Float小數", 12.3)
print(s)
print('%d除%d是%f' %(20, 7, 10/7))
print('%5d除%5d是%.3f' %(20, 7, 10/7))
print('%-5d除%-5d是%.3f' %(20, 7, 10/7))
print('%-8d除%-8d是%10.3f' %(20, 7, 10/7))

# %%
# 格式化字串(Python only)
print('{:.2f}'.format(3.1415926))
print('{:10s}'.format('ABCDE'))
print('{:.0f}'.format(3.1415926))
print('{:0>2d}'.format(3))
print('{:x>4d}'.format(10))
print('{:,}'.format(1000000))
print('{:10d}'.format(13))
print('{:<10d}'.format(13))
print('{:^10d}'.format(13))
print('{:.2%}'.format(0.13))
print('{:.2e}'.format(1000000))

print('{0:d}-{2:b}-{1:o}-{0:x}'.format(10, 20, 30))
print('{n1:d}-{n3:b}-{n2:o}-{n1:x}'.format(n1=10, n2=20, n3=30))
print('{n1:!>5d}-{n3:?^8b}-{n2:o}-{n1:x}'.format(n1=10, n2=20, n3=30))

# %%
# Exercise_1
def floatTryParse(value):
    try:
        return float(value), True
    except ValueError:
        return value, False

def squareLength():
    sideLength = floatTryParse(input('請輸入正方形邊長：'))
    if sideLength[1]:
      print('邊長為：%.2f\n週長為：%.2f\n面積為：%.2f' %(sideLength[0], sideLength[0] * 4, sideLength[0] ** 2))
    else:
      print('型態錯誤，請重新輸入數字')
      squareLength()

squareLength()

# %%
