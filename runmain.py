#this file will be what is called by the webserver(website) and will handle the input data.
import sys

#code from random website
if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")