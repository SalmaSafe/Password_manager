Title= input("Enter the name of platform: ")
Email= input("Enter Email: ")
userName= input("Enter Username: ")
Password= input("Enter password: ")

if __name__=="__main__":
    file= open(Title +".txt","a")    # created a file that will hold all my input info
    file.write("Platform:" + Title + "/n")     # the */n* represents new line which is shown in my password.py file.
    file.write("E-mail Address: " + Email + "/n")
    file.write("Username: " + userName + "/n")
    file.write("password: " + Password + "/n")
    file.write("/n")
