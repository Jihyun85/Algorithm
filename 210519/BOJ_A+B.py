# No.1000 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

num_list = input().split(" ")
print(int(num_list[0]) + int(num_list[1]))


# No.2558 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오. (첫째 줄에 A, 둘째 줄에 B가 주어진다. (0 < A, B < 10)

a = int(input())
b = int(input())
print(a+b)


# No.10950 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 내가 풀었던 풀이
num = int(input())
for i in range(num):
  input_list = input().split()
  print(int(input_list[0]) + int(input_list[1]))

# 다른 분의 풀이를 참고한 경우  (map과 int를 연관지어 생각하지 못했다!! int()도 함수다!)
num = int(input())
for i in range(num):
  a, b = map(int, input().split())
  print(a + b)


# No.10951 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

while(True):
  try:
    a, b = map(int, input().split())
    print(a + b)
  except:
    break


# No.10952 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 입력의 마지막에는 0 두 개가 들어온다.

while(True):
  a, b = map(int, input().split())
  if (a == 0 and b == 0):
    break
  print(a + b)


# No.10953 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)

num = int(input())
for i in range(num):
  a, b = map(int, input().split(','))
  print(a + b)


# No.11021 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.

num = int(input())
for i in range(num):
  a, b = map(int, input().split())
  print(f'Case #{i+1}: {a+b}')


# No.11022 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다. x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

num = int(input())
for i in range(num):
  a, b = map(int, input().split())
  print(f'Case #{i+1}: {a} + {b} = {a+b}')

  # print("Case %s: %s + %s = %s" %(i+1, a, b, a+b))  # formatting을 이용할 수도 있다!



