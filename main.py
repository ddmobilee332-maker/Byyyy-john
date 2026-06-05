import asyncio
import sys
import config
from logo import BANNER
from bot import start_discord_bot
from sender import start_sending_process

async def main_menu():
    config.clear_screen()
    # เด้งมาหน้าแรกตอนรันสำเร็จ
    print("Welcome to Termux Project Launcher")
    input("\n📥 กด [Enter] เพื่อส่งข้อมูลและเริ่มต้นรันโปรเจค...")
    
    # เด้งไปหน้าโลโก้
    config.clear_screen()
    print(BANNER)
    
    while True:
        print("\n⚡ [ เมนูคำสั่งควบคุม ] ⚡")
        print("1. oopp  - ติดตั้งและล็อค Token บอท")
        print("2. oopp2 - ตั้งค่าจำนวน คำ และโหมดความเร็วเพื่อส่งข้อความ")
        print("3. exit  - ออกจากโปรแกรม")
        
        choice = input("\nเลือกคำสั่งหลักที่ต้องการทำ: ").strip()
        
        if choice == "oopp":
            token = input("\n🔑 กรุณาใส่ Token Bot ของคุณพี่: ").strip()
            if not token:
                print("❌ Token ห้ามว่าง!")
                continue
            config.bot_token = token
            print("\n⏳ กำลังสั่งบอทให้เชื่อมต่อและออนไลน์...")
            start_discord_bot(token)
            # ให้เวลาระบบเชื่อมต่อแป๊บนึง
            await asyncio.sleep(4)
            
        elif choice == "oopp2":
            if not config.client_instance:
                print("\n❌ กรุณากดใช้คำสั่ง oopp เพื่อออนบอทก่อนค่ะ!")
                continue
            if not config.target_channel_id:
                print("\n❌ บอทออนไลน์แล้ว แต่คุณพี่ยังไม่ได้ไปกด /ติดตั้ง ในช่อง Discord เลยค่ะ!")
                continue
                
            try:
                count = int(input("\n🔢 ใส่จำนวนครั้งที่จะส่งข้อความ: ").strip())
            except ValueError:
                print("❌ กรุณาใส่เฉพาะตัวเลขเท่านั้น!")
                continue
                
            msg_text = input("✍️ ใส่ข้อความที่ต้องการส่ง (ใส่ได้ทุกรูปแบบ): ")
            
            print("\n📋 เลือกโหมดความเร็วสำหรับการทำงาน:")
            print("- [ n ] : โหมดรัว (เร็วสุดขีด ดีเลย์ 0.1 วินาที)")
            print("- [ g ] : โหมดแรง (ความเร็วระดับกลาง ดีเลย์ 0.5 วินาที)")
            print("- [ a ] : โหมดเบา (เรื่อยๆ สบายๆ ดีเลย์ 1.5 วินาที)")
            
            mode = input("👉 พิมพ์ตัวเลือก (n / g / a): ").strip().lower()
            if mode not in ['n', 'g', 'a']:
                print("❌ โหมดไม่ถูกต้อง! ระบบจะใช้โหมดเบา (a) อัตโนมัติ")
                mode = 'a'
                
            # เรียกฟังก์ชันทำงานส่งสแปมสลับลบแบบเท่ๆ
            await start_sending_process(count, msg_text, mode)
            
        elif choice == "exit":
            print("\nปิดการทำงานโปรแกรม. ขอบคุณที่ใช้บริการค่ะคุณพี่!")
            sys.exit()
        else:
            print("\n❌ คำสั่งไม่ถูกต้อง กรุณาเลือกพิมพ์ oopp หรือ oopp2")

if __name__ == "__main__":
    # เปิดใช้และรันระบบแบบ Asyncio Loop
    try:
        asyncio.run(main_menu())
    except KeyboardInterrupt:
        print("\n\nปิดการทำงานโปรแกรม.")
      
