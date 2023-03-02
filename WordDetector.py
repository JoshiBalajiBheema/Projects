import os
#The text file should be in the same folder as this script. or else copy and run this file from the destination folder

def isFound(filename):
    with open(filename, "r") as f:
        fileContent = f.read()
        return wordd in fileContent.lower()


wordd = input("Enter a key word to find: ")

if __name__ == "__main__":
    dir_contents = os.listdir()
    nWord = 0
    for item in dir_contents:
        if item.endswith("txt"):
            print(f"Detecting word in {item}")
            flag = isFound(item)
            if flag:
                print(f"{wordd} found in {item} ")
                nWord += 1
            else:
                print(f"{wordd} not found in {item} ")
    print("Word detector summary!")
    print(f"{nWord} files found with '{wordd}' in them.")
