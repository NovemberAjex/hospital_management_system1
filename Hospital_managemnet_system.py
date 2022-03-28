# open("Hospital_managemnt_system.txt","x")
def new_patient_data():
    new_patient_name = input("Please enter the name of the patient:  ")
    new_patient_ID= int(input("Please enter the ID of the new patient:  "))
    new_patient_address = input("Please enter the address of the patient:  ")
    new_patient_Fee = float(input("Please enter the fee of the patient:  "))
    new_patient_contact = int(input("Please enter the contact of the patient:  "))
    with open("Hospital_managemnt_system.txt", "a") as f:
        print(new_patient_name, new_patient_ID, new_patient_address, new_patient_Fee, new_patient_contact, file=f)
        f.close()
    new_patient_choice = int(input("You want to enter patient data 1 for Yes :  "))
    if new_patient_choice==1:
        new_patient_data()
    else:
        print("Your pateint data has been entered sucessfully")
def show_patient_data():
    with open("Hospital_managemnt_system.txt","r") as f:
        user_choice3 = int(input("Press 0 to show all the data and press 1 to show specific patient data:  "))
        if user_choice3==0:
            print(f.readlines())
        elif user_choice3==1:
            user_choice= int(input("Please enter the ID of the patient in 1 and 2 form"))
            user_choice2 = user_choice-1
            print(f.readlines()[user_choice2])
        else:
            show_patient_data()
        f.close()
def delete_patient_data():
    lines= []
    user_delete_input = int(input("Please give the ID of the patient you want to delete the data:  "))
    user_delete_input2 = user_delete_input-1
    with open("Hospital_managemnt_system.txt","r") as f:
        lines = f.readlines()
    with open("Hospital_managemnt_system.txt","w") as f:
        for x,y in enumerate(lines):
            if x not in [user_delete_input2]:
                f.write(y)

user_decide= int(input("""Please enter which function you want to choose
press 1 to enter new patient data
press 2 to show previous data
press 3 to delete patient data
press 4 to exit
   """))
if user_decide==1:
    new_patient_data()
elif user_decide==2:
    show_patient_data()
elif user_decide==3:
    delete_patient_data()
else:
    print("Please enter 1 or 2 or 3")









