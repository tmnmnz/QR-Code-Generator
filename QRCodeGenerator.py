import qrcode
import os

def create_qr_code(data, filename):
    # สร้าง QR Code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    
    # สร้างภาพ QR Code
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # บันทึกภาพ QR Code เป็นไฟล์ PNG
    file_path = os.path.join("C:\\Users\\r_Yuk\\OneDrive\\Pictures\\ITClUBCard\\QRCode", filename + ".png")
    qr_img.save(file_path)

# เริ่มการสร้าง QR Code โดยให้ผู้ใช้ป้อนข้อมูลและชื่อไฟล์
while True:
    data = input("ป้อนข้อมูลสำหรับ QR Code: ")
    filename = input("ป้อนชื่อไฟล์ที่ต้องการ (โดยไม่รวมนามสกุล): ")
    
    # สร้าง QR Code
    create_qr_code(data, filename)
    
    # ถามว่าผู้ใช้ต้องการสร้าง QR Code เพิ่มอีกหรือไม่
    again = input("คุณต้องการสร้าง QR Code เพิ่มอีกหรือไม่ (y/n): ")
    if again.lower() != 'y':
        break
