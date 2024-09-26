#!/usr/bin/env python3
    # above tells the command line that 
    # this program should be executed using 
    # Python 3 interpreter
    # `chmod +x run.py` to make the script executable

# import classes
import ipdb
from lib.visit import Visit
from lib.museum import Museum
from lib.visitor import Visitor

m1 = Museum("Botanical")
m2 = Museum("The Met")

visitor_1 = Visitor("Emiley", "Pal")
visitor_2 = Visitor("Conner", "Price")

Visit(m1, visitor_1, "January 10, 2023")
Visit(m1, visitor_2, "January 10, 2023")
Visit(m2, visitor_1, "January 11, 2023")
#m1.visits()
#m1.visitors()

ipdb.set_trace()

if __name__ == '__main__':
    # should only execute this code if file called 
    # from the command line

    # create instances and test relationships

    # input function
    print('hello! :)')
