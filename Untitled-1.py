def ask1():
    s = str(input("enter somthing : "))
    def whatVowels(s):
        for i in s :
            if i == "a" or i == "o" or i == "e" or i == "i" or i == "u" or i == "y":
                print(i,end="")
    whatVowels(s)

    def whatVowel(s):
        vowels = "aeiouy"
        for x in s:
            if x in vowels:
                print(x, end="")
    whatVowel(s)

# ask1()

def ask2():
    s = str(input("enter somthing : "))
    def wordScore(s):
        x = 0
        vowels = "aeiou"    # 2 points
        mry = "mry"     # 3 points
        for i in s:
            if i in vowels:
                x += 2
            elif i in mry :
                x += 3
            else:
                x+=1
        return x
    print(f"the points you gained is : {wordScore(s)}")

#ask2()

def ask3():
    def numWars(n1,n2):
        if n1 >= n2 :
            x = n1
        else :
            x = n2
        
        counter = 0
        for i in range(2,x):
            if n1 % i == 0 and n2 % i == 0 :
                counter +=1
                if counter == 2:
                    break
        
        if counter >=2 :
            print("friends")
        else :
            print("enemies")
    
    n1 = int(input("enter a number : "))
    n2 = int(input("enter a number : "))
    
    numWars(n1,n2)

ask3()

def ask4():
    







ask4()