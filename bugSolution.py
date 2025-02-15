def function_with_uncommon_error_solution(a, b):
    try:
        if a == 0:
            return 0
        elif b == 0:
            return 0 #Handle b = 0
        else:
            return a / b
    except ZeroDivisionError:
        return float('inf') #Or handle as per your requirements.

result = function_with_uncommon_error_solution(10, 0) 