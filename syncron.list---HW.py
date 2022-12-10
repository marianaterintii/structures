#syncronisation list

from os import system
system ("cls")

students_first_name = [ ]
students_last_name = [ ]
students_age = [ ]
students_mark = [ ]

students_first_name.append( "Juli" )
students_last_name.append( "Pierre" )
students_age.append( 21 )
students_mark.append ( 9 )

index = []
student_index = students_first_name.index
while True:
    student_data = ( input ("Enter students data:" ) )
    if student_data == " ":
         break 
    student_data = student_data.split()
    
    fragments = student_data
    students_first_name.append(fragments[0])
    students_last_name.append(fragments[1])
    students_age.append(int (fragments[2]))
    students_mark.append (int(fragments [3]))

print ()


for x in range(4):
    print ( f" {x+1} {students_first_name[x]} {students_last_name[x]} {students_age[x]} {students_mark[x]}")
    

print ()

for i in range((len(students_first_name))):
           print ("Students first name:", f" {students_first_name [i]}")

print ()

   



   





