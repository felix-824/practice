'''Packages & Debugging
   (1) Python Packages & Core Package
   (2) Package Manager & Extrinal Package
   (3) Debugging
'''
from PIL import Image
import turtle
print("==== Python Packages & Core Package ====")
''' Python Packages/Modules: Core, File and External '''

# Core
# t = turtle.Turtle()
# t.shape("turtle")
# t.shape("turtle")
# t.speed(2)
# t.circle(150)
# turtle.done()

my_file = open("material/message.txt", "r")
try:
    content = my_file.read()
    print("content:", content)
finally:
    my_file.close()    
    
# with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)
    
print("DONE")        



print("==== Package Manager & Extrinal Package ====")
''' Package Managers: pip pipenv bpm yarn composer brew'''
# External Package > https://pypi.org/

with Image.open("material/Fujifilm.png") as img_obj:
    reversed_img = img_obj.resize((200, 200))
    reversed_img.show()
    reversed_img.save("material/sample.png")