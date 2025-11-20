logged_user = ''
logged = False
def register():
    new_name = input("Enter your name: ")
    new_age = input("Enter your age: ")
    new_email = input("Enter your email: ")
    new_college = input("Enter your college name: ")
    new_year = input("Enter your year of study: ")
    new_user = input("Enter a new username: ")
    new_pass = input("Enter your password: ")
    new_pass2 = input("Confirm your password: ")
    if new_pass == new_pass2:
        print("Registration successful!")
    else:
        print("Passwords do not match. Please try again.")
        register()
# here i can add new function for passworrd as then I will only need to call that if both passwords 
# are not equal it will only go back to the password part not the whole registration part 
    pass
def login():
    global logged , logged_user
    if logged == False:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        print("Login successful!")
        logged = True
        logged_user = username
    else:
        print("You are already logged in.")
        print(f"hello, {logged_user}!")
    pass
def show_profile():
    global logged , logged_user
    if logged == False:
        print("You need to login first.")
        login()
    elif logged == True:
        print(f"hello, {logged_user}!")
        print("Profile details:")
        print("Name: [Name]")
        print("Age: [Age]")
        print("Email: [Email]")
        print("College: [College Name]")
        print("Year of Study: [Year of Study]")
    pass
def update_profile():
    global logged , logged_user
    if logged == False:
        print("You need to login first.")
        login()
    elif logged == True:
        print(f"hello, {logged_user}!")
        print("Update your profile details:")
        updated_name = input("Enter your new name: ")
        updated_age = input("Enter your new age: ")
        updated_email = input("Enter your new email: ")
        updated_college = input("Enter your new college name: ")
        updated_year = input("Enter your new year of study: ")
        print("Profile updated successfully!")
    pass
def logout():
    global logged , logged_user
    if logged == False:
        print("You are not logged in, so no need to logout.")
    elif logged == True:
        print(f"Goodbye, {logged_user}!")
        logged = False
        logged_user = ''
        print("You have been logged out successfully.")
    pass
def terminate():
    print("Exiting the program. Goodbye!")
    exit()
def Report():
    report_num = 0
    print('sorry that you are facing some problem')
    print('it is in  our priority to solve your problem as soon as possible')
    report_input = input("Please describe the problem you want to report: ")
    report_num += 1
    print(f"Thank you for your report. Your report number is {report_num}. We will get back to you soon.")
    pass
def helping():
    print("Help Section:")
    print('''Here are some common Acedemic queries you might have:
          1. How to register for courses?
          2. How to check my grades?
          3. How to contact my professors?
          4. How to access the library resources?
          5. How to apply for internships?
          6. How to join student clubs and organizations?
          7. How to get academic advising?
          8. Other queries..''')
    query = input("Do you have any specific query? if no Please type no otherwise starte the query below: ")
    query = query.lower()
    query_number = 0 
    if query != 'no':
        print('your query has been noted')
        query_detail = input("Please describe your query in detail: ")
        query_number += 1 
        print(f"Your query number is {query_number}. We will get back to you soon.")
    else:
        print('thank you for using the help section.')
        main()
    pass
def about():
    print(''' 
    Choosing to study at LNCT (Lakshmi Narain College of Technology) in Bhopal means joining an
    institution synonymous with academic excellence and a strong tradition of discipline, backed 
    by over three decades of success. The college is renowned for its state-of-the-art infrastructure,
    including well-equipped labs, digital classrooms, and a lush, sprawling campus that fosters a 
    focused learning environment. LNCT is consistently recognized for its strong focus on industry 
    readiness and boasts an impressive placement record, with leading companies regularly visiting the 
    campus. Here, you will benefit from a commitment to quality technical education, holistic development
    through various clubs and activities, and the chance to build a successful future in your chosen 
    professional field.''')
    pass
def main():
    while True:
        print("Welcome in LNCT")
        response = input('''
            Choose option:
            1. Registration
            2. Login
            3. Profile
            4. Update profile
            5. Logout
            6. Main Menu
            7. Report a Problem
            8. Help
            9. About
            10. Exit

                select option 1/2/3/4/5/6/7/8/9/10: ''')

        if response == '1':
            register()
        elif response == '2':
            login()
        elif response == '3':
            show_profile()
        elif response == '4':
            update_profile()
        elif response == '5':
            logout()
        elif response == '6':
            main()
        elif response == '7':
            Report()
        elif response == '8':
            helping()
        elif response == '9':
            about()
        elif response == '10':
            terminate()
        else:
            print("Invalid Choice, Please select correct option")
            main()
main()
