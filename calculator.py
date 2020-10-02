#|---------------INSTRUCTION----------------------------------------------------------|
#|MAKE THIS CALCULATOR WHILE LEARNING PYTHON                                          |
#|FIRST WHEN THE DIALOUGE BOX OPEN WRITE add.                                    |
#|ON THE SECOND LINE WRITE THE FIRST NUMBER SUCH AS 2                                 |
#|ON THE THIRD LINE WRITE THE SECOND NUMBER SUCH AS 3                                 |
#|THEN THE OUTPUT WILL BE 5.BY THIS WAY YOU CAN DO sub,div,multi
#|---------------INSTRUCTION----------------------------------------------------------|

inputation = input("RESULT:")
#ADDITION 
if inputation == "add":
    add1 = float(input(""))
    add2 = float(input(""))
    print(add1 + add2)
#SUBTRACTION
if inputation == "sub":
    sub1 = float(input(""))
    sub2 = float(input(""))
    print(sub1 - sub2)
#DIVISION
if inputation == "div":
    div1 = float(input(""))
    div2 = float(input(""))
    print(div1 / div2)
#MULTIPLICATION
if inputation == "multi":
    multy1 = float(input(""))
    multy2 = float(input(""))
    print(multy1 * multy2)
