FROM ubuntu:22.04

# تثبيت الأدوات
RUN apt-get update && apt-get install -y wget tar python3 cpulimit

# تحميل xmrig
RUN wget https://xmrig.com/api/latest/xmrig-linux-static -O xmrig.tar.gz && \
    tar -xf xmrig.tar.gz && \
    mv xmrig-6.22.0/xmrig . && \
    chmod +x xmrig

# إضافة سكربت التشغيل
COPY main.py .

# أمر التشغيل
CMD ["python3", "main.py"]
