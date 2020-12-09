# Optimization using Genetic Algorithm
# Selva Subramani Damodaran
# CSC 425 525 - Fall 2020 

import sys

# parents array
codes = []

# code piece for square of prime
code='''def squarePrime(num):
        isPrime = False
        square = 0
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
        if(isPrime == True):
            square = num -2
        else:
            square = num +0
        return square'''

# The initial population consists of 4 members
# One of the member of initial population would be the original code itself
# The other three members are derived as result of mutatation of some parts of the original code
codes.append(code.replace('+','-'))
codes.append(code.replace('-','+'))
codes.append(code.replace('+','/'))
codes.append(code)

print(codes)
exec(code)

testlist = [3, 32, 8, 17, 19, 42, 13, 25]

try:
    print(squarePrime(testlist[0]))
except:
    print("Unexpected error:", sys.exc_info()[0])

# number of offsprings = set to 8
offs_per_pop = 8
# step size to stop the code for running infinite loops
steps = 10

# cross-over logic
def crossover(code):
    # cross over parts of code_temp
    code_temp = code
    code_temp = code_temp.replace("-","^")
    return code_temp

# mutation of code - logic
def mutate(code_temp):
    # mutate parts of the code_temp
    code_temp = code_temp.replace("+","*")
    return code_temp

# Fitness calculates the number of prime elements in the test array and then returns a score
def fitness(code_temp):
    score = []
    exec(code_temp)
    
    # as we may have "malformed" offspring, we use try clause to keep program runnning without stop the program
    try:
        for num in testlist:
            if(squarePrime(num)>0):
                score.append('T')
            else:
                score.append('F')
    except:
        print("Unexpected error:", sys.exc_info())
    return score

#Evaluate Probability of Fitnesses - compares the output of fitness function with expected value and generates score
def probability(score):
    prob =0

    expectedVal = ['T','F','F','T','T','F','T','F']
    
    for i in range(len(score)):
        if(score[i] == expectedVal[i]):
            prob+=1

    return prob

# test if the program fulfills the requirements, you can change it accordingly your preferences
def satisfied(codes):
    original_code='''def squarePrime(num):
        isPrime = False
        square = 0
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    isPrime = False
                    break
                else:
                    isPrime = True
        if(isPrime == True):
            square = num ^2
        else:
            square = num *0
        return square'''

    for str_code in codes:
        if(str_code == original_code):
            print("Found the right code! Exit~!")
            return True    
    return False

offspring = []
index = 0
# run until find the target
while not satisfied(codes) and index < steps:
    # generate offsprings
    index +=1
    offspring = []
    index1=0
    while len(offspring) < offs_per_pop and index1 < steps:
        index1+=1
        
        for c in codes:
            code_temp = ""
            code_temp = crossover(c)
            code_temp = mutate(code_temp)
            exec(code_temp)

            fitnessScore = fitness(code_temp)
            if(probability(fitnessScore) > 4):
                offspring.append(code_temp)

    # substitute the new generation as the parents
    if len(offspring) > 0:
        codes = offspring