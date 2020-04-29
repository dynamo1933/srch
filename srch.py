import os
import sys
import pyperclip

foundfilelist=[]

def findninfile(filename,srchword):
    if os.path.isfile(filename):
        #print(len(str(filename)))
        #check weather the file is commpressed or Not
        #if str(filename[-3:0]) !='zip':
            with open(filename) as f:
                if srchword in f.read():
                    foundfilelist.append(filename)

    


def listdir(argv,word_in):
    entries = os.listdir(argv)
    str1 = '\n'.join(entries)
    print("********************************************************************************************")
    print("TOTAL ENTRY TO BE SEARCHED ")
    print("********************************************************************************************")
    #print((str1))
    # for value input 
    for entry in entries:
        print(argv +'/'+ entry)
    yesstring=input("\n PRESS 'Y' TO START SEARCH OR ANY BUTTON TO END \n")
    if yesstring =='Y':
        for entry in entries:
            #print(argv[0]+''+entry)
            findninfile(argv+'/'+entry,word_in[0])
        print("\n********************************************************************************************")
        print("WORD FOUND IN THE FOLLOWING LOCATION")
        print("********************************************************************************************\n")
        print('\n'.join(foundfilelist))
        print("\n********************************************************************************************\n")
if __name__ == "__main__":
    strclip=pyperclip.paste()
    print(strclip)

    listdir(strclip,sys.argv[1:])    