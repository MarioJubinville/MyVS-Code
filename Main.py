import time


print("Hello World")
input("Press any key to start the countdown...")

for remaining in range(3, 0, -1):
    print(f"{remaining}...")
    time.sleep(1)

print("0!")
