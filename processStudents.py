''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv
def main():

# create a file object to open the file in read mode

    infile = open("students.csv",'r')

    students_file = csv.reader(infile, delimiter = ',')


# create a csv object from the file object

    students_file = csv.reader(infile, delimiter = ',')

#skip the header row


#create an outfile object for the pocessed record
    outfile = open("processedStudents.csv",'w')


#create a new dictionary named 'student_dict'

    student_dict = {
    "stud_id":{
        "firstname":{
            "lastname":{
                "major":{
                    "classification":{
                        "gpa:"
                    }
                }
            }
        }
    }
}
    
    

#use a loop to iterate through each row of the file
    print(student_dict['stud_id']['firstname']['lastname']['major']['classification']['gpa'])


    #check if the GPA is below 3.0. If so, write the record to the outfile
    for record in students_file:
        StudID = record[0]
        FirstName = record[2]
        LastName = [3]
        Major = [6]
        Class = [7]
        Gpa = ([8] < 3.0)
        outfile.write(StudID + ',' + FirstName + ',' + LastName + ',' Major )
        




        for record in student_file:
       FirstName = record[0]
       Grade1 = record[1]
       Grade2 = record[2]
       Grade3 = record[3]
       avg = (float(record[1]) + float(record[2]) + float(record[3]))/3
       outfile.write(FirstName + "," + format(round(avg,2)) + "\n") 
    
    infile.close()
    outfile.close()
    
main()

        



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    





#print the entire dictionary


#Print the student id 


#print out the corresponding GPA from the dictionary



#close the outfile








