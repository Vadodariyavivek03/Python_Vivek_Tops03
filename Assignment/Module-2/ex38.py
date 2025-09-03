import pywhatkit as pwk, os

pwk.sendwhatmsg_instantly("+918980268240", "Hello!")

os.rename("PyWhatKit_DB.txt", "Temp_Data/PyWhatKit_DB.txt")

# os library is used to rename or move file and save in particular folder.

print("Successfully Sent...!!")