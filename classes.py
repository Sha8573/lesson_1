from connect import Database


class Base:
    @staticmethod
    def select(table):
        query = f"SELECT * FROM {table}"
        return Database.connect(query, "select")

    @staticmethod
    def delete_id(table, id):
        query = f"DELETE FROM {table} WHERE student_id = {id}"
        return Database.connect(query, "delete")

    @staticmethod
    def update_id(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = {new_data} WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def update(table, colum_name, old_data, new_data):
        query = f"UPDATE {table} SET {colum_name} = '{new_data}' WHERE {colum_name} = '{old_data}'"
        return Database.connect(query, "update")

    @staticmethod
    def delete(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = '{data}'"
        return Database.connect(query, "delete")

    @staticmethod
    def delete_data(table, column_name, data):
        query = f"DELETE FROM {table} WHERE {column_name} = {data}"
        return Database.connect(query, "delete")


class Speciality(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"INSERT INTO {table}(name) VALUES('{self.name}')"
        return Database.connect(query, "insert")

class Profile(Base):
    def __init__(self, password, login, birth_date):
        self.password = password
        self.login = login
        self.birth_date = birth_date


class Course(Base):
    def __init__(self, name, description, rating, active_students, mentor_id, language_id, price, course_status_id):
        self.name = name
        self.description = description
        self.rating = rating
        self.active_students = active_students
        self.mentor_id = mentor_id
        self.language_id = language_id
        self.price = price
        self.course_status_id = course_status_id


    @staticmethod
    def select(table):
        query = """
            SELECT course.course_id, course.name, course.description, course.rating, mentor.first_name, mentor.last_name, course_status.name, language.name, course.price FROM course
                INNER JOIN mentor
                    ON course.mentor_id = mentor.mentor_id
                INNER JOIN course_status
                    ON course_status.course_status_id = course.course_status_id
                INNER JOIN language
                    ON language.language_id = course.language_id

        """
        return Database.connect(query, "select")

    def insert(self, table):
        query = (
            f"INSERT INTO {table}(name, description, rating, active_students, mentor_id, language_id, price, course_status_id, support_date)"
            f" VALUES('{self.name}', '{self.description}',  {self.rating},  {self.active_students},  {self.mentor_id},  {self.language_id},  {self.price},  {self.course_status_id})")
        return Database.connect(query, "insert")


