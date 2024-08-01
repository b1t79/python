import pickle

studentdata = {}
found = 0
rollno = int(input("Enter rollno to search: "))

with open("ss.data", "rb+") as myfile:
    while True:
        pos = myfile.tell()
        try:
            students_data = pickle.load(myfile)
        except EOFError:
            break

        if students_data['rollno'] == rollno:
            students_data['marks'] = float(input("Enter marks to update: "))
            myfile.seek(pos)
            pickle.dump(students_data, myfile)
            found = 1

if found == 0:
    print("Student marks updated successfully")