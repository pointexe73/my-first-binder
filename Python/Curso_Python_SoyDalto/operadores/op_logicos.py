# OPERADORES LOGICOS

# and (&)
# el operador and es falso cuando uno de sus operandos es falso
op_and_1 = True and True 
op_and_2 = False and True
op_and_3 = True and False
op_and_4 = False and False

# or (|)
# el operador or el falso cuando todos sus operandos son falso
op_or_5 = True or True 
op_or_6 = False or True
op_or_7 = True or False
op_or_8 = False or False

# not (!)
# el operador not invierte el valor de su operando
# not True = False
# not False = True

op_not_9 = not True
op_not_10 = not False

print(f"Op_and, True and True: {op_and_1}: ")
print(f"Op_and, False and True: {op_and_2}: ")
print(f"Op_and, True and False: {op_and_3}: ")
print(f"Op_and, False and False: {op_and_4}: ")

print(f"Op_or, True or True: {op_or_5}: ")
print(f"Op_or, False or True: {op_or_6}: ")
print(f"Op_or, True or False: {op_or_7}: ")
print(f"Op_or, False or False: {op_or_8}: ")

print(f"Op_not, not True: {op_not_9}: ")
print(f"Op_not, not False: {op_not_10}: ")