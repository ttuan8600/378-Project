#this file will be what is called by the webserver(website) and will handle the input data.
import sys
import main
import time
import os

#code from random website
if __name__ == "__main__":
    # [0] is used for filename
    email = sys.argv[1]
    password = sys.argv[2]

    main.login_email(email,password)
    
    

    while not os.path.exists(email+"call.txt"):
        time.sleep(2)
    with open(email+"call.txt") as file:
        var_return = file.readline().strip()
    
        if var_return == "1":
            main.call()
        else:
            main.text(email)

    main.open_mycsulb()
    main.log_info(email,password)
    main.driver.close
    # for i, arg in enumerate(sys.argv):
    #    with open("test.txt",'+a') as file:
    #        file.write(arg)
           
    #     # print(f"Argument {i:>6}: {arg}")