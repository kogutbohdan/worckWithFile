from math import exp,sqrt

file=open('input.txt',"r")
output=open("output.txt","w")

textFromFile=file.read()
numbersFromFile=list(map(float,textFromFile.split(" ")))

def calculate(x,y):
    t=(sqrt(x)+sqrt(y))/exp(x)
    z=t+1
    print(f"x:{x}")
    print(f"y:{y}")
    print(f"z:{z}")
    print(f"t:{t}")
    return {
        "x":x,
        "y":y,
        "z":z,
        "t":t
    }



result=calculate(numbersFromFile[0],numbersFromFile[1])

output.write("""
        x:{x}
        y:{y}
        z:{z}
        t:{t}
    """.format(x=result["x"],y=result["y"],z=result["z"],t=result["t"]))

file.close()
output.close()