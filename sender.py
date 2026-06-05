import asyncio
import random
import string
from config import client_instance, target_channel_id

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

async def start_sending_process(count, message_text, mode):
    if not client_instance or not target_channel_id:
        print("\n[❌] เกิดข้อผิดพลาด: บอทไม่ได้ออนไลน์ หรือยังไม่ได้เลือกช่องโดยคำสั่ง /ติดตั้ง")
        return

    channel = client_instance.get_channel(int(target_channel_id))
    if not channel:
        print("\n[❌] ไม่พบช่องสัญญาณที่ระบุไว้!")
        return

    # ตั้งค่าดีเลย์ตามโหมด (n = รัว, g = แรง, a = เบา)
    if mode == 'n':
        delay = 0.1
    elif mode == 'g':
        delay = 0.5
    else:  # 'a'
        delay = 1.5

    print(f"\n🚀 เริ่มต้นทำงานส่งข้อความทั้งหมด {count} ครั้ง...")
    print("---------------------------------------------")

    for i in range(1, count + 1):
        try:
            # ครั้งที่ 1: ส่งข้อความสุ่มมั่วๆ
            random_msg = generate_random_string()
            first_msg = await channel.send(random_msg)
            
            # ครั้งที่ 2: ส่งคำสั่งตอบกลับ (Reply) ข้อความแรก และใส่ข้อความจริงที่คุณพี่เลือก
            reply_msg = await first_msg.reply(message_text)
            
            # ลบข้อความแรกทิ้งทันที เหลือไว้แค่ข้อความที่สอง
            await first_msg.delete()
            
            # แสดงสถานะบน Termux เรียงลำดับ 1, 2, 3... พร้อมเครื่องหมายติ๊กถูก ✅
            print(f"{i}. ส่งข้อความสำเร็จ ✅")
            
        except Exception as e:
            print(f"{i}. ส่งข้อความล้มเหลว ❌ (Error: {e})")
            
        await asyncio.sleep(delay)
        
    print("---------------------------------------------")
    print("✨ ทำงานตามจำนวนที่กำหนดเสร็จสิ้น!")
  
