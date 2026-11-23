# Welcome to Python Playground! 🐍
# 
# This is a web-based Python IDE that lets you write and run 
# Python code directly in your browser.
#
# Get started by writing some Python code below and 
# clicking the Run button. You can also create new files
# using the (+) button or upload files using the upload 
# icon (↑) in the sidebar.
#
# Try this example:

print("Hello, Python Playground!")

# Happy coding!

mylist=['kiran', 'manoj','anush','bijesh']
print(mylist)
print(mylist[0:2])
print(mylist[1:2])
print(mylist[1:])
print(mylist[1:-1])
print("Length of list", len(mylist))
print("Sorted list", sorted(mylist))
print("Max of the list element", max(mylist))
print("Min of list element", min(mylist))
mylist.append("kishan")
print(mylist.index('kiran'))
print("Original list ", mylist)
flist=[]
i=len(mylist)
for vlist in mylist:
    flist.append(mylist[i-1])
    i=i-1
print("Reversed list ", flist)
intlist=[0,2,3,4,6,7,8,12,45,21,68,55]
print(intlist[::3])
# Using list comprehension
every_third = [item for index, item in enumerate(intlist) if index % 3 == 0]
print(every_third)
# Using a regular for loop
result = []
for i in range(0, len(intlist), 3):
    result.append(intlist[i])
print(result)

superhero=input("Enter superhero name: ")
if superhero.startswith(("S","s")):
    print("Super hero name starts with S or s")
else:
    print("Doesnt start with S or s")



