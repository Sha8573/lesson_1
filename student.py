from connect import Database
from classes import Speciality, Profile


def courses(email, password):
    query = "SELECT * FROM course"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
            ID: {i[0]}
            Name: {i[1]}
            Description: {i[2]}
            Price: {i[7]}
            Rating: {i[3]}
        """)

    back = input("""
        0. back
            >>> """)
    if back == "0":
        return student(email, password)

    else:
        print("Error")
        return courses(email, password)


def speciality(email, password):
    query = "SELECT * FROM speciality"
    data = Database.connect(query, "select")
    for i in data:
        print(f"""
            ID: {i[0]}
            Name: {i[1]}
        """)

    back = input("""
        0. back
            >>> """)
    if back == "0":
        return student(email, password)

    else:
        print("Error")
        return speciality(email, password)

def profile(email, password):
    services = input("""
                1. Change password
                2. Change login
                3. Change birth date
                0. back
                    >>> """)

    if services == "1":
        return change_password(email, password)

    elif services == "2":
        return change_login(email, password)

    elif services == "3":
        return change_birth_date(email, password)

    back = input("""
           0. back
               >>> """)
    if back == "0":
        return student(email, password)

    else:
        print("Error")
        return speciality(email, password)

def change_password(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")

def change_login(email, password):
    column_name = input("Column Name: ")
    old_data = input("Now Data: ")
    new_data = input("New Data: ")

    if column_name == "profile_id":
        print()
    else:
        print()
    return speciality(email, password)


def change_birth_date(email, password):
    pass

def student(email, password):
    print(">>>>>>>>>>>> Student Page <<<<<<<<<<<")
    services = input("""
        1. Specialities
        2. Courses
        3. Profile
        4. back
            >>> """)

    if services == "1":
        return speciality(email, password)

    elif services == "2":
        return courses(email, password)

    elif services == "3":
        return profile(email, password)

    elif services == "4":
        return student(email, password)

    else:
        return student(email, password)
