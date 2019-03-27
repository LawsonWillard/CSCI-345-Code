from __future__ import print_function
import hashlib
import itertools


class PasswordCracker:

    words = []
    fiveChar = []

    #Defines the dictionary to be used as well as getting the 5 char words
    def __init__(self, dictionary):
        PasswordCracker.words = dictionary
        for i in range(0, len(PasswordCracker.words)):
            if len(PasswordCracker.words[i]) == 5:
                PasswordCracker.fiveChar.append(PasswordCracker.words[i])


    #Implements 3 of the four rules
    def BruteForceAlgorithm(self, hash, dict):

        word = ''
        specialChars = ['*', '~', '!', '#']
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        for n in range(0, len(dict)):
            word = dict[n]
            if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                return hash+":"+word

        for i in range(3):
            if i == 0:
                for j in range(0, len(dict)):
                    for k in range(0,10):
                        word = dict[j]
                        word  = word.capitalize()
                        num = str(k)
                        word = word + num
                        if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                            return hash+":"+word
            elif i == 1:
                for k in range(1, 5):
                    for x in itertools.permutations(specialChars, k):
                            for k in range(0, 10000):
                                num = "0000"
                                num = int(num)
                                num = num + k
                                num = str(num)
                                strtup = ''.join(x)
                                num = strtup+num
                                if hash == hashlib.sha256(num.encode('utf-8')).hexdigest():
                                    return hash+":"+num
            elif i == 2:
               for j in range(0, len(PasswordCracker.fiveChar)):
                    word = PasswordCracker.fiveChar[j]
                    if "a" in word:
                        word = word.replace("a", "@")
                    if "A" in word:
                        word = word.replace("A", "@")
                    if "L" in word:
                        word = word.replace("L", "1")
                    if "l" in word:
                        word = word.replace("l","1")
                    if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                        return hash+":"+word
        return "nothing"


    #Deals with any length char password with up to 6 digits appended
    def rule4(self, hash, dict):

        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        word = ''
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=1):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=2):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=3):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=4):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=5):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word
        for j in range(0, len(dict)):
            for m in itertools.product(digits, repeat=6):
                word = dict[j]
                strtup = ''.join(m)
                word = word + strtup
                if hash == hashlib.sha256(word.encode('utf-8')).hexdigest():
                    return hash+":"+word


if __name__ == '__main__':


    file_object = open("Words.txt", "r")
    list = []
    passwords = []
    password_File = open("Passwords.txt", "r")
    #Clears password file
    open("Output.txt", "w").close()
    #Reopening for appending
    output_File = open("Output.txt", "a")

    line = password_File.readlines()

    for i in range(0, len(line)):
        line[i] = line[i].strip("\n")
        line[i] = line[i].split(":")
        passwords.append(line[i][1])

    for i in file_object:
        line = file_object.readline()
        line = line.strip("\n")
        list.append(line)


    pc = PasswordCracker(list)

    i = 0

    while i < len(passwords):
        hash = passwords[i]
        encryption = pc.BruteForceAlgorithm(hash, list)
        encryption = encryption.split(":")
        if (encryption[0] != "nothing"):
            print("Match Found!")
            passwords.remove(encryption[0])
            encryption = ":".join(encryption)
            output_File.writelines(encryption+"\n")
            i-=1
        i+=1

    output_File.close()
    output_File = open("Output.txt", "a")

    #Any word with up to 6 digits appended
    if len(passwords) == 0:
        print("finished cracking passwords")
    else:
        for j in range(0, len(passwords)):
            hash = passwords[j]
            encryption = pc.rule4(hash, list)
            output_File.writelines(encryption + "\n")




    file_object.close()
    password_File.close()
    output_File.close()