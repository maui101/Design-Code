# Mauro Serrano 42096674 Roberto Rivera 37577941

from pathlib import Path
import shutil

def get_path():
    '''Receives path and checks if it exists'''
    while True:

        path = Path(input(''))

        if path.exists() == True:
            return path
        else:
            print('ERROR')

def search():
    '''will look for first index'''
    while True:
        
        special_char = input() 

        if special_char[0].upper() in ['N','E']:
            name = special_char.split()
            
            try:
                file_name = name[1]
               
                character = name[0]
               
                return file_name,character  

            except:
                print('ERROR')

        elif special_char[0].upper() in ['S']:
            
            
            name = special_char.split()

            try:
                size = int(special_char[2:])
                
                if type(size) == int:
                
                    try:
                        file_name = name[1]
                        character = name[0]
                        
                        return file_name, character
                    except:

                        print('ERROR')
            except:
                print('ERROR')
 
        else:
            print('ERROR')

        

def path_list(p:Path)->list:
    '''checks if path is a file or a directory & makes a list of paths'''
    file_list = []
    
    for i in p.iterdir():
        
        if i.is_file():
            file_list.append(i)
            
        elif i.is_dir():
            file_list.extend(path_list(i))
        
    return file_list


def name_search(list_of_path,L2_input):
    '''will go through file_list and see if the input matches a file name'''

    matching_paths = []

    if L2_input[1].upper() == 'N':
        '''will check for files w/exact name'''
        
        word_match = L2_input[0]
 
        for i in list_of_path:
            if i.stem == word_match:
   
                matching_paths.append(i)
                
        return matching_paths

    elif L2_input[1].upper() == 'E':
        '''will check for files with specified extension'''

        suffix_match = L2_input[0]
        for i in list_of_path:
            if i.suffix == suffix_match or i.suffix[1:]== suffix_match:

                matching_paths.append(i)
        return matching_paths

    elif L2_input[1].upper() == 'S':
        '''will return files larger than the specified size'''
        
        size_match = L2_input[0]
        
        for i in list_of_path:
            
            if i.stat().st_size >= int(size_match):
                

                matching_paths.append(i)
        
        return matching_paths

           
        


def action_taken(match_paths):
    '''will take in the paths and perform an action on them'''

    while True:
            
        action = input()
        

        if action.upper() == 'P':
            '''will print file paths'''
            for i in match_paths:
                print(str(i))
            break
            
        elif action.upper() == 'F':
            '''will read and print the first line of each file'''
            try:
                
                for i in match_paths:
                    print(str(i))
                    f = open(str(i),'r')
                    print(f.readline())
                break
            
            except:
                break
            
        elif action.upper() == 'D':
            '''create a duplicate copy of a file & give extension dup'''
            try:
                
                for i in match_paths:
                    print(str(i))
                    x = str(i) + '.dup'
                    i = str(i)
                    shutil.copy2(i,x)
                break
                                   
            except:
                break

        elif action.upper() == 'T':
            '''updates the time modified'''

            try:
                
                for i in match_paths:
                    print(str(i))
                    i.touch()
                break
            
            except:
                break    
        else:
            print('ERROR')
        
    

if __name__ == '__main__':
    
    path = get_path()   #returns path
    L2_input = search()  # returns file_name & character
    list_of_path = path_list(path)   #returns file_list
    match_paths = name_search(list_of_path, L2_input)   #returns variable "matching_paths"
    act_taken = action_taken(match_paths)
