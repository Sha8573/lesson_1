
from connect import Database
def create_table():
    student_table = """
        CREATE TABLE student(
        student_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        email VARCHAR(50),
        birth_date DATE,
        phone_number VARCHAR()
        create_date TIMESTAMP DEFAULT NOW());
        """
    teacher_table = """
         CREATE TABLE teacher(
        teacher_id SERIAL PRIMARY KEY,
        first_name VARCHAR(20),
        last_name VARCHAR(20),
        email VARCHAR(50),
        birth_date DATE,
        phone_number VARCHAR()
        create_date TIMESTAMP DEFAULT NOW());
        """
    language_table = """
            CREATE TABLE language(
            language_id SERIAL PRIMARY KEY,
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
        """

    course_status_table = """
            CREATE TABLE course_status(
            course_status_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());
        """

    speciality_table = """
            CREATE TABLE speciality(
            speciality_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            create_date TIMESTAMP DEFAULT now());
        """

    course_table = """
            CREATE TABLE course(
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(30),
            description TEXT,
            rating FLOAT,
            active_Students INT,
            mentor_id INT REFERENCES student(student_id),
            language_id INT REFERENCES language(language_id),
            price NUMERIC,
            course_status_id INT REFERENCES course_status(course_status_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
        """

    payment_table = """
            CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            course_id INT REFERENCES course(course_id),
            student_id INT REFERENCES student(student_id),
            amount NUMERIC,
            card_number INT,
            create_date TIMESTAMP DEFAULT now());
        """

    speciality_course_table = """
            CREATE TABLE speciality_course(
                speciality_course_id SERIAL PRIMARY KEY,
                speciality_id INT REFERENCES speciality(speciality_id),
                course_id INT REFERENCES course(course_id),
                create_date TIMESTAMP DEFAULT now())
        """

    lesson_status_table = """
            CREATE TABLE lesson_status(
                lesson_status_id SERIAL PRIMARY KEY,
                name VARCHAR(30),
                create_date TIMESTAMP DEFAULT now())
        """

    modules_table = """
            CREATE TABLE modules(
                module_id SERIAL PRIMARY KEY,
                name VARCHAR(30),
                course_id INT REFERENCES course(course_id),
                lesson_count INT,
                last_update DATE DEFAULT now(),
                create_date TIMESTAMP DEFAULT now())
        """

    data = {
        "student_table": student_table,
        "mentor_table": teacher_table,
        "language_table": language_table,
        "course_status_table": course_status_table,
        "speciality_table": speciality_table,
        "course_table": course_table,
        "payment_table": payment_table,
        "speciality_course_table": speciality_course_table,
        "lesson_status_table": lesson_status_table,
        "modules_table": modules_table,


    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_table()
