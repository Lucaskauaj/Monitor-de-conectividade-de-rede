import socket
import datetime


target_host = "127.0.0.1"  
port_range = range(20, 1025)  
log_file = "port_scan_log.txt"

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                return True
    except Exception:
        return False
    return False

def log_result(port, status):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_text = "ABERTA" if status else "FECHADA"
    log_entry = f"{timestamp} - Porta {port}: {status_text}\n"
    
    with open(log_file, "a") as file:
        file.write(log_entry)
    
    print(log_entry, end="")

if __name__ == "__main__":
    print(f"Iniciando escaneamento de portas em {target_host}...\n")
    for port in port_range:
        status = scan_port(target_host, port)
        log_result(port, status)
    print("Escaneamento concluído!")
