num = int(input("Enter  number of employee"))
total_salary_all = 0
for i in range(1,num+1):
    basic = float(input("Enter basic salary of employee"))
    if basic<20000:
        da = 0.10*basic
        ta = 0.12*basic
        hra = 0.15*basic
    else:
        da = 0.15*basic
        ta = 0.18*basic
        hra = 0.20*basic

    total_salary = basic + da + ta + hra
    print(" Total salary of employee", total_salary)

    total_salary_all += total_salary
    print("Total salary of all employee",total_salary_all)
