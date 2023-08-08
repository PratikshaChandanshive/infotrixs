#Python program for contact management system

import os
import csv
import datetime

#fuction for title
def title():
    line_1 = "****************************************"
    title = "Contacts Management System"
    line_2 = "****************************************"

    print(line_1.center(130)) #here, center() function is used to give the text align to the text
    print(title.center(130))
    print(line_2.center(130))

# now, we will create a class and in that class we will define all the functions for options
class contact_functions:
    contact_fields = ["Name","Mobile_No"]
    contact_database = "contacts.csv"
    contact_data = [] # this list is used to temporarily store the contact data 

    # create function
    def create(self):
        # now, using os module we will clear the  console and we create menu page
        os.system('cls')
        title()
        print("     Create Contact: ")
        print("     ----------------")
        print("")

        # now, one by one we iterate the contact_fields and get input from the user according to that fields 
        for fields in self.contact_fields:
            contact_details = input("   Enter " + fields + ":")
            print("")
            self.contact_data.append(contact_details)

        # now, we get date from the system
        Date = datetime.datetime.today()
        d = Date.strftime("%m %d %Y") # strftime() function is used to give the format to the date
        self.contact_data.append(d)

        # here using above statements we will get success to get input from an user.
        # now, we will insert these inputs into the csv file
        with open(self.contact_database, 'a') as file:
            write = csv.writer(file)
            write.writerows([self.contact_data])

        self.contact_data = [] # using this statement we will clear the contact_data list to get more inputs
        print("")
        print("Contact is created successfully".center(129))
        print("\n")
    
    # view function
    def view(self):
        os.system('cls')
        title()

        print("Contacts: ".center(10))
        print("---------".center(10))
        print("")

        count = 0
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data1 in read:
                if len(data1) > 0:
                    count = count + 1
            print("Total Contacts: ",count)
            print('')

        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            if os.path.getsize(self.contact_database) == 0:
                print("Contact book is empty, Please create contacts".center(129))
            else:
                for fields in self.contact_fields:
                    print('{0:<10}'.format(fields).center(10), end= "\t\t")
                print('{0:<10}'.format("Date"))
                print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','-----------','----'))
                print("")

                for data in read:
                    for item in data:
                        print('{:<10}'.format(item).center(10), end = "\t\t")
                    print("")
        
        print("\n")
        input("\t Press enter key to continue...".center(120))
        os.system('cls')

    # search function
    def search(self):
        os.system('cls')
        title()

        print("Search Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match = "false"
        search_value = input("Enter your name: ")
        print("")

        # first we display fields name
        for fields in self.contact_fields:
            print('{0:<10}'.format(fields).center(10), end= "\t\t")
        print('{0:<10}'.format("Date"))
        print('{:<10}\t\t{:<10}\t\t{:<10}'.format('-----','-----------','----'))
        print("")


        # now, we read the database for the match.
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if search_value == data[0]:
                        self.contact_match = 'true'
                        print('{:<10}\t\t{:<10}\t\t{:<10}'.format(data[0], data[1], data[2]).center(10))

        if self.contact_match == 'false':
            print("")
            print("Sorry!, there is no contact by this name".center(129))
        
        print("")

    # delete function
    def delete(self):
        os.system('cls')
        title()

        print("Delete Contact: ".center(10))
        print("----------------".center(10))
        print("")

        self.contact_match = "false"
        delete_value = input("Enter your name: ")
        update_list = []

        # reading file to get match of the search
        with open(self.contact_database, 'r') as file:
            read = csv.reader(file)
            for data in read:
                if len(data) > 0:
                    if delete_value != data[0]:
                        update_list.append(data) 
                    else:
                        self.contact_match = 'true'

        # conditions to delete matched contact     
        if self.contact_match == 'true':
            with open(self.contact_database, 'w') as file:
                write = csv.writer(file)
                write.writerows(update_list)
                print("")
                print("Contact is deleted successfully...!".center(129))
                print("")

        if self.contact_match == 'false':
            print("")
            print("Sorry! data not found" .center(129))
            print("")


# crating object of the class 
contact_class = contact_functions()

os.system('cls')
title()

while True:
    print("1. View Contacts".center(128))
    print("2. Create Contact".center(129))
    print("3. Search Contact".center(129))
    print("4. Delete Contact".center(129))
    print("5. Exit".center(120))
    print("_______________________________________".center(130))
    option = int(input("\t\t\t\t\t\t\t Choose your option: "))

    # now we, put some conditions to acess above options and using that conditions we call there functions like view(), create(), search() and delete() functions.

    if option == 1:
        contact_class.view()
        title()
    
    if option == 2:
        while True:
            contact_class.create()
            ans = input("\t\t\t\t\tDo you want to create another contact number?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else: break
        
        os.system('cls')
        title()
    
    if option == 3:
        while True:
            contact_class.search()
            ans = input("\t\t\t\t\tDo you want to search another contact number?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else: break
        
        os.system('cls')
        title()

    if option == 4:
        while True:
            contact_class.delete()
            ans = input("\t\t\t\t\tDo you want to delete another contact number?[Y/N]: ")

            if ans == 'Y' or ans == 'y':
                continue
            else: break
        
        os.system('cls')
        title()


    if option == 5:
        os.system('cls')
        line_1 = "****************************************"
        msg    = "   Thank You for using this software"
        line_2 = "****************************************"
        print(line_1.center(130))
        print(msg.center(130))
        print(line_2.center(130))
        break

    if option > 5 or option < 1:
        os.system('cls')
        print("Invalid choice. Please choose valid option.".center(129))
        print("\n")

        input("Press enter key to continue...".center(130))
        os.system('cls')
        title()