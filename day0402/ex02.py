import math

def getCircleArea(radius):

    return math.pow(radius,2) * math.pi

def getDonutArea(r1, r2):

    area1 = getCircleArea(r1)
    area2 = getCircleArea(r2)
    result = area1 - area2

    return abs(result)

if __name__ == "__main__":
	print(getDonutArea(5,10))