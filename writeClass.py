#From BicycleRaceSplits
import readline
import string
from pathlib import Path
import copy
referanceFilePath = "Referance/"

class ReadFile:
    #This class is mainly meant to read variables stored in a text file, and
    #store those variables as a dictionary using the .dictionaryData function
    #These variables can then be used for program configuration or other inputs
    #correct usage would be to have each line in the .txt file represent a
    # different value in the dictionary.  Seperate the values by a colon :
    # ie- First_Name:Brian will create a dictionary entry of First_Name = Brian

    def __readFile(self):
        #probably should just read file at init and return data here?
        self.thisData = self.file_object.read()
        return self.thisData

    def __openFile(self):
        self.file_object = open(self.filePath, 'r')

    def __closeFile(self):
        self.file_object.close()

    def __processValuesDictionary(self):
        #loop through items either in file or in string variable
        for i in range(20):
            #TODO improve for loop

            #Read a line and split
            x = self.file_object.readline().split(':')

            #add line to dictionaryData
            if(len(x)>1):
                #get rid of endline charactor
                if x[1].endswith('\n'):
                    x[1] = x[1][0:-1]
                self.dictionaryData[x[0]] = x[1]
            # if not x:
            #     print("Successfully enter break")
            #     break
        pass


    def getValuesAsDictionary(self):
        #simply returns what has already been calculated
        return self.dictionaryData

    def getValueAsInt(self,thisKey):
        #Todo, test to make sure output is supposed to be an int
        if True:
            return int(self.dictionaryData[thisKey])
        else:
            print("error Code 3092")

    def getValueAsStr(self,thisKey):
        return self.dictionaryData[thisKey]

    def __init__(self, fileName):
        self.fileName = fileName
        self.filePath = Path(referanceFilePath + fileName)
        self.__openFile()
        self.dictionaryData = dict()
        self.__processValuesDictionary()
        self.__closeFile()

class WriteFile:
    #This class is mainly meant to write variables to be stored in a text file, and
    # those variables can be accessed as a dictionary using the ReadFile Class
    #This is meant to be a permanent storage for dictionaryData so that it can
    #be refered to later.  This is a really low grade database
    #correct usage would be to have each line in the .txt file represent a
    # different value in the dictionary.  Seperate the values by a colon :
    # ie- First_Name:Brian will create a dictionary entry of First_Name = Brian
    def __readFile(self):
        # print('reading file')
        self.thisData = self.file_object.read()
        # print('read file complete')
        return self.thisData

    def __openFile(self):
        #filePath = Path(self.filePath)
        if self.filePath.is_file():
            print('warning! filePath already exists.  Will be written over')
        self.file_object = open(self.filePath, 'w')
        # print('opened file')

    def __closeFile(self):
        self.file_object.close()

    def saveValuesAsDictionary(self):
        combineText = list()
        for i in self.dictionaryData:
            # thisLine = i + self.dictionaryData[i] + "\n"
            thisLine = ":".join((i,self.dictionaryData[i]))
            combineText.append(thisLine)
            # self.localText.join(thisLine)

        newText = "\n".join(combineText)
        with open(self.filePath, 'w') as f:
            print(newText, file=f)

    def __init__(self, fileName, inputDictionary):
        self.fileName = fileName
        self.filePath = Path(referanceFilePath + fileName)
        self.dictionaryData = copy.deepcopy(inputDictionary)
        #self.__openFile()
        self.localText = string
