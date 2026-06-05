import discord
from discord import app_commands
import asyncio
import config
from commands import setup_commands

class SpamBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        setup_commands(self.tree)
        # ซิงค์คำสั่งแบบ Global ไปยัง Discord
        await self.tree.sync()

    async def on_ready(self):
        config.client_instance = self
        print("\n=============================================")
        print(f"🤖 บอทเข้าสู่ระบบสำเร็จและพร้อมใช้งาน! (ออนให้แล้ว)")
        print(f"🎈 ชื่อบอท: {self.user.name}")
        print(f"🆔 ID บอท: {self.user.id}")
        print("=============================================")
        print("\n👉 กรุณาไปที่ช่อง Discord ที่ต้องการ แล้วพิมพ์ /ติดตั้ง ก่อนเริ่มใช้งานฟังก์ชันอื่นๆ")

def start_discord_bot(token):
    bot = SpamBot()
    # สร้าง Loop แยกเพื่อไม่ให้ Block หน้าต่าง Terminal เมนูหลัก
    loop = asyncio.get_event_loop()
    loop.create_task(bot.start(token))
  
