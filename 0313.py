import random
print("1~10猜一個數字")

answer=random.randint(1,20)
counyer = 0
while counyer == 5:
    guess = input("猜猜看")
    guess = int(guess)
    
if guess > answer:
    print('太大')

else: guess > answer:
    print("太小")
            
else:
    print('答對')
    break