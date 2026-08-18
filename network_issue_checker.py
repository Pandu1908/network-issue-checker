# Network Issue Checker 📡

import os

print("🌐 Network Issue Checker")
print("------------------------")

website = input("Enter a website to check: ")

response = os.system("ping -c 1 " + website)

if response == 0:
    print("✅ Network is working properly!")
    print("🌐 Internet connection is available.")
else:
    print("❌ Network issue detected!")
    print("📡 Please check your Wi-Fi or mobile data.")
