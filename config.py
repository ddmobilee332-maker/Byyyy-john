import os

# ตัวแปร Global สำหรับเก็บสเตตัสการทำงาน
bot_token = None
client_instance = None
target_channel_id = None  # บันทึก ID ช่องที่กด /ติดตั้ง

def clear_screen():
    os.system('clear')
  
