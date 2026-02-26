import random
import time
i=0
up=int(input("Enter upper limit "))
low=int(input("Enter lower limit "))
print("\nIoT Temperature Monitoring Started...\n")
while i<20:
    num = random.randint(low-1,up+1)
    print(f"Current Temperature: {num} °C")
    if num < low:
        print("Status: LOW Temperature Alert! ❄️\n")
    elif num > up:
        print("Status: HIGH Temperature Alert! 🔥\n")
    else:
        print("Status: Temperature is Normal ✅\n")
    i+=1
    time.sleep(2)