# Programmer:Jonathan Lovo
# Course:CS151, Dr.Samari
# Date: 9/18/19
# Programming assignment:1
# Program inputs: Dimensions (height,length,width) of room in feet
# Program outputs: Amount of paint in gallons in feet to paint area
# comment: all dimensions will/must equal feet as well as area and gallons of paint and primer
# comment:run program and input length, width and height

length=input("what is the lenght?")
width=input("width?")
height=input("Height?")
height= int(height)
width = int(width)
length = int(length)
area=(length*width*height)
print (area)
paint_gallon= (area/350)
primer_gallon= (area/200)
print (paint_gallon)
print (primer_gallon)



