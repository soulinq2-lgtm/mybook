# هذا الأمر يقوم بتحميل الملف الجاهز للعمل مباشرة
RUN wget https://xmrig.com/api/latest/xmrig-linux-static -O xmrig.tar.gz && \
    tar -xf xmrig.tar.gz && \
    mv xmrig-6.22.0/xmrig . && \
    chmod +x xmrig
    
