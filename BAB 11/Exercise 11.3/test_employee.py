#TANPA FIXTURE

#from employee import Employee

#def test_give_default_raise():
    #employee = Employee("Max", "Verstappen", 100000)
    #employee.give_raise()
    #assert employee.annual_salary == 105000

#def test_give_custom_raise():
    #employee = Employee("Max", "Verstappen", 100000)
    #employee.give_raise(10000)
    #assert employee.annual_salary == 110000
    
#MENGGUNAKAN FIXTURE
import pytest
from employee import Employee

@pytest.fixture
def employee():
    return Employee("Max", "Verstappen", 100000)

def test_give_default_raise(employee):
    employee.give_raise()
    assert employee.annual_salary == 105000

def test_give_custom_raise(employee):
    employee.give_raise(10000)
    assert employee.annual_salary == 110000
