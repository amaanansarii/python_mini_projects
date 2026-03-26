# import re

# def validate_email(email):
#     regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-0,-]+\.[a-zA-Z]{2,}$'

#     if re.match(regex, email):
#         return True
#     else:
#         return False


# email = input("Enter an email address: ")
# if validate_email(email):
#     print("Email adress is valid.")

# else:
#     print("Email address is not valid.")


email = input("Enter your Email: ") # @gmail.com .com .in checks needed

if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if 
        else:
            print("Wrong email 3") 
    else:
        print("Wrong email 2")
else:
    print("Wrong email 1")
