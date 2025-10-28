import socket
import sys
# host is ip address for example 214.15.18.4
def check_port(host, port):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mySocket.settimeout(0.5)
    
    try:
        result = mySocket.connect_ex((host, port))
        
        if result == 0:
            print(f"Success. Port {port} on {host} is open.")
        else:
            print(f"No success. Port {port} on {host} is closed.")
            
    except socket.gaierror:
        print(f"Hostname error: Could not resolve '{host}'.")
    except socket.error as e:
        print(f"Connection error: {e}")
    finally:
        mySocket.close()

targetPort=int(1)
if __name__ == "__main__":
    
    hostIp = input("Please enter host ip address or domain (e.g., 4.2.2.4): ")
    
    try:
        while 0 < targetPort <= 65536:
            print(f"\nChecking {hostIp} on port {targetPort}...")
            check_port(hostIp, targetPort)
            targetPort+=1
    finally:
        sys.exit()