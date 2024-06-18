# test_persona.py
import unittest
from persona import Persona
from dottore import Dottore
from fatture import Fattura
from paziente import Paziente

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.persona = Persona("Mario", "Rossi")

    def test_initialization(self):
        self.assertTrue(self.persona.getName(), str)
        self.assertTrue(self.persona.getLastname(), str)


    def test_set_name(self):
        self.persona.setName("Luigi")
        self.assertTrue(self.persona.getName(), str)

    def test_set_last_name(self):
        self.persona.setLastName("Bianchi")
        self.assertTrue(self.persona.getName(), str)

    def test_set_age(self):
        self.persona.setAge(30)
        self.assertTrue(self.persona.getAge() >= 30)


class TestDottore(unittest.TestCase):
    def test_initialization(self):
        d = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        self.assertEqual(d.getName(), "Mario")
        self.assertEqual(d.getLastname(), "Rossi")
        self.assertEqual(d.getAge(), 0)
        self.assertEqual(d.getSpecialization(), "Cardiologo")
        self.assertEqual(d.getParcel(), 150.0)

        d = Dottore(123, "Rossi", "Cardiologo", 150.0)
        self.assertIsNone(d.getName())
        self.assertEqual(d.getLastname(), "Rossi")
        self.assertEqual(d.getSpecialization(), "Cardiologo")
        self.assertEqual(d.getParcel(), 150.0)

        d = Dottore("Mario", 123, "Cardiologo", 150.0)
        self.assertEqual(d.getName(), "Mario")
        self.assertIsNone(d.getLastname())
        self.assertEqual(d.getSpecialization(), "Cardiologo")
        self.assertEqual(d.getParcel(), 150.0)

        d = Dottore("Mario", "Rossi", 123, 150.0)
        self.assertEqual(d.getName(), "Mario")
        self.assertEqual(d.getLastname(), "Rossi")
        self.assertIsNone(d.getSpecialization())
        self.assertEqual(d.getParcel(), 150.0)

        d = Dottore("Mario", "Rossi", "Cardiologo", "cento")
        self.assertEqual(d.getName(), "Mario")
        self.assertEqual(d.getLastname(), "Rossi")
        self.assertEqual(d.getSpecialization(), "Cardiologo")
        self.assertIsNone(d.getParcel())

    def test_setSpecialization(self):
        d = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        d.setSpecialization("Dermatologo")
        self.assertEqual(d.getSpecialization(), "Dermatologo")

        d.setSpecialization(123)
        self.assertIsNone(d.getSpecialization())

    def test_setParcel(self):
        d = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        d.setParcel(200.0)
        self.assertEqual(d.getParcel(), 200.0)

        d.setParcel("duecento")
        self.assertIsNone(d.getParcel())

    def test_isAValidDoctor(self):
        d = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        d.setAge(35)
        self.assertTrue(d.isAValidDoctor())

        d.setAge(25)
        self.assertFalse(d.isAValidDoctor())

    def test_doctorGreet(self):
        d = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        d.setAge(35)
        self.assertEqual(d.doctorGreet(), None)





class TestPaziente(unittest.TestCase):
    def test_initialization(self):
        p = Paziente("Mario", "Rossi", "12345")
        self.assertEqual(p.getName(), "Mario")
        self.assertEqual(p.getLastname(), "Rossi")
        self.assertEqual(p.getAge(), 0)
        self.assertEqual(p.getidCode(), "12345")

    def test_setIdCode(self):
        p = Paziente("Mario", "Rossi", "12345")
        p.setIdCode("67890")
        self.assertEqual(p.getidCode(), "67890")

    def test_patientInfo(self):
        p = Paziente("Mario", "Rossi", "12345")
        self.assertEqual(p.patientInfo(), None)





class TestFattura(unittest.TestCase):
    def setUp(self):
        self.valid_doctor = Dottore("Mario", "Rossi", "Cardiologo", 150.0)
        self.invalid_doctor = Dottore("Luigi", "Neri", "Pediatria", 200.0)
        self.patient1 = Paziente("Carlo", "Bianchi", "P001")
        self.patient2 = Paziente("Giulia", "Verdi", "P002")
        self.fattura_valid = Fattura(self.valid_doctor, [self.patient1, self.patient2])
        self.fattura_invalid = Fattura(self.invalid_doctor, [])

    def test_initialization_valid_doctor(self):
        self.assertEqual(self.fattura_valid.doctor.getName(), "Mario")
        self.assertEqual(self.fattura_valid.doctor.getLastname(), "Rossi")
        self.assertEqual(self.fattura_valid.fatture, 2)
        self.assertEqual(self.fattura_valid.salary, 300.0)

    def test_initialization_invalid_doctor(self):
        self.assertIsNone(self.fattura_invalid.doctor)
        self.assertIsNone(self.fattura_invalid.patients)
        self.assertIsNone(self.fattura_invalid.fatture)
        self.assertIsNone(self.fattura_invalid.salary)

    def test_getSalary(self):
        self.assertEqual(self.fattura_valid.getSalary(), 300.0)

    def test_getFatture(self):
        self.assertEqual(self.fattura_valid.getFatture(), 2)

    def test_addPatient_valid(self):
        new_patient = Paziente("Anna", "Gialli", "P003")
        message = self.fattura_valid.addPatient(new_patient)
        self.assertEqual(len(self.fattura_valid.patients), 3)
        self.assertEqual(self.fattura_valid.fatture, 3)
        self.assertIn("P003", message)

    def test_addPatient_invalid(self):
        new_patient = Paziente("Giovanni", "Verdi", "P004")
        message = self.fattura_invalid.addPatient(new_patient)
        self.assertIsNone(self.fattura_invalid.doctor)
        self.assertIsNone(self.fattura_invalid.patients)
        self.assertIsNone(self.fattura_invalid.fatture)
        self.assertIsNone(self.fattura_invalid.salary)
        self.assertIn("Non è possibile creare la classe fattura", message)


if __name__ == '__main__':
    unittest.main()
