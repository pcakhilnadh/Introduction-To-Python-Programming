'''
Enter a number : 5
Required Output = factorial of 5 is : 120
'''
def factorial(number):
    if (number<=1):
        return 1
    else:
        return (number*factorial(number-1))

def main():
    inputNum = int(input("Enter a Number : "))
    print("factorial of "+str(inputNum)+" is :",factorial(inputNum))

if __name__ == '__main__':
    main()
