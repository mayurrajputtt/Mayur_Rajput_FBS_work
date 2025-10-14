# Convert distant given in feet and inches into meter and centimeter.

feet = int(input("Enter the Feet: "))
inches = int(input("Enter the Inches: "))

total_inches = (feet * 12) + inches

centemeter = total_inches * 2.54

meter = centemeter / 100

print(f'{meter} This is meter {centemeter} This is centemeter')

