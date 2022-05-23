hrs = float(input("Enter Hours:"))
rate = float(input("Enter the rate:"))

if hrs > 40:
    pay = (40 * rate) + ((hrs - 40) * 1.5 * rate)

else:
    pay = hrs * rate

print(pay)
