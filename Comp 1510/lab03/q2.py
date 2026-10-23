message = input("Message: ")
while True:
    user_step = int(input("Step size: "))

    if user_step >= 1:
        break
    print("The step size must be at least 1")

index = 0
hidden = ""
while index < len(message):
    hidden += message[index]

    index+=user_step
    
print(f"Hidden message: {hidden}")

