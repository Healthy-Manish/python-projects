# collect email from the  user
# split the email using the @, the first part as the user name, the second part is gonna be saved as domain
# split domain using .,

def main():
    print("welcome to the email slicer")
    print("")

    email_input = input("enter your email address: ")
    (username,domain)= email_input.split('@')
    (domain,extension) = domain.split(".")

    print("username : ",username)
    print("Domain: ",domain)
    print("Extension: ",extension)

main()