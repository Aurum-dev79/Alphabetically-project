def add_name(name):
    try: 
       with open('directory.txt','a') as file:
           file.write(name+ "\n")
    except FileNotFoundError:
        with open('directory.txt', 'w') as file:
            file.write(name + "\n")


def delete_name(name):
    try:
        with open('directory.txt', 'r+') as file:
            lines = [line.strip() for line in file.readlines()]
            if name in lines:
                lines.remove(name)
                file.seek(0)  
                for element in lines:
                    file.write(element + "\n")
                file.truncate()
                return True  
            else:
                print("Do not find the name")
                return False  
    except FileNotFoundError:
        print("The file does'nt exist ")
        return False
    except Exception as e:
        print("unknow error", e)
        return False
    

def edit_name(name):
    try:  
        with open('directory.txt','r+') as file:
            file.seek(0)
            lines = [line.strip() for line in file.readlines()]
            if name in lines:
                new_name = str(input("write the new name: "))
                index_1 = lines.index(name)
                lines[index_1] = new_name
                file.seek(0)
                for element in lines:
                    file.write(element + '\n')
                file.truncate()
                return True    

            else:
             print("do not find the name")
             return False

    except FileNotFoundError:
        print("The file does'nt exist")       
        return False 
    


def sort_name():
    try: 
        with open("directory.txt","r+") as file:
            lines = [line.strip() for line in file.readlines()]
            file.seek(0)
            lines.sort(key=str.casefold)
            for element in lines: 
                file.write(element + '\n')
            file.truncate()





    except FileNotFoundError:
        print("The file does'nt exist")    

        
        
        

    
            

