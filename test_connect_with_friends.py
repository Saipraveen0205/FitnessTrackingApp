import unittest
from appium import webdriver

class ConnectWithFriendsTest(unittest.TestCase):

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

    def test_connect_with_friends(self):
        # Navigate to the "Connect with Friends" screen
        connect_with_friends_button = self.driver.find_element_by_id('connect_with_friends_button')
        connect_with_friends_button.click()

        # Verify that the user's friend list is displayed
        friend_list = self.driver.find_element_by_id('friend_list')
        self.assertIsNotNone(friend_list)

        # Select a friend to view their profile
        friend_profile_button = friend_list.find_element_by_class_name('friend_profile_button')
        friend_profile_button.click()

        # Verify that the friend's profile is displayed
        friend_profile = self.driver.find_element_by_id('friend_profile')
        self.assertIsNotNone(friend_profile)

        # Send a message to the friend
        message_button = friend_profile.find_element_by_id('message_button')
        message_button.click()
        message_field = self.driver.find_element_by_id('message_field')
        message_field.send_keys('Hey, great job on your progress!')
        send_button = self.driver.find_element_by_id('send_button')
        send_button.click()

        # Verify that the message was sent successfully
        sent_messages = self.driver.find_element_by_id('sent_messages')
        message_list = sent_messages.find_elements_by_class_name('message_item')
        self.assertNotEqual(len(message_list), 0)

        # Go back to the friend list
        back_button = self.driver.find_element_by_id('back_button')
        back_button.click()

        # Select another friend to view their profile
        friend_profile_button = friend_list.find_elements_by_class_name('friend_profile_button')[1]
        friend_profile_button.click()

        # Verify that the friend's profile is displayed
        friend_profile = self.driver.find_element_by_id('friend_profile')
        self.assertIsNotNone(friend_profile)

        # Like the friend's progress update
        like_button = friend_profile.find_element_by_id('like_button')
        like_button.click()

        # Verify that the like was recorded
        liked_updates = self.driver.find_element_by_id('liked_updates')
        update_list = liked_updates.find_elements_by_class_name('update_item')
        self.assertNotEqual(len(update_list), 0)
        
if __name__ == '__main__':
    unittest.main()
