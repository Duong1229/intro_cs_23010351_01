from random import randint

secret_number = randint(1, 10)

while True:
    guess = input("What number am I thinking of? ")

    if secret_number == guess:
        print("Yay! You got it.")
        break
    else:
        print("No, that's not it.")
        
        
        
def guess1():
    secret_number = 8
    """
    hàm chơi doán số
    """

    guess = input("What number am I thinking of? ")

    if secret_number == guess:
        print("Yay! You got it.")
    else:
        print("No, that's not it.")
        
        
