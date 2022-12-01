from datetime import datetime

def Suma_log(data1, data2, data3):
    time=datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}    {} + {} = {} \n".format(time, data1, data2, data3))

def Minus_log(data1, data2, data3):
    time=datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}    {} - {} = {} \n".format(time, data1, data2, data3))

def Multiplications_log(data1, data2, data3):
    time=datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}    {} * {} = {} \n".format(time, data1, data2, data3))

def Division_log(data1, data2, data3):
    time=datetime.now().strftime("%H:%M")
    with open("log.csv", "a") as file:
        file.write("{}    {} / {} = {} \n".format(time, data1, data2, data3))
