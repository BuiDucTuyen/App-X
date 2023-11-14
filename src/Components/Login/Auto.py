# from selenium import webdriver
# import time


# driver = webdriver.Chrome()


# driver.get('https://twitter.com/home')  


# time.sleep(60)

# try:
#     while True:

#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    
#         follow_buttons = driver.find_elements_by_css_selector('.not-following .user-actions-follow-button.js-follow-btn')
#         for button in follow_buttons:
#             try:
#                 button.click()
#                 time.sleep(1)  
#             except Exception as e:
#                 pass
#         time.sleep(4)
# except KeyboardInterrupt:
#     pass
# driver.quit()

import tweepy
import random


consumer_key = 'ugOMYByo2crEjIVafGuIJCVXD'
consumer_secret = 'XpvykA6FaG18pk3liE2gevfEVGrZFkLCndUKmJafQvsVb2bxEI'
access_token = '1723995577698885632-Qh5yDUoZ7Db3ilEIoTJayzWCroaHnU'
access_token_secret = 'LyGKjkKvsWkNyKNbAZNgkMX8rjqiFlnQcyFjcGOwClCCH'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


random_accounts = ['account1', 'account2', 'account3', 'account4', 'account5']
random.shuffle(random_accounts)

for account in random_accounts[:5]:
    try:
        api.create_friendship(screen_name=account)
        print(f"Đã theo dõi @{account}")
    except Exception as e:
        print(f"Lỗi: {e}")