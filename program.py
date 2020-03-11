import os
print("hello world")
print('hello dear friend akash')
print('hi there')
print('hey dear')
mystring=[1,'akash',2.5]
print(mystring)
print(mystring[2])
student_id = {'age':21,'name':'akash shalikram wendole','roll_number':34}   #dictionary declaration
print(f" {student_id['age']}\n {student_id['name']}\n {student_id['roll_number']}")     #calling values of dictionary
print(type(mystring[2]))
print(mystring.pop())
print(mystring)
mystring.insert(2,25)
print(mystring)
akash_marks = (4,3,6,2,3,5,3,9,1)
print(akash_marks[2])
print(akash_marks.index(4))
print(akash_marks.count(8))


myfile = open('test.txt')
path = os.getcwd()
print(path)
print(myfile.read())
myfile.seek(0)
print(myfile.read())
print("readlines\n function")
myfile.seek(0)
print(myfile.readlines())
print('reading seperate line')
myfile.seek(0)
print(myfile.readline(12))
print('closing the file')
myfile.close()
print('opening file from different location')
myfiletwo = open('/home/akash/akash.txt')
print(myfiletwo.read())
print('another way or new way of accessing file')
with open('test.txt') as my_new_file:
    print(my_new_file.read())
    my_new_file.seek(0)
    print(my_new_file.readlines())
print('append mode for file processing')
with open('test.txt' , mode='a') as append_file:
    append_file.write('\nThis is the appended line.')
with open('new_file.txt' , mode='w') as write_file:
    write_file.write('This is the file that i created.')
print('this is the testing of new file that is created')
with open('new_file.txt') as open_file:
    open_file.seek(0)
    print(open_file.read())
