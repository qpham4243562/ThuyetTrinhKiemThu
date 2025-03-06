# Hướng dẫn Cài Đặt và Chạy Test

## Cài đặt

1. Cài đặt Python
2. Cài đặt selenium và webdriver-manager:
   ```
   pip install selenium webdriver-manager
   ```
3. Chỉ tới đúng mục trong file bằng cách dùng đường dẫn tuyệt đối
4. Chạy và hiện kết quả:
   ```
   python <tenfile.py>
   ```

## Test case của bài tập 2:

- Cộng hai số dương, kết quả đúng phép cộng
- Cộng hai số 0, kết quả bằng 0
- Cộng hai số âm, kết quả là đúng phép cộng 
- Để trống cả hai số, kết quả là tổng là 0 
- Số thứ nhất dương, số thứ hai 0, kết quả ra số thứ nhất
- Số thứ nhất 0, số thứ hai dương, kết quả ra số thứ 2
- Số thứ nhất âm, số thứ hai dương, kết quả ra số âm 

### Ví dụ:
```
(5, 3, "Tổng: 8", "Cộng hai số dương")
```
### Làm xong gửi file python