try:
    input_hour = int(input("Enter Hours: "))
except Exception as e: print(e)

try:
    input_rate = int(input("Enter Rate: "))
except Exception as e: print(e)


def compute_pay(hour, rate):
    if hour>40:
        overtime = hour-40
        payment = overtime * rate * 1.5 + 40 * rate
    else:
        payment = hour * rate
    return payment

print("Hours worked: ", input_hour,'\nPayment: ', compute_pay(input_hour, input_rate))