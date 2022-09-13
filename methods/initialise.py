from appium import webdriver


def create_session():
    desired_caps = {
        'deviceName': 'GalaxyS8+',
        'platformName': 'Android',
        'platformVersion': '9',
        'appPackage': 'com.sec.android.app.popupcalculator',
        'appActivity': 'com.sec.android.app.popupcalculator.Calculator',
    }
    # Initialize the session
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver
