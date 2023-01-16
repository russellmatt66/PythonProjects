# Compute number of distinct workouts possible for current
# strength program.  
# Future extension: Create Randomized Workout Generator
from helper import computePossibilities
import sys

permutations = 1.0 # Squat and Deadlift baby
numExercises = 2
for i in range(len(sys.argv)-1): # i is ModeNumber 
    permutations *= computePossibilities(int(sys.argv[i+1]),i)
    numExercises += int(sys.argv[i+1])

print("There are " + str(permutations) + " possible distinct workouts \
for " + sys.argv[1] + " accessory compound(s), " +\
 sys.argv[2] + " assistance lift(s), " + sys.argv[3] + " calf, and "\
+ sys.argv[4] + " ab accessory movement(s)")

print("In total, you will be performing " + str(numExercises) + \
" exercises." )
