import random

def makeNums():

        balls = [ x for x in range(1,46)]
        random.shuffle(balls)
        #print(balls[0:6])
        return balls[0:6]



print("Hello World")



def input_display():
    money = int(input('금액을 입력하세요.'))
    if money % 1000 != 0:
        print("다시입력해주세요.")
        return input_display()
    else:
        return money / 1000

def main():
    count = input_display()
    for x in range(int(count)):
        nums = makeNums()
        print(sorted(nums))
    print("----------------------------")


if __name__ == "__main__":
    main()