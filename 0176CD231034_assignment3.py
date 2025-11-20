import os
import random
import datetime

# --- Global Variables ---
USERS_FILE = "users.txt"
RESULTS_FILE = "quiz_results.txt"
QUIZ_FILES = {
    "DSA": "DSA.txt",
    "DBMS": "DBMS.txt",
    "PYTHON": "PYTHON.txt"
}
CURRENT_USER = None 

# --- Helper: Initialize Dummy Files (So code works immediately) ---
def initialize_quiz_files():
    # This function creates the question files if they don't exist yet.
    # Format: Question|OptA|OptB|OptC|OptD|Answer
    
    dsa_data = [
        "What data structure uses LIFO?|a) Queue|b) Stack|c) Tree|d) Graph|b",
        "Worst case complexity of Bubble Sort?|a) O(n)|b) O(log n)|c) O(n^2)|d) O(1)|c",
        "Which is not a linear data structure?|a) Array|b) Linked List|c) Tree|d) Stack|c",
        "To access the 5th element of an array, time complexity is?|a) O(n)|b) O(1)|c) O(log n)|d) O(n^2)|b",
        "A binary search tree must satisfy which property?|a) Heap property|b) Ordering property|c) FIFO|d) None|b"
    ]
    
    dbms_data = [
        "What does SQL stand for?|a) Structured Query Language|b) Strong Question Language|c) Structured Question List|d) None|a",
        "Which is a DDL command?|a) SELECT|b) INSERT|c) CREATE|d) UPDATE|c",
        "A primary key must be?|a) Unique & Not Null|b) Unique only|c) Not Null only|d) Duplicate|a",
        "Which Normal Form deals with partial dependency?|a) 1NF|b) 2NF|c) 3NF|d) BCNF|b",
        "ACID properties stand for?|a) Atomicity, Consistency, Isolation, Durability|b) Atomicity, Class, Image, Data|c) None|d) All|a"
    ]
    
    python_data = [
        "Who developed Python?|a) Dennis Ritchie|b) Guido van Rossum|c) James Gosling|d) Bjarne Stroustrup|b",
        "Which is mutable?|a) Tuple|b) String|c) List|d) Integer|c",
        "Keyword to define a function?|a) func|b) define|c) def|d) function|c",
        "Output of 2 ** 3?|a) 6|b) 8|c) 9|d) 5|b",
        "Which library is used for data analysis?|a) Pandas|b) PyGame|c) Flask|d) Requests|a"
    ]

    # Write data only if file doesn't exist
    if not os.path.exists("DSA.txt"):
        with open("DSA.txt", "w") as f: f.write("\n".join(dsa_data))
    if not os.path.exists("DBMS.txt"):
        with open("DBMS.txt", "w") as f: f.write("\n".join(dbms_data))
    if not os.path.exists("PYTHON.txt"):
        with open("PYTHON.txt", "w") as f: f.write("\n".join(python_data))

def ensure_user_files_exist():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f: pass
    if not os.path.exists(RESULTS_FILE):
        with open(RESULTS_FILE, "w") as f: pass

# --- Core Functions ---

def load_questions_from_file(filename):
    questions = []
    if not os.path.exists(filename):
        return []
    
    with open(filename, "r") as f:
        for line in f:
            # Split line by '|'
            parts = line.strip().split("|")
            if len(parts) == 6: 
                q_obj = {
                    "q": parts[0],
                    "options": [parts[1], parts[2], parts[3], parts[4]],
                    "ans": parts[5]
                }
                questions.append(q_obj)
    return questions

def save_user_to_file(user_data):
    line = f"{user_data['username']}|{user_data['password']}|{user_data['name']}|{user_data['age']}|{user_data['email']}|{user_data['college']}|{user_data['year']}|{user_data['contact']}\n"
    with open(USERS_FILE, "a") as f:
        f.write(line)

def get_password_input():
    while True:
        p1 = input("Enter your password: ")
        p2 = input("Confirm your password: ")
        if p1 == p2:
            return p1
        else:
            print("Passwords do not match! Please try again.")

def register():
    print("\n--- REGISTRATION ---")
    username = input("Enter a new username: ")
    
    with open(USERS_FILE, "r") as f:
        if any(line.split("|")[0] == username for line in f):
            print("Username already exists! Try logging in.")
            return

    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    college = input("Enter your college name: ")
    year = input("Enter your year of study: ")
    contact = input("Enter your contact number: ")
    
    password = get_password_input()

    user_data = {
        "username": username, "password": password, "name": name,
        "age": age, "email": email, "college": college,
        "year": year, "contact": contact
    }
    
    save_user_to_file(user_data)
    print("Registration successful! Please Login.")

def login():
    global CURRENT_USER
    print("\n--- LOGIN ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "admin123":
        print("Welcome Admin! (Admin features unlocked)")
        CURRENT_USER = {"username": "admin", "role": "admin", "name": "Administrator"}
        return True

    with open(USERS_FILE, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) >= 8:
                u, p, n, a, e, c, y, cont = parts
                if u == username and p == password:
                    CURRENT_USER = {
                        "username": u, "password": p, "name": n, "age": a,
                        "email": e, "college": c, "year": y, "contact": cont, "role": "student"
                    }
                    print(f"Login Successful! Welcome, {n}.")
                    return True
    
    print("Invalid username or password.")
    return False

def attempt_quiz():
    if not CURRENT_USER:
        print("Please login first.")
        return

    print("\n--- SELECT CATEGORY ---")
    print("1. DSA")
    print("2. DBMS")
    print("3. PYTHON")
    choice = input("Select (1-3): ")
    
    # Map choice to File Names directly
    cat_map = {'1': 'DSA', '2': 'DBMS', '3': 'PYTHON'}
    category = cat_map.get(choice)
    
    if not category:
        print("Invalid Category")
        return

    # LOAD QUESTIONS FROM THE SPECIFIC FILE
    filename = QUIZ_FILES[category]
    questions_list = load_questions_from_file(filename)
    
    if not questions_list:
        print(f"Error: No questions found in {filename}.")
        return

    random.shuffle(questions_list)
    
    score = 0
    total = len(questions_list)
    
    print(f"\nStarting {category} Quiz... ({total} questions)")
    
    for i, q in enumerate(questions_list, 1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q['options']:
            print(opt)
        
        ans = input("Your answer (a/b/c/d): ").lower()
        if ans == q['ans']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer was {q['ans']}")

    print(f"\n--- QUIZ FINISHED ---")
    print(f"You scored: {score}/{total}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    record = f"{CURRENT_USER['username']}|{category}|{score}/{total}|{timestamp}\n"
    
    with open(RESULTS_FILE, "a") as f:
        f.write(record)
    print("Score saved successfully.")

def show_my_scores():
    if not CURRENT_USER: return
    
    print(f"\n--- PERFORMANCE HISTORY FOR {CURRENT_USER['username']} ---")
    print(f"{'Category':<10} {'Score':<10} {'Date Time':<20}")
    print("-" * 40)
    
    found = False
    with open(RESULTS_FILE, "r") as f:
        for line in f:
            # Handle potential empty lines
            if not line.strip(): continue
            
            parts = line.strip().split("|")
            if len(parts) == 4:
                u, cat, sc, dt = parts
                if u == CURRENT_USER['username']:
                    print(f"{cat:<10} {sc:<10} {dt:<20}")
                    found = True
    
    if not found:
        print("No quiz attempts found.")

def update_profile():
    global CURRENT_USER
    if not CURRENT_USER: return

    print("\n--- UPDATE PROFILE ---")
    print("Leave blank to keep current value.")
    
    new_email = input(f"New Email ({CURRENT_USER['email']}): ") or CURRENT_USER['email']
    new_college = input(f"New College ({CURRENT_USER['college']}): ") or CURRENT_USER['college']
    new_year = input(f"New Year ({CURRENT_USER['year']}): ") or CURRENT_USER['year']
    new_contact = input(f"New Contact ({CURRENT_USER['contact']}): ") or CURRENT_USER['contact']

    CURRENT_USER['email'] = new_email
    CURRENT_USER['college'] = new_college
    CURRENT_USER['year'] = new_year
    CURRENT_USER['contact'] = new_contact

    all_users = []
    with open(USERS_FILE, "r") as f:
        all_users = f.readlines()
    
    with open(USERS_FILE, "w") as f:
        for line in all_users:
            data = line.strip().split("|")
            if len(data) > 0 and data[0] == CURRENT_USER['username']:
                f.write(f"{data[0]}|{data[1]}|{data[2]}|{data[3]}|{new_email}|{new_college}|{new_year}|{new_contact}\n")
            else:
                f.write(line)
    
    print("Profile updated in database.")

def show_profile():
    if not CURRENT_USER: return
    print("\n--- PROFILE DETAILS ---")
    for k, v in CURRENT_USER.items():
        if k != 'password': 
            print(f"{k.capitalize()}: {v}")

def logout():
    global CURRENT_USER
    CURRENT_USER = None
    print("Logged out successfully.")

def about():
    print(''' 
    Choosing to study at LNCT (Lakshmi Narain College of Technology) in Bhopal means joining an
    institution synonymous with academic excellence...
    ''')

def quiz_menu():
    while True:
        if not CURRENT_USER:
            break 
        
        print(f"\n--- QUIZ DASHBOARD ({CURRENT_USER['username']}) ---")
        print("1. Attempt Quiz (DSA/DBMS/PYTHON)")
        print("2. View My Scores")
        print("3. View Profile")
        print("4. Update Profile")
        print("5. Logout")
        
        choice = input("Select Option: ")
        
        if choice == '1':
            attempt_quiz()
        elif choice == '2':
            show_my_scores()
        elif choice == '3':
            show_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
            break
        else:
            print("Invalid choice.")

def main_menu():
    # 1. Create users.txt and results.txt
    ensure_user_files_exist()
    # 2. Create DSA.txt, PYTHON.txt etc if they don't exist
    initialize_quiz_files()
    
    while True:
        if CURRENT_USER:
            quiz_menu()
        else:
            print("\n=== WELCOME TO LNCT QUIZ PORTAL ===")
            print("1. Registration")
            print("2. Login (User/Admin)")
            print("3. About")
            print("4. Exit")
            
            choice = input("Select Option: ")
            
            if choice == '1':
                register()
            elif choice == '2':
                if login():
                    quiz_menu() 
            elif choice == '3':
                about()
            elif choice == '4':
                print("Goodbye!")
                exit()
            else:
                print("Invalid Choice")

main_menu()