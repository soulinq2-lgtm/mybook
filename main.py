import subprocess
import time
import os
import sys

# جلب المحفظة من متغيرات البيئة في Railway
WALLET = os.getenv("WALLET_ADDRESS")
POOL = "pool.supportxmr.com:3333"

if not WALLET:
    print("خطأ: يجب تحديد WALLET_ADDRESS في إعدادات Railway!")
    sys.exit(1)

def run_mining():
    while True:
        print("Starting mining pulse...")
        # استخدام cpulimit لتحديد القوة بـ 5% فقط
        cmd = ["cpulimit", "-l", "5", "--", "./xmrig", "-o", POOL, "-u", WALLET, "--donate-level", "1"]
        
        process = subprocess.Popen(cmd)
        
        time.sleep(60) # العمل لمدة دقيقة
        
        # إنهاء العملية بلطف
        process.terminate()
        process.wait() 
        
        print("Sleeping to avoid detection...")
        time.sleep(30) # الاستراحة لـ 30 ثانية

if __name__ == "__main__":
    run_mining()
