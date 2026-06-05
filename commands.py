import discord
from discord import app_commands
import config

def setup_commands(tree: app_commands.CommandTree):
    
    @tree.command(name="ติดตั้ง", description="เปิดระบบสแปมและลิงก์ช่องนี้เข้ากับ Termux")
    async def install_cmd(interaction: discord.Interaction):
        config.target_channel_id = interaction.channel_id
        # แสดงข้อมูลบนหน้าจอ Termux แบบ Real-time
        print(f"\n[🔔 REAL-TIME] ผู้ใช้ {interaction.user} ได้เรียกใช้คำสั่ง /ติดตั้ง")
        print(f"[📍 LOCATION] ช่อง: {interaction.channel.name} (ID: {interaction.channel_id})")
        print(f"[📍 SERVER] เซิร์ฟเวอร์: {interaction.guild.name if interaction.guild else 'DM'}")
        print("---------------------------------------------")
        
        # ephemeral=True เพื่อให้เห็นเฉพาะคนกดใช้เท่านั้น
        await interaction.response.send_message("⚙️ ทำการติดตั้งและเชื่อมต่อช่องสัญญาณเรียบร้อยแล้ว!", ephemeral=True)

    @tree.command(name="หยุดติดตั้ง", description="ยกเลิกการเชื่อมต่อช่องสัญญาณ")
    async def stop_cmd(interaction: discord.Interaction):
        config.target_channel_id = None
        print("\n[⚠️ WARNING] ตัวบอทถูกสั่ง [หยุดติดตั้ง] ผ่าน Discord แล้ว")
        print("---------------------------------------------")
        await interaction.response.send_message("🚫 หยุดการติดตั้งและตัดการเชื่อมต่อเรียบร้อยแล้ว", ephemeral=True)
      
