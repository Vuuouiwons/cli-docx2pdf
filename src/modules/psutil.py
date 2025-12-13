import psutil

def check_process_running(process = 'WINWORD.EXE') -> bool:
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        try:
            info = proc.info
            if info['name'] == process:
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False