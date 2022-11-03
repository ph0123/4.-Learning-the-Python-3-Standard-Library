# Command Line Arguments
import sys

# Print Arguments
print("Number of arguments: ", len(sys.argv), ' arguments.')
print("Arguments ", sys.argv)

# Remove Arguments
sys.argv.remove(sys.argv[0])

print("Arguments", sys.argv)

# Sum up the Arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum = sum + number
    except Exception:
        print("Bad input")

print(sum)

#remember "import system"
#import sys
#sys.argv is a list of arguments. argv[0] is the program's name

