class CitaMedica:
    def __init__(self, fecha, doctor, paciente):
        self.fecha = fecha
        self.doctor = doctor
        self.paciente = paciente

    def get_info(self):
        return f"Cita médica: {self.fecha}, Doctor: {self.doctor.nombre}, Paciente: {self.paciente.nombre}"


class Paciente:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.historial_clinico = []  # Lista de citas médicas

    def agregar_historial(self, cita):
        self.historial_clinico.append(cita)

    def listar_historial(self):
        if not self.historial_clinico:
            return "No hay citas en el historial."
        return [cita.get_info() for cita in self.historial_clinico]


class Doctor:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.citas = []  # Lista de citas médicas programadas

    def asignar_cita(self, paciente, fecha):
        nueva_cita = CitaMedica(fecha, self, paciente)
        self.citas.append(nueva_cita)
        paciente.agregar_historial(nueva_cita)


class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.doctores = []  # Lista de doctores
        self.pacientes = []  # Lista de pacientes

    def agregar_doctor(self, doctor):
        self.doctores.append(doctor)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def listar_doctores(self):
        if not self.doctores:
            return "No hay doctores registrados."
        return [doctor.nombre for doctor in self.doctores]

    def listar_pacientes(self):
        if not self.pacientes:
            return "No hay pacientes registrados."
        return [paciente.nombre for paciente in self.pacientes]


# Ejemplo de uso:
hospital = Hospital("Hospital Central")

# Agregar doctores
doctor1 = Doctor("Dr. Smith", 1)  # Cardiología
doctor2 = Doctor("Dr. Jones", 2)  # Neurología
hospital.agregar_doctor(doctor1)
hospital.agregar_doctor(doctor2)

# Agregar pacientes
paciente1 = Paciente("Alice", 30)
paciente2 = Paciente("Bob", 45)
hospital.agregar_paciente(paciente1)
hospital.agregar_paciente(paciente2)

# Asignar citas
doctor1.asignar_cita(paciente1, "2024-10-15")
doctor2.asignar_cita(paciente2, "2024-10-16")

# Listar doctores y pacientes
print("Doctores registrados:", hospital.listar_doctores())
print("Pacientes registrados:", hospital.listar_pacientes())

# Listar historial clínico de los pacientes
print("Historial de citas de Alice:", paciente1.listar_historial())
print("Historial de citas de Bob:", paciente2.listar_historial())
