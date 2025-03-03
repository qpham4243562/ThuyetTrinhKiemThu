from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def run_test_case(number1, number2, expected_result, test_name):
    try:
        driver.get("file:///D:/Work/ThuyetTrinhKiemThu/TestCongHaiSo.html")
     
        #bổ sung các trường cần kiểm thử
        submit_button.click()

        time.sleep(1)

        result = driver.find_element(By.ID, "result").text
        if result == expected_result:
            print(f"TEST PASSED: {test_name}")
        else:
            print(f"TEST FAILED: {test_name} - Expected '{expected_result}', got '{result}'")
    except Exception as e:
        print(f"TEST ERROR: {test_name} - {str(e)}")

try:
    #bổ sung các test case
    test_cases = [   
    ]

    for number1, number2, expected_result, test_name in test_cases:
        run_test_case(number1, number2, expected_result, test_name)

finally:
    driver.quit()
    print("Đã đóng trình duyệt")