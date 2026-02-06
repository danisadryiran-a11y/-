import socket, time, requests, re, base64, json

class AutoDiamond:
    def __init__(self):
        # منابع معتبر برای استخراج آی‌پی‌های سالم شاتل و همراه اول
        self.sources = [
            "https://raw.githubusercontent.com/MatinGhanbari/v2ray-configs/main/subscriptions/filtered/subs/vless.txt"
        ]
        self.best_ip = None

    def find_best_server(self):
        print("Scanning for best server...")
        for url in self.sources:
            try:
                res = requests.get(url, timeout=5).text
                ips = re.findall(r'[0-9]+(?:\.[0-9]+){3}', res)
                if ips:
                    self.best_ip = ips[0] # انتخاب اولین آی‌پی در دسترس
                    return True
            except: continue
        return False

    def connect_with_frag(self):
        if not self.find_best_server(): return
        
        # تکنیک نانو-فرگمنت برای عبور از نت ملی
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.best_ip, 443))
            payload = b"GET / HTTP/1.1\\r\\nHost: google.com\\r\\n\\r\\n"
            for byte in payload:
                s.send(bytes([byte])) # ارسال بایت به بایت
                time.sleep(0.0001)
            print(f"Connected to {self.best_ip} successfully!")

if __name__ == "__main__":
    app = AutoDiamond()
    app.connect_with_frag()
