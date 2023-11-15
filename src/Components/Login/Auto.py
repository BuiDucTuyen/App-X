import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def follow_users(driver):
    try:
        while True:
         
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

   
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.not-following .user-actions-follow-button.js-follow-btn')))

          
            follow_buttons = driver.find_elements(By.CSS_SELECTOR, '.not-following .user-actions-follow-button.js-follow-btn')
            for button in follow_buttons:
                try:
                    button.click()
                    time.sleep(1)
                except Exception as e:
                    pass

            time.sleep(4)
    except KeyboardInterrupt:
        pass
    finally:
        driver.quit()

if __name__ == "__main__":
    driver = webdriver.Chrome()

    try:
        driver.get('https://twitter.com/Beatver136')
        follow_users(driver)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()
