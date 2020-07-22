student_name = input("Enter your name ")
school_name = 'FEDERAL BOARD OF INTERMEDIATE AND SECONDARY EDUCATION , ISLAMABAD'
print(school_name)
print("        SECONDARY SCHOOL CERTIFICATE (SSC) EXAMINATION")
print('                  Student Mark Sheet')
roll_number = 999364
print("Roll NUmber : " , roll_number)
reg_number = 1877020180
print("Regestraion no : " , reg_number)
group_name = "Humanities"
print("Group : " , group_name)
print("                        RESULT CARD")
print("                  ANNUAL EXAMINATION 2020")
print()
student_name = "HAFSAH BADAR"
father_name = "MUHAMMAD BADAR"
print("Camdidate's Name: " , student_name ,  end ="\t")
print("     S/D Of: " , father_name)
print()
print("                Obtained Marks"  )
print()
English = input("please enter your English marks out of 75" )
Urdu = input("please enter your Urdu marks marks out of 100" )
Maths = input("please enter your Maths marks marks out of 75" )
Computer = input("please enter your Computer marks marks out of 50" )
Gernal_Science = input("please enter your Gernal Science marks marks out of 100" )
Islamiyat = input("please enter your Islamiyat marks marks out of 50" )
Education = input("please enter your Education marks marks out of 50" )
Pakistan_Studies = input("please enter your Pakistan Studies marks marks out of 50" )
Obtained_marks = int (English) +int(Urdu)+int(Maths)+int(Computer)+int(Gernal_Science)+int(Islamiyat)+int(Education)+int(Pakistan_Studies)
print()
print("  Student Marks: " , Obtained_marks , end= "\t")
avg = (Obtained_marks/550) *100
print(" Percentage: " , avg ,    end="\t")
if (avg>=90) :
    print("Grade: A+ Outstanding")
elif (avg>=75) :
     print("   Grade: B Excellent")
elif (avg>=65) :
    print("Grade: C Very Good")
elif (avg>=45) :
    print("Grade: D Good ")
elif (avg>=30) :
    print("You Are Fail")











