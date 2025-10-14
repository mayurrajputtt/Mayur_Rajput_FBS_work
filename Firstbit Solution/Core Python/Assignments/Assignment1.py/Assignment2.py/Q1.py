# Convert the time entered in hh,min and sec into seconds.

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds  = int(input("Enter the seconds: "))

total_seconds =(hours*3600) + (minutes*60) + seconds
print(total_seconds)

# convert_hours = hours*3600
# convert_seconds = minites*60