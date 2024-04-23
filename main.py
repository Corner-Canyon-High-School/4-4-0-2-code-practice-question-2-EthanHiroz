red = int(input("Enter the Red: "))
green = int(input("Enter the Green: "))
blue = int(input("Enter the Blue: "))


if (red < 0 or red > 255):
    print("Red number is not correct")

if (green < 0 or green > 255):
    print("Green number is not correct")

if (blue < 0 or blue > 255):
    print("Blue number is not correct")

else:
    print("No problems found!")
