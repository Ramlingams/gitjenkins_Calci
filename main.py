from calculator import add, subtract
from utils import greet

def main():
    greet("User")
    print("Addition:", add(5, 3))
    print("Subtraction:", subtract(5, 3))

if __name__ == "__main__":
    main()
