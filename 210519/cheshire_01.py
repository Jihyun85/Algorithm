### 체셔의 퀴즈 

# 재귀함수로 풀기
def findSurvivor(survivors, stickownerIndex):
  if len(survivors) == 1:
      return survivors[0]
  else:
    # 만약 [0, 1, 2, 3, 4]에서 stickownerIndex가 4인 경우 index가 5인 값은 없으므로, stickownerIndex + 1 / len(survivor) => 즉, 5 / 5 = 0으로 가장 앞에 있는 값을 지워주게 된다!
    loser = (stickownerIndex + 1) % len(survivors)
    del survivors[loser]
    stickownerIndex = loser
    return findSurvivor(survivors, stickownerIndex)
  
survivors = list(range(1, 101))
stickownerIndex = 0
winner = findSurvivor(survivors, stickownerIndex)
print("The winner is %d✨" % winner)


# while문으로 풀기
user = list(range(1, 101))
thisTurnIndex = 0

while len(user) > 1:
  loser = (thisTurnIndex + 1) % len(user)
  del user[loser]
  thisTurnIndex = loser

print("The winner is %d🎉" % user[0])