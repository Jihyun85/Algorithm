# No.11718 그대로 출력하기
# 입력 받은 대로 출력하는 프로그램을 작성하시오.
# 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

while(True):
  try:
    print(input().strip())
  except:
    break


# No.11719 입력 받은 대로 출력하는 프로그램을 작성하시오.
# 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다. 각 줄은 100글자를 넘지 않으며, 빈 줄이 주어질 수도 있고, 각 줄의 앞 뒤에 공백이 있을 수도 있다.

while(True):
  try:
    print(input())
  except:
    break


# No.11720 숫자의 합
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.
# 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

t = input()
num = input()
result = 0

for i in num:
  result += int(i)

print(result)


# No.11721 열 개씩 끊어 출력하기
# 알파벳 소문자와 대문자로만 이루어진 길이가 N인 단어가 주어진다.
# 한 줄에 10글자씩 끊어서 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 단어가 주어진다. 단어는 알파벳 소문자와 대문자로만 이루어져 있으며, 길이는 100을 넘지 않는다. 길이가 0인 단어는 주어지지 않는다.
# 출력 : 입력으로 주어진 단어를 열 개씩 끊어서 한 줄에 하나씩 출력한다. 단어의 길이가 10의 배수가 아닌 경우에는 마지막 줄에는 10개 미만의 글자만 출력할 수도 있다.

# 내가 풀었던 풀이(비효율적.. 내장함수를 더 많이 이용하자!)
text = input()

text_list = []
current_text = ""
for x in text:
  if (len(current_text) == 10):
    text_list.append(current_text)
    current_text = x
  else:
    current_text += x

text_list.append(current_text)

for i in text_list:
  print(i)
  

# 다른 분의 코드를 참고하여 작성
# range(시작숫자, 종료숫자, step)으로 사용할 수 있다!!!
text = input()
length = len(text)

for x in range(0, length, 10):
  print(text[x: x+10])
