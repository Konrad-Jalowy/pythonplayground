from PIL import Image

# color --> "red" or (255,0,0) or #ff0000
# img = Image.new('RGB', (200, 400), (255, 255, 255))
# img.show()
if __name__ == '__main__':
    while True:
        width = int(input("Width please\n"))
        height = int(input("Width please\n"))
        red = int(input("How much red?\n"))
        green = int(input("How much green?\n"))
        blue = int(input("How much blue?\n"))
        img = Image.new('RGB', (width, height), (red, green, blue))
        img.show()
        quit_flag = input("Press q to quit, enter to continue\n")
        if quit_flag.lower() == "q":
            break
