# Purpose: Calculate Blood Alcohol Concentration
# Author : Michael Lee
# Date: March 1, 2023


'''
    Computes blood alcohol concentration
    @param: drinks - how many drinks indivudal had as integer value; weight - bodyweight as integer; duration - time since last drink in minutes
    @return: Returns blood alcohol concentration for males and females given the same parameter input
'''
def computeBloodAlcoholConcentration(drinks, weight, duration):
    maleBac = drinks / weight * 3.8 - (duration / 40) * 0.01
    femaleBac = drinks / weight * 4.5 - (duration / 40) * 0.01
    maleBac = max(0, maleBac)
    femaleBac = max(0, femaleBac)
    return (maleBac, femaleBac)
'''
    Determines how impaired individual is based on blood alcohol concentration
    @param: bac - blood alchohol concentration as float value 
    @return: Returns determination of how intoxicated an individual is based on BAC
'''
def impairment(bac):
    if bac == 0:
        return "Safe to Drive"
    elif bac < 0.04:
        return "Some Impairment"
    elif bac < 0.08:
        return "Driving Skills Significantly Affected"
    elif bac < 0.1:
        return "Criminal Penalties in Most US States"
    elif bac <= 0.3:
        return "Legally Intoxicated - Criminal Penalties in All US States"
    elif bac > 0.3:
        return "Death is Possible!"
    else:
        return 
'''
    Makes impairment chart output
    @param: duration - time since last drink in minutes; sex - gender identity as single letter abbreviation; weight - bodyweight in pounds
    @return: Displays error message when given invalid inputs of sex
'''
def showImpairmentChart(weight, duration, sex):
    if sex.upper() == "M":
        bacConstant = 3.8
        sexFull = "male"
    elif sex.upper() == "F":
        bacConstant = 4.5
        sexFull = "female"
    else:
        print("Error: You must enter M or F")
        return
    
    print(f"{weight} pounds, {sexFull.lower()}, {duration} minute(s) since last drink")
    print("#drinks   BAC       Status")
    for drinks in range(12):
        maleBac, femaleBac = computeBloodAlcoholConcentration(drinks, weight, duration)
        bac = maleBac if sex.upper() == "M" else femaleBac
        status = impairment(bac)
        print(f"{drinks:<9}{bac:.4f}    {status}")

'''
    Asks user for integer until within range
    @param: lower - minimum value of integer; uppper - maximum value of integer
 
'''
def promptForInteger(lower, upper):
    while True:
        try:
            value = int(input())
            if value < lower or value > upper:
                print("Error: value out of bounds")

            else:
                return value
        except ValueError:
            print("Error: An integer value was expected. Try again")
'''
    Asks for male and female abbeviations
    @param: name and purpose of each parameter, if any
'''
def promptForMorF():
    print("Enter your sex as M or F: ")
    while True:
        value = input()
        if value.upper() == "M" or value.upper() == "F":
            return value.upper()
        else:
            print("\nError: You must enter M or F")

if __name__ == '__main__':
    print('Enter your weight (in lbs): ')
    weight = promptForInteger(0, 500)
    print('How many minutes has it been since your last drink? ')
    duration = promptForInteger(0, 300)
    sex = promptForMorF()
    showImpairmentChart(weight, duration, sex)
