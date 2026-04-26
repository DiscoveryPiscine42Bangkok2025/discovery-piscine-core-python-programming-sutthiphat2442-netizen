#!/usr/bin/env python3

def main():
    # 1. กำหนดอาเรย์ตัวเลขต้นฉบับ
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]
    
    # 2. สร้างอาเรย์ใหม่โดยบวก 2 เข้าไปในแต่ละค่า
    new_array = [x + 2 for x in original_array]
    
    # 3. แสดงผลอาเรย์ทั้งสอง
    print(f"Original array: {original_array}")
    print(f"New array: {new_array}")

if __name__ == "__main__":
    main()
