

import sys
from multipledispatch import dispatch

dict1=dict()
#dict1={ 'file1':{"name":"Hello"} }
dict1={ 'file1': 'Hello' }

dict2 = dict()
dict2 ={ 'file2': 'Hellodir2' }

directories = dict()
directories = {'dir1' : ''}
directories['dir1'] = dict1 
directories['dir2'] = dict2


print(directories)


class Files():
    def __init__(self,dir_name,file_name,file_content):
        self.dir_name=dir_name
        self.file_name=file_name
        self.file_content=file_content
        #self.size=size
       # self.mode=mode


    @dispatch(str)
    def write_to_a_file(self, text):
        prev_content = directories[self.dir_name][self.file_name]
        directories[self.dir_name][self.file_name] = prev_content + " " + text
        print("Successfully written to file\n")

    @dispatch(int, str)
    def write_to_a_file(self, write_at, text):
        directories[self.dir_name][self.file_name] = directories[self.dir_name][self.file_name][:write_at] + text + directories[self.dir_name][self.file_name][write_at + 1:]
        print("Successfully written to file\n")

    @dispatch()
    def read_from_file(self):
        content = directories[self.dir_name][self.file_name]
        print(content)

    @dispatch(int,int)
    def read_from_file(self,start,size):
        content = directories[self.dir_name][self.file_name]
        print(content[start:size+start])

    def truncate_file(self,size):
        truncated_text = directories[self.dir_name][self.file_name][0:int(size)]
        directories[self.dir_name][self.file_name] = truncated_text
        print(truncated_text)

    def Move_within_file(self, _from, to, size):

            a = _from + size

           # s1 = 'Hello world!!'
            array = directories[self.dir_name][self.file_name][_from:a]
            # d= d.replace(d[_from:a], "")

            directories[self.dir_name][self.file_name] = directories[self.dir_name][self.file_name][:to] + array + directories[self.dir_name][self.file_name][to:]

            directories[self.dir_name][self.file_name]=directories[self.dir_name][self.file_name].replace(directories[self.dir_name][self.file_name][_from:a], "", 1)

file_obj=None


def existing_files(dictio):
    print("Following are the existing files")
    for key in dictio:
        print(key)

def existing_directories(directories):
    print("Following are the existing Directories")
    for key in directories:
        print(key)  

#===================================================
# This Function is Creating a file with unique name
#===================================================
def create_a_file(name,cont):
    dub=False
    for direct in directories:
        for file in directories[direct]:
            if name==file:
                dub=True
                print("This file already exists")    
                break   

    if (dub==False):
        existing_directories(directories)
        dir = input('Enter directory name in which you want to create a file : ')
        dup_dir = False
        for direct in directories:
            if direct==dir:
                dup_dir=True
                print('Directory Exists so file can be created')
                directories[dir][name]=cont
                print("File successfully created\n")


#==============================================
# Delete a file
#==============================================
def delete_a_file(dict1):
    print('existing files of dir1')
    existing_files(dict1)

    print('existing files of dir2')
    existing_files(dict2)
    dir_name=''
    file_name=input("Enter the name of file you want to delete: ")
    dub=False
    for direct in directories :
        for file in directories[direct]:
            if file_name == file:
                dub=True
                dir_name=direct
    if dub==True:
        print("This file exists so can be deleted")
        directories[dir_name].pop(file_name)          
        print(file_name + " deleted successfully!!!!!!!!!!!!\n")
    else:
        print('No such file exists')           
#==============================================
# move a file
#==============================================
def move_a_file():
    dir_n=''
    content=''
    new_dir=''
    dub=False
    dir_dub=True
    file_n=input('Write the name of file you want to move: ')
    for direct in directories:
        for file in directories[direct]:
            if(file_n==file):
                dir_n=direct;
                content=directories[direct][file]
                dub=True;
    if dub==True:
        directories[dir_n].pop(file_n)            
        new_dir=input('Name the directory you want the file to move: ')
        for direct in directories:
            if direct==new_dir:
                dir_dub=True
        if dir_dub==True:        
            directories[new_dir][file_n]=content

#==============================================
# make a directory
#==============================================
def make_dir(directories):
    sample_dict={'sample_file':'Hello World'}
    dir = input('Enter directory name: ')
    print(directories)   
    dub=False 
    for key in directories:
        if dir == key:
            dub=True
            print("This directory already exists")    
            break
    if (dub==False):
        directories[dir]=sample_dict
        print("directory successfully created\n")
    print(directories)   
      
    
#===================================================
# This Function is Chanding a directpry 
#===================================================
def change_dir():
    dir_open=input('Enter the name of directory you want to open: ')
    exists=False
    for direct in directories:
        if (dir_open==direct):
            exists=True
    if exists==True:
        print('Opening the directory '+ str(dir_open))
        print(" In directory --- directories "+" >> "+str(dir_open)+' >>'+str(directories[dir_open]))        
    else:
        print('No such directories exists')
#===================================================
# This Function is opening a file 
#===================================================
def open_a_file():
    file_n=input("Enter the name of file you want to open : ")
    dir_n=None
    cont=None
    file_obj=None
    for direct in directories:
        for file in directories[direct]:
            if file==file_n:
                dir_n=direct
                cont=directories[direct][file]
                file_obj=Files(dir_n,file_n,cont)
                print("file successfully opened")
                return file_obj  
      
#===================================================
# This Function is Closing a file object
#===================================================
def close_a_file(file_obj):
    file_n=input("Enter the name of file you want to close : ")
    if file_obj.file_name==file_n:
        print("Closing the file object")
        file_obj=None
        print('File sucessfully closed')
    else:
        print('File was already closed')
        
#==============================================
# write to a file
#==============================================
def write_to_a_file():
    file_obj=open_a_file()
    return file_obj

#==============================================
# read a file
#==============================================
def read_a_file():
    file_obj=open_a_file()
    return file_obj
            
#==============================================
# read a file
#==============================================
def truncate_a_file():
    file_obj=open_a_file()
    return file_obj

#==============================================
# move within a file
#==============================================
def move_within_a_file():
    file_obj=open_a_file()
    return file_obj
            
#==============================================
# show memory map
#==============================================
def show_mem_map(directories,dict1,dict2):
    i=1
    print('*******************\n                  MEMORY MAP                              \n*******************\n')
    print(directories)
    '''for keys in directories:
        print('directory Name: \n'+keys)
        print('\ndirectory Name\t\File Name\t File Content\t\t\n ')'''
    print('\nNo\t\tDirectory Name\t\tFile Name\t\tFile Content\t\tLength of file\t\tsize of file\n ')
    i=1
    for direct in directories:
        for file in directories[direct]:
            print(str(i) +'\t\t\t'+str(direct)+'\t\t\t'+str(file)+'\t\t\t\t'+str(directories[direct][file])+'\t\t\t\t' + str(len(directories[direct][file]))+'\t\t\t\t' +str(sys.getsizeof(directories[direct][file]))+'\n')
            i+=1     
            
#==============================================
# main menu 
#==============================================
rep=True
while (rep==True):  
        
    print("Select the function you want to choose")
    print("1) Create a file \n2) Delete A file \n3) Make directory \n4) Change directory \n5) Move a file \n6) Open a file \n7) Close a file \n8) Write to a file \n9) Read from a file \n10) Move within a file \n11) Truncate a file \n12) Memory Map \n13) Exit")
    
    option=input()
    option=int(option)
      
    if option==1:
        file_name=input("Enter the name of file to be created: ")
        content=input("Enter any content you want to store: ")
        create_a_file(file_name,content)
            
    elif option==2:
        delete_a_file(dict1)
        
    elif option==3:
        make_dir(directories)     
    
    elif option==4:
        change_dir()
    
    elif option==5:
        move_a_file()
    
    elif option==6:
        file_obj=open_a_file()

    elif option==7:
        close_a_file(file_obj)

    elif option==8:
        file_obj=write_to_a_file()
        if(file_obj!=None):
            text=input("Input text to be written :" )
            file_obj.write_to_a_file(text)
            print('DIsplaying content of file now')
            file_obj.read_from_file()
        else:
            print('Failed to open')
    elif option==9:
        file_obj=read_a_file()
        if(file_obj!=None):
            print("Reading content of file : " )
            file_obj.read_from_file()
        else:
            print('Failed to open')

    elif option==10:
        file_obj=move_within_a_file()
        if(file_obj!=None):
            to=input('Enter from where to move: ')
            _from=input('Enter from where content needed to be moved: ')
            size=input("Input the size till where to be moved: " )
            file_obj.Move_within_file(int(_from),int(to),int(size))
            print('DIsplaying content of file now')
            file_obj.read_from_file()
        else:
            print('Failed to open')

    elif option==11:
        file_obj=truncate_a_file()
        if(file_obj!=None):
            size=input("Input text the size till where to be truncated:" )
            file_obj.truncate_file(size)
            print('DIsplaying content of file now')
            file_obj.read_from_file()
        else:
            print('Failed to open')
    
    elif option==12:
        show_mem_map(directories,dict1,dict2)
        
    elif option==13:
        rep=False