#this file will be what is called by the webserver(website) and will handle the input data.
import sys
import main
#code from random website
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    with open(sys.argv[1]+"call.txt") as file:
        file.write(sys.argv[2])
        