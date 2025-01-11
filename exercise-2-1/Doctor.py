

from sqlite3 import *
from datetime import datetime
from constant import CONNECTION_STRING, CREATE_DOCTOR_TABLE_QUERY, DELETE_DOCTOR_ADDRESS_QUERY, INSERT_DOCTOR_QUERY , SELECT_SINGLE_DOCTOR_QUERY, SELECT_ALL_DOCTORS_QUERY, UPDATE_DOCTOR_FIRST_LASTNAME_QUERY, UPDATE_DOCTOR_SALARY_QUERY, UPDATE_DOCTOR_ADDRESS_QUERY

def create_doctor_table_if_not_exists(connection: Connection):
    connection.execute(CREATE_DOCTOR_TABLE_QUERY)

class Doctor:
    id: int
    def __init__(self, firstName: str, lastName: str, salary: int, address: str):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary
        self.address = address
        self.joiningDate = datetime.now()

    def __str__(self):
        return f"{self.firstName} {self.lastName} joined on {self.joiningDate} with salary {self.salary} and address {self.address}"

    def __repr__(self):
        return f"Doctor('{self.firstName}', '{self.lastName}', {self.salary}, '{self.address}')"

    def insert(self):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = INSERT_DOCTOR_QUERY.format(self.firstName, self.lastName, self.joiningDate, self.salary, self.address)
        cursor.execute(query)
        print(f"Doctor {self.firstName} {self.lastName} inserted successfully")
        connection.commit()
        self.id = cursor.lastrowid
        connection.close()
        return self.id
    
    @staticmethod
    def update_doctor_first_lastname(id: int, firstName: str, lastName: str):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = UPDATE_DOCTOR_FIRST_LASTNAME_QUERY.format(firstName, lastName, id)
        cursor.execute(query)
        print(f"Doctor {firstName} {lastName} updated successfully")
        connection.commit()
        connection.close()
    
    @staticmethod    
    def update_doctor_salary(id: int, newSalary: int):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = UPDATE_DOCTOR_SALARY_QUERY.format(newSalary, id)
        cursor.execute(query)
        print(f"Doctor's Salary updated successfully")
        connection.commit()
        connection.close()
    
    @staticmethod    
    def update_doctor_address(id: int, newAddress: int):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = UPDATE_DOCTOR_ADDRESS_QUERY.format(newAddress, id)
        cursor.execute(query)
        print(f"Doctor's Salary updated successfully")
        connection.commit()
        connection.close()
    
    @staticmethod
    def delete(self):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        query = DELETE_DOCTOR_ADDRESS_QUERY.format(self.id)
        cursor.execute(query)
        print(f"Doctor {self.firstName} {self.lastName} deleted successfully")
        connection.commit()
        connection.close()

    @staticmethod
    def get_all():
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = SELECT_ALL_DOCTORS_QUERY
        cursor.execute(query)
        doctors = cursor.fetchall()
        connection.close()
        return doctors

    @staticmethod
    def get_doctor_by_id(id: int):
        connection = connect(CONNECTION_STRING)
        cursor = connection.cursor()
        create_doctor_table_if_not_exists(connection)
        query = SELECT_SINGLE_DOCTOR_QUERY.format(id)
        cursor.execute(query)
        doctor = cursor.fetchone()
        connection.close()
        return doctor
