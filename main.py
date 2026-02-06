import socket, time, random, binascii, base64, json

class DiamondKernel:
    def __init__(self, encrypted_token):
        self.token = encrypted_token.replace("DIAMOND-SEC-", "")

    def decrypt_payload(self):
        try:
            # معکوس کردن مراحل رمزنگاری سایت
            b64_rev = binascii.unhexlify(self.token).decode()
            original_b64 = b64_rev[::-1]
            return json.loads(base64.b64decode(original_b64).decode())
        except: return None

    def start_tunnel(self):
        data = self.decrypt_payload()
        if not data: return print("Error: Invalid Token")
        
        # تکنیک نانو-فرگمنت + استتار در قالب پکت‌های HTTP
        target = (data['a'], int(data['p']))
        header = f"GET /stream?id={random.randint(1,999)} HTTP/1.1\\r\\nHost: {data['a']}\\r\\n\\r\\n".encode()

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(target)
            # ارسال بایت‌به‌بایت برای فریب DPI شاتل
            for b in header:
                s.send(bytes([b]))
                time.sleep(0.0001) # Nano-Wait
            print("Connected Successfully.")

if __name__ == "__main__":
    # کد لایسنس از ورودی اپلیکیشن خوانده می‌شود
    app = DiamondKernel("DIAMOND-SEC-...")
    app.start_tunnel()
