import shutil
import sys
# thse is a D: drive
# total, used, free = shutil.disk_usage("D:")
total, used, free = shutil.disk_usage("/")
free_gb = free // (2**30)
# free=541542727680 bytes
# 2 to the power of 30. 1024 x 1024 x 1024

print("Free Space:", free_gb, "GB")
if free_gb < 700:
    print("Low disk space!")
sys.exit(1)