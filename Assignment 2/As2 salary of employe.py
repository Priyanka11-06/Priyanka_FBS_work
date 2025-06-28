# To calculate total salary of employee 

basic = float(input("Enter the basic salary of employee"))

da = 0.10 * basic
ta = 0.12 * basic
hra = 0.15 * basic

total_salary = basic + da + ta + hra

print("Total salary of employee is =", total_salary)