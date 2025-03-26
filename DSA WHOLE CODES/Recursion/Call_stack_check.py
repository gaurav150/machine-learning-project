def funThree():
    print("Three")

def funTwo():
    funThree()
    print("Two")
    
def funOne():
    funTwo()
    print("One")

funOne()  