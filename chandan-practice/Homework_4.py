from pathlib import Path


try:
    fname = input("enter the path and file name")
    nfile = Path("/home/chandan-nekkanti/Practice/chandan-practice/nfile.txt")
    with open(fname, 'r') as file:
         cont = file.read()
         if len(cont) > 1:
              print("TRUE")
              with open(nfile,'w') as file:
                   file.write("This is a new file")
                  
         else:
              print("FALSE")
              with open(fname, 'a') as file:
                   file.write("\nThis file is quite possibly empty")
except(FileExistsError, FileNotFoundError) as err:
     print(f"make sure the file name is correct and exists within the mentioned path")

  