#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


import os
dir = str(os.path.curdir)
print(dir)

# relative directory not working on windows
# replace string with working directory
dir = "c:/Users/max.hilliard/OneDrive - HYPERTHERM, INC/Desktop/Day24-SnakeGame2/Mail Merge Project Start"

with open(dir+"/Input/Names/invited_names.txt") as name_file:
    name_list = name_file.readlines()

with open(dir+"/Input/Letters/starting_letter.txt") as start_letter:
    st_letter = start_letter.read()
    for name in name_list:
        name = name.strip()
        mod_letter = st_letter.replace("[name]", name)
        with open(f"{dir}/Output/ReadyToSend/{name}", "w") as new_file:
            new_file.write(mod_letter)