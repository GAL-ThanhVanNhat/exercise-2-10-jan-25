from Doctor import *;

#newDoctor = Doctor("Napoleon", "Doe", 100000, "123 Main St")
#id = newDoctor.insert()
#print(f"Doctor ID: {id}")

doctors = Doctor.get_all()
for doctor in doctors:
    print(doctor.__repr__())
    
secondDoctor: Doctor = doctors[1]
secondDoctorId: int = secondDoctor[0]

Doctor.update_doctor_first_lastname(secondDoctorId, "test_Demo_2", "test_Demo_2")
Doctor.update_doctor_salary(secondDoctorId, 456789)
Doctor.update_doctor_address(secondDoctorId, "HCM Vietnam")
print(secondDoctor.__repr__())

dbSecondDoctor = Doctor.get_doctor_by_id(secondDoctorId)
print(dbSecondDoctor.__repr__())


