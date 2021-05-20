# No.2741 N 찍기
# 자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.
# 출력: 첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
max_num = int(input())
for i in range(max_num):
  print(i+1)

# comprehension 이용 ✨✨✨
[print(i + 1) for i in range(max_num)]


# No.2742 기찍 N
# 자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

max_num = int(input())

# 입력값에서 index를 빼는 방법
for i in range(max_num):
  print(max_num - i)

# comprehension 이용
# [print(max_num - i) for i in range(max_num)] 

# reversed 이용
for i in reversed(range(max_num)):
  print(i + 1)


# No.2739 구구단
# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 출력 형식에 맞춰서 출력하면 된다.
N = int(input())
for i in range(9):
  print(f'{N} * {i + 1} = {N * (i + 1)}')
[print(f'{N} * {i + 1} = {N * (i + 1)}') for i in range(9)]


# No.1924 2007년 
# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
# 입력: 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
# 출력: 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.

# 직접 작성한 코드 (비효율적이다. 가독성이 좋지 않다.)
month, day = map(int, input().split())

week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
thirty = [4, 6, 9, 11]

month_to_day = 0
if (month - 1 > 0):
  for i in range(month - 1):
    if (i + 1 == 2):
      month_to_day += 28
    elif (i + 1 in thirty):
      month_to_day += 30
    else:
      month_to_day += 31


total = day + month_to_day
index = total % 7
print(week[index])

# 다른 분의 풀이를 참조
X, Y = map(int, input().split())

A = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
B = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 , 31]  # month도 list를 만들면 훨씬 간편하게 풀 수 있겠구나!!!

Day = 0
for i in range(X - 1):
  Day += B[i]

Day += Y % 7
print(A[Day])


# No.8393 n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
n = int(input())
result = 0
for i in range(n):
  result += i + 1
print(result)


# No.10818 최소 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

# 내가 푼 방법
N = int(input())
A = list(map(int, input().split()))
A.sort()
print(A[0], A[-1])

# 다른 분의 풀이를 참고한 방법
N = int(input())
A = list(map(int, input().split()))
print('{} {}'.format(min(A), max(A)))  # min과 max 내장함수를 쓰면 더 간결하게 표현이 가능하다!
print(f'{min(A)} {max(A)}')


# No.2438 별 찍기 - 1
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
N = int(input())
# 1번 방법
for i in range(N):
  print('*' * (i + 1))
# 2번 방법
[print('*' * (i + 1)) for i in range(N)]
# range를 다르게 사용하는 방법
for i in range(1, N+1):
  print('*' * i)


# No 2439 별 찍기 - 2
# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
N = int(input())
for i in range(1, N+1):
  print(' ' * (N - i) + '*' * (i))


# No.2440 별 찍기 - 3
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
N = int(input())
for i in reversed(range(1, N+1)):
  print('*' * i)


# No.2441 별 찍기 - 4
# 첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
# 오른쪽 기준으로 시작
N = int(input())
for i in reversed(range(1, N+1)):
  print(' ' * (N - i) + '*' * i)


# No.2442 별 찍기 - 5
# 첫째 줄에는 별 1개, 둘째 줄에는 별 3개, ..., N번째 줄에는 별 2×N-1개를 찍는 문제
# 별은 가운데를 기준으로 대칭이어야 한다.
N = int(input())
for i in range(1, N+1):
  star = ' '*(N-i) + '*' * (2*i - 1)
  print(star)


# No.2445 별 찍기 - 8
# 예시 (N=5)
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

N = int(input())

for i in range(1, N+1):
  star = '*' * i
  blank = ' ' * ((N * 2) - (i * 2))
  print(star + blank + star)

for i in reversed(range(1, N)):
  star = '*' * i
  blank = ' ' * ((N * 2) - (i * 2))
  print(star + blank + star)

# 줄여쓰면
for i in range(1, N+1):
  print('*'*i + ' '*(N*2 - i*2) + '*'*i)
for i in reversed(range(1, N+1)):
  print('*'*i + ' '*(N*2 - i*2) + '*'*i)


# No.2522 별 찍기 - 12
N = int(input())
for i in range(1, N+1):
  print(' '*(N-i) + '*'*i)
for i in reversed(range(1, N)):
  print(' '*(N-i) + '*'*i)


# No.2446 별 찍기 - 9
N = int(input())
for i in reversed(range(1, N+1)):
  print(' '*(N-i) + '*'*(i*2 - 1))
for i in range(2, N+1):
  print(' '*(N-i) + '*'*(i*2 - 1))


# No.10991 별 찍기 - 16
N = int(input())
for i in range(1, N+1):
  blank = ' ' * (N - i)
  star = '* '*(i-1) + '*' if i-1 > 0 else '*'  # 굳이 필요없던거지;;;
  print(blank + star)

# 줄여쓰기
for i in range(1, N+1):
  print(' '*(N-i) + '* '*(i-1) + '*')