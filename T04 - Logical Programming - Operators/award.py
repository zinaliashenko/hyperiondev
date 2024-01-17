# award.py

# enter the times for swimming, cycling, and running
swimming_time = float(input("Enter swimming time (in minutes): "))
cycling_time = float(input("Enter cycling time (in minutes): "))
running_time = float(input("Enter running time (in minutes): "))

# calculate the total time taken to complete the triathlon
total_time = swimming_time + cycling_time + running_time

# display the total time
print("Total time taken to complete the triathlon:", total_time, "minutes")

# determine the award based on the total time
if total_time <= 100:
    print("Award: Provincial Colours")
elif total_time <= 105:
    print("Award: Provincial Half Colours")
elif total_time <= 110:
    print("Award: Provincial Scroll")
else:
    print("No award")
