# Part 5
# Footprint of local transportation and travel
# Author: Yian Bian 260886212

from footprint_services import *
from footprint_transport import *
from footprint_consumption import *

PROMPT = 'Name of person (file must be in same directory): '

########################## 
def input_filename():
    '''() -> str
    Prompt the user to enter the filename of the input they
    want for the carbon footprint calculator (e.g. 'example'),
    EXCLUDES the .csv.

    >>> input_filename() # enter 'example'
    'example.csv'
    '''
    name = input(" the name of the person getting their footprint calculated is ") + ".csv"
    return name + ".csv"

######################### 


def footprint_calculator(file_name = "example.csv"):
    '''(str) -> NoneType
    Read in the input from file_name, calculate CO2E footprint by category
    and print the output.'''
    results = calculate_footprint_from_input(file_name)
    output_results(results)


def calculate_footprint_from_input(fname):
    '''(str) -> lst
    Read input from file with name fname, call the six relevant functions,
    and return a list with the result for each function.
    '''
    funs = [fp_of_utilities, fp_of_studies, fp_of_computing, fp_of_diet,
            fp_of_transportation, fp_of_travel]
    results = ['']*6

    with open(fname, 'r') as f:
        f.readline() # lose the header

        # for calling the functions
        curr_fun = -1
        args = []

        for line in f:
            if '-'*8 in line:
                if len(args):
                    #print(args, curr_fun)
                    results[curr_fun] = funs[curr_fun](*args)
                curr_fun += 1
                args = []

            else:
                val = line.split(',')[-1].strip()
                if val:
                    args.append(float(val))
        
    return results


def output_results(results):
    '''(lst) -> NoneType
    Print out the results.'''
    names = ['Utilities', 'University', 'Computing', 'Diet', 'Transportation', 'Travel']
    delim = '\t'
    print('Category', 'Tonnes CO2E (sum: ' + str(round(sum(results),4)) + ')', sep=delim)
    for i, n in enumerate(names):
        print(names[i] + ' '*(16 - len(names[i])), round(results[i], 4), sep=delim)


if __name__ == '__main__':
    fname = input_filename()
    if fname is not INCOMPLETE:
        footprint_calculator(fname)
    
