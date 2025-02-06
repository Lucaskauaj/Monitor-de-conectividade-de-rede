import time
import socket
import datetime


target_host = "8.8.8.8" 
timeout = 3  
log_file = "network_log.txt"

def check_connectivity():
    try:
        
        socket.create_connection((target_host, 53), timeout=timeout)
        return True
    except OSError:
        return False

def log_status(status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_text = "Online" if status else "Offiline"
    log_entry = f"{timestamp} - Status: {status_text}\n"
    
    with open(log_file, "a") as file:
        file.write(log_entry)
    
    print(log_entry, end="")

if __name__ == "__main__":
    print("Iniciando monitoramento da rede... (CTRL+C para sair)")
    while True:
        status = check_connectivity()
        log_status(status)
        time.sleep(10)  
