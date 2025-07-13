num = int(input("Enter a number of students"))
i = 0
total_percentage = 0

while i < num:
    print("Enter marks of students ")
    j = 0
    total_marks = 0

    while j < 5:
        mark = float(input("Enter marks of subject"))
        total_marks += mark
        j += 1
    percentage = total_marks / 5
    print("Percentage of students", percentage)
    total_percentage += percentage
    i += 1
averagr_percentage = total_percentage / num
print("Average percent of all students")

 