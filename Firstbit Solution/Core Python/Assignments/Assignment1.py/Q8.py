# Write a program to convert days into years, weeks and days.

days  = int(input("Enter the days: "))

years = (days // 365)

Remaning_Days = (days % 365)

weeks = (Remaning_Days // 7)

Days = (Remaning_Days % 7)

print(f'Years{years} weeks{weeks} Days{Days}')



