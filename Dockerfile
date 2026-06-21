FROM ubuntu:22.04

# تثبيت الأدوات الضرورية
RUN apt-get update && apt-get install -y wget tar python3

# تحميل xmrig
RUN wget https://github.com/xmrig/xmrig/releases/download/v6.21.3/xmrig-6.21.3-linux-x64.tar.gz && \
    tar -xf xmrig-6.21.3-linux-x64.tar.gz && \
    mv xmrig-6.21.3/xmrig .

# إضافة السكربت الخاص بك
COPY main.py .

# أمر التشغيل
CMD ["python3", "main.py"]
