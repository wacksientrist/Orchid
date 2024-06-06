import socket
import os
import time

class Instance:
    def __init__(self, UUID, host):
        self.UUID = UUID
        self.host = host
        self.port = int(UUID) + 8000
        self.client_socket = None

        # Start the Java server instance
        os.system("java -Xms512m -Xmx2048m -XX:+UseG1GC Instance " + str(self.port) + " &")

    def connect(self):
        if not self.client_socket:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))

    def Process(self, A, B, Type):
        command = str(A) + " " + str(B) + " " + Type
        try:
            self.connect()
            self.client_socket.sendall((command + "\n").encode())  # Ensure the command ends with a newline
            result = self.client_socket.recv(1024).decode().strip()
            return self.Read(result)
        except Exception as e:
            self.client_socket = None  # Reset the socket to reconnect on the next command
        finally:
            if self.client_socket:
                self.client_socket.close()
                self.client_socket = None

    def Read(self, result):
        if result == "":
            return False
        elif result == "T":
            return True
        else:
            try:
                if '.' in result:
                    return float(result)
                else:
                    return int(result)
            except ValueError:
                return result
