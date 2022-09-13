def numpad_click(driver, expression):
    for num in expression:
        if num.isdigit():
            driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_0' + num).click()
        else:
            match num:
                case '+':
                    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_add').click()
                case '-':
                    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_sub').click()
                case '*':
                    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_mul').click()
                case '/':
                    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_div').click()
                case _:
                    raise ValueError('Unknown operand')
    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_equal').click()


def clear(driver):
    driver.find_element('id', 'com.sec.android.app.popupcalculator:id/calc_keypad_btn_clear').click()
