import time
from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'Android Emulator',
    'appPackage': 'com.example.fitnessapp',
    'appActivity': 'com.example.fitnessapp.MainActivity'
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# Navigate to the library of exercises and workout plans
driver.find_element_by_id('btn_library').click()

# Scroll down to view more options
driver.swipe(0, 1000, 0, 500, 400)

# Select an exercise from the library
driver.find_element_by_xpath('//android.widget.ListView/android.widget.LinearLayout[3]').click()

# Add the exercise to a workout plan
driver.find_element_by_id('btn_add_workout_plan').click()
driver.find_element_by_id('workout_plan_name').send_keys('Monday Workout Plan')
driver.find_element_by_id('btn_add').click()

# Save the workout plan and navigate back to the main screen
driver.find_element_by_id('btn_save_workout_plan').click()
driver.find_element_by_id('btn_back').click()

# Close the app
driver.quit()
