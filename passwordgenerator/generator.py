import random 
import string

def password_strenght(pw):
    score = 0
    if any(c.islower() for c in pw): score += 1
    if any(c.isupper() for c in pw): score += 1
    if any(c.isdigit() for c in pw): score += 1
    if any(c in string.punctuation for c in pw): score += 1
    if len(pw) >= 12: score += 1
    if score <= 2:
        return "ZAYIF ❌"
    elif score <= 4:
        return "ORTA ⚠️"
    else:
        return "GÜÇLÜ 💪"
        
def generate_password():
    length = int(input("şifre uzunluğu: "))
    chars = string.ascii_letters + string.digits + string.punctuation
    pw = "".join(random.choice(chars) for _ in range(length))
    print("\nşifre:", pw)
    print("Güç:", password_strenght(pw))
    
while True:
    print("\n- şifre oluştur")
    print("0- çıkış")
    secim = input("seçim: ")
    
    if secim == "1":
        generate_password()
    elif secim == "0":
        break
    else:
        print("Yanlış seçim!")