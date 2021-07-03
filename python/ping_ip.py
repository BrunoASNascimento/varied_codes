import os
import platform

current_os = platform.system().lower()
print(current_os)
if current_os == "windows":
    parameter = "-n"
else:
    parameter = "-c"

ip = "10.100.3.15"
exit_code = os.system(f"ping {ip}")
print(exit_code)
