import random
def generatePassword(passlength):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []
    
    for i in passlength: 
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        passwords.append(password) 
    return passwords

def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword

def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword

def main():
    numPasswords = int(input("How many passwords would you like to generate? "))
    print("***GENERATING " +str(numPasswords)+" PASSWORD(S)***") 
    passwordLengths = []
    print("THE MINIMUM LENGTH OF EACH PASSWORD SHOULD BE AT LEAST 3.")

    for i in range(numPasswords):
        length = int(input("Enter the length of Password #" + str(i+1) + ": "))
        while length < 3:
            print("YOU HAVE ENTERED A NUMBER LESS THAN 3, PLEASE ENTER A NUMBER GREATER THAN 3!")
            length = int(input("Enter the length of Password #" + str(i+1) + ": "))
        passwordLengths.append(length)
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Generated Password #"+str(i+1)+" = " + Password[i])

main()
