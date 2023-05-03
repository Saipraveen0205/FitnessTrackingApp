import unittest
from appium import webdriver

class LogWorkoutTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': '9.0',
            'deviceName': 'emulator-5554',
            'app': 'path/to/your/app.apk',
            'automationName': 'UiAutomator2'
        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_log_workout(self):
        # Navigate to the "Log Workout" screen
        log_workout_button = self.driver.find_element_by_id('log_workout_button')
        log_workout_button.click()

        # Verify that the "Exercise" field is present
        exercise_field = self.driver.find_element_by_id('exercise_field')
        self.assertIsNotNone(exercise_field)

        # Select an exercise from the drop-down list
        exercise_dropdown = self.driver.find_element_by_id('exercise_dropdown')
        exercise_dropdown.click()
        exercise_option = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Bench Press"]')
        exercise_option.click()

        # Verify that the "Sets" and "Reps" fields are present
        sets_field = self.driver.find_element_by_id('sets_field')
        reps_field = self.driver.find_element_by_id('reps_field')
        self.assertIsNotNone(sets_field)
        self.assertIsNotNone(reps_field)

        # Enter a value for the "Sets" field
        sets_field.send_keys('3')

        # Enter a value for the "Reps" field
        reps_field.send_keys('10')

        # Tap the "Save" button
        save_button = self.driver.find_element_by_id('save_button')
        save_button.click()

        # Verify that the workout was saved successfully by checking that the workout appears in the user's workout history
        workout_history = self.driver.find_element_by_id('workout_history')
        workout_list = workout_history.find_elements_by_class_name('workout_item')
        self.assertNotEqual(len(workout_list), 0)

if __name__ == '__main__':
    unittest.main()
