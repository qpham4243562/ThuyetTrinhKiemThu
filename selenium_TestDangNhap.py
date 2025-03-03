from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Khởi tạo Service với đường dẫn từ ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

def run_test_case(username, password, expected_result, test_name):
    try:
        driver.get("file:///D:/Work/ThuyetTrinhKiemThu/TestDangNhap.html")  
        username_field = driver.find_element(By.ID, "username")
        password_field = driver.find_element(By.ID, "password")
        submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        username_field.clear()
        password_field.clear()
        username_field.send_keys(username)
        password_field.send_keys(password)

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
    test_cases = [
        ("admin", "12345", "Đăng nhập thành công!", "Đăng nhập với thông tin đúng"),
        ("user", "wrong", "Sai thông tin!", "Đăng nhập với thông tin sai"),
        ("", "12345", "Sai thông tin!", "Để trống username, password đúng"),
        ("admin", "", "Sai thông tin!", "Username đúng, để trống password"),
        ("", "", "Sai thông tin!", "Để trống cả username và password"),
        ("wrong", "12345", "Sai thông tin!", "Username sai, password đúng"),
        ("admin", "wrong", "Sai thông tin!", "Username đúng, password sai"),
    ]

    for username, password, expected_result, test_name in test_cases:
        run_test_case(username, password, expected_result, test_name)

finally:
    driver.quit()
    print("Đã đóng trình duyệt")