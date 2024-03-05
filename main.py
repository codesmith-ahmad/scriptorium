#This script must at the top level lest all imports will fail!

from myutils           import logging_config # Set up logger, do not remove
from os                import system
from presentation.View import *

def main():
    system('cls')
    View.start() # loop

if __name__ == "__main__":
    main()