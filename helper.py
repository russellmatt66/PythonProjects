import numpy as np
import sys

def factorial(n: int) -> int:
    if(n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)

def choose(choose_from: int, to_choose: int) -> int:
    # print(choose_from)
    return factorial(choose_from) / (factorial(to_choose)\
        * factorial(choose_from - to_choose))

def computePossibilities(choose_num: int, ExerciseMode: int) -> int:
    Compounds = ["OHP","BENCH","HIPTHRUST"]
    Assistance = ["DIPS","CHINUPS","GOODMORNINGS","ROWS"\
        ,"CGBENCH"]
    AccessoryCalves = ["CALFRAISE","BOXJUMPS"]
    AccessoryAbs = ["ABCRUNCH","LANDMINEWIPERS"]
    if (ExerciseMode > 4): # Needs to be number of lists
        print("ExerciseMode value of " + ExerciseMode)
        sys.exit("Dimension of ExerciseMatrix anomalous")
    choose_from = 0
    match ExerciseMode:
        case 0: choose_from = len(Compounds)
        case 1: choose_from = len(Assistance)
        case 2: choose_from = len(AccessoryCalves)
        case 3: choose_from = len(AccessoryAbs)
    return choose(choose_from,choose_num)