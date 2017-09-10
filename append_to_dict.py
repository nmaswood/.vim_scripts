import argparse
import sys
import os
from pathlib import Path

def extension(name):

    return name.split(".")[-1]

def determine_dir():

    def get_ext():

        arg = sys.argv[1]
        return "general" if arg == "GENERAL" else extension(arg)

    return '{}/.vim_dictionaries/{}'.format(os.environ["HOME"], get_ext())

def write_file(name, word):
    with open(name, 'a') as infile:
        infile.write("\n" + word)

name = determine_dir()
write_file(name, sys.argv[2])
