score = 0

answer1 = input("True or False: The Earth is round\n").lower()
answer2 = input("True or False: The first Coca Cola was made in 1923\n").lower()
answer3 = input("True or False: Michael Jordan retired three times\n").lower()

if answer1 == "true":
    score += 1
if answer2 == "false":
    score += 1
if answer3 == "true":
    score += 1

print("Game over")
print("Your score:", str(score) + "/3")
