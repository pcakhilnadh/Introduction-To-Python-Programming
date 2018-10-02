'''
Enter a String : Introduction To Python
Required Output =  ['y', 't', 't', 'o', 'o', 'n', 'n', 'h', 'c', 'P', ' ']
'''
def main():
    inputString= input("Enter a String : ")
    inputList=list(inputString)
    inputList.sort()
    inputList.reverse()
    print("Required Output = ",inputList[::2])

if __name__ == '__main__':
    main()
