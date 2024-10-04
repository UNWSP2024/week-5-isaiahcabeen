# Program #1: Kilometer Converter
# Write a program that asks the user to enter a distance in kilometers, 
# then converts that distance to miles.  The conversion formula is as follows:  
# Miles = kilometers x 0.6214.   
# The conversion must be done as a function with input and output.


def kilometer_conversion(kilometers):
    miles = kilometers * 0.6214
    return miles


if __name__ == '__main__':
    kilometers = float(input('Enter distance in kilometers: '))

    miles = kilometer_conversion(kilometers)

    print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")
