#간단한 계산기:
#a. 사용자에게 두 개의 숫자를 입력하라는 메시지를 표시합니다.
while True:
     try:
          f = float(input('첫번째 숫자를 입력하세요.'))
          break  
     except ValueError:  
          print("숫자를 입력해주세요.")
while True:
     try:
          s = float(input('두번째 숫자를 입력하세요.'))
          break  
     except ValueError:  
          print("숫자를 입력해주세요.")
print(f'첫번째 수 : {f}, 두번째 수 : {s}')

#b. 산술 연산(예: 더하기, 빼기, 곱하기, 나누기)이 있는 메뉴를 표시합니다.
while True:
     try:
          ch = int(input('진행할 연산을 고르세요. 1.더하기 , 2.빼기, 3.곱하기, 4.나누기\n'))
          if ch < 1 or ch > 4:
               raise ValueError("1부터 4까지의 번호를 입력해주세요.")
          break
     except ValueError as e:
          print(e)
#c. 사용자의 선택에 따라 숫자에 대해 선택한 작업을 수행합니다.

def one_Addition(f,s):
    return f+s

def two_Subtraction(f,s):
    return f-s

def three_Multiplication(f,s):
    return f*s
def four_Division(f,s):
    return round(f/s,7)

switch = {
    1: one_Addition,
    2: two_Subtraction,
    3: three_Multiplication,
    4: four_Division
}

def switch_case(x,f,s):
     fucn = switch.get(x, lambda: '잘못된 선택입니다.')
     if callable(fucn):
          return fucn(f,s)
     else:
          return fucn()
#d. 결과를 사용자에게 표시합니다.
print(f'결과 : {switch_case(ch,f,s)}')  
