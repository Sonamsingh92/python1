import pickle,  random, os

class Record:
    '''
    A class to represent a Record.
    '''
    def __init__(self,   key,  nonKey):
        '''
        Objective : To initialize the object of class Record.
        Input         :
             self : (Implicit Parameter) An object of class record.
        Return    : None
        '''

        self.keyAttr = key
        self.nonKeyAttr = nonKey

    def __str__(self):
        return 'KEY : '+str(self.keyAttr)

def recordKey(record):
    '''
    Objective : To return the key of the given node.
    Input          :
         node : An object of class Record.
    RETURN     : Key of the given node.
    '''
    return record.keyAttr

def RecordSave():
    '''
    Objective : To save records in a file and create an index file.
    Input          : None
    Return   : None
    '''
    
    start,  end,  min1,  max1,  min2,  max2 = 1, 100, 300, 500, 50, 250

    fout = open('records.bin','wb')

    allKeys = []

    for i in range(start, end):

        key = random.randint(min1, max1)

        while key in allKeys : key = random.randint(min1, max1)

        allKeys.append(key)

        nonKey = str(i)*5

        pickle.dump(Record(key, nonKey),  fout)

    fout.close()

    
    
def getFileEnd(file):

    endOfFile =  file.seek(0,  os.SEEK_END)

    file.seek(0)

    return endOfFile


                
def MergeSortFiles( ):
    '''
    Objective : To merge sort the records on the basis of key values.
    Input     : None
    Return    : None
    '''
    inputFile, f1, f2 = open('records.bin','rb'), open('f1.bin','wb'), open('f2.bin','wb')
     
    blockSize = 4

    endOfFile = getFileEnd(inputFile)

    while inputFile.tell() < endOfFile:

        list1, list2 = [[pickle.load(inputFile) for _ in range(blockSize) if  inputFile.tell() < endOfFile] for _ in range(2)]

        list1.sort(key = recordKey), list2.sort(key = recordKey)

        for x in list1: pickle.dump(x,f1)

        for y in list2: pickle.dump(y,f2)

    inputFile.close(), f1.close(), f2.close()

def RangeRecords(Filename,StartRec,EndRec):
    '''
    Objective: To retrive records in range StartRec tp EndRec.
    Input Parameters:
            Filename-> Name of file from which records are to be retrieved.
            StartRec-> Starting Record Number.
            EndRec-> Ending Record Number.
    Output : None
    '''
    f=open(Filename,'rb')
    p=pickle.load(f)
    size=f.tell()
    start=f.seek(size*(StartRec-1))
    end=f.seek(size*(EndRec-1))
    f.seek(start)
    while start<=end:
        print(pickle.load(f))
        start+=size
    f.close()

RecordSave()
MergeSortFiles()
filename=input('Enter File name form which records are to be retrieved : ')
s=int(input('Enter start record number  :  '))
e=int(input('Enter end record number : '))
RangeRecords(filename,s,e)
    
