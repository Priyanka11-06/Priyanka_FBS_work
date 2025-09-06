def calculator():
    try:
        n1 = int(input("Enter first number"))
        n2 = int(input("Enter second number"))
        op = input("Enter operator(+,_,*,/):")

        if op == "+":
            result = n1+n2
        elif op == "_":
            result = n1-n2
        elif op == "*":
            result = n1*n2
        elif op == "/":
            if n2 == 0:
                raise ZeroDivisionError("Cannotdidvide by zero")
        else:
         raise ValueError("Invalid operator")
        
        print("Result =", result)

    except ValueError as ve:
        print("Error:", ve)
    except ZeroDivisionError as zde:
        print("Error:",zde)
    except Exception:
        print("Error:,Invalid output")

calculator()


        
        
        
        