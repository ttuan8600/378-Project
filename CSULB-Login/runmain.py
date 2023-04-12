#this file will be what is called by the webserver(website) and will handle the input data.
import sys
import main
#code from random website
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    main.login_email(sys.argv[1],sys.argv[2])
    if sys.argv[3]:
        main.call()
    else:
        main.text(sys.argv[1])
    main.open_mycsulb()
    main.log_info(sys.argv[1],sys.argv[2])
    main.driver.close
    # for i, arg in enumerate(sys.argv):
    #    with open("test.txt",'+a') as file:
    #        file.write(arg)
           
    #     # print(f"Argument {i:>6}: {arg}")