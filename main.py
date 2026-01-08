from calculator import add, subtract, divide, multi
from utils import greet

def main():
    greet("User")
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))
    print("Divide:", divide(5, 3))
    print("Multiply", multi(5,3))

if __name__ == "__main__":
    main()
