total_seconds = int(input("Enter a positive whole numebr of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(seconds, "seconds is equivalent to: ", hours, "hours", minutes, "minutes", seconds, "seconds")
