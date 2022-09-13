import sys
sys.path.append(r"C:\Appium\Project")
from methods import initialise
from methods import calculator

driver = initialise.create_session()


# Test addition
def test_add():
    calculator.clear(driver)
    calculator.numpad_click(driver, '15+20')
    result = driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_edt_formula')
    assert result.text == '35'


# Test Subtraction
def test_subtract():
    calculator.clear(driver)
    calculator.numpad_click(driver, '63-24')
    result = driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_edt_formula')
    assert result.text == '39'


# Test Multiplication
def test_multiply():
    calculator.clear(driver)
    calculator.numpad_click(driver, '8*9')
    result = driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_edt_formula')
    assert result.text == '72'


def test_divide():
    calculator.clear(driver)
    calculator.numpad_click(driver, '50/5')
    result = driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_edt_formula')
    assert result.text == '10'
