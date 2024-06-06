import socket

class Instance:
    def __init__(self, UUID, host):
        self.UUID = UUID
        self.host = host
        self.port = int(UUID) + 8000
        self.client_socket = None

    def connect(self):
        if not self.client_socket:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))

    def Process(self, A, B, Type):
        command = str(A) + " " + str(B) + " " + Type
        print("Instance " + str(self.UUID) + ": Sending command '" + command + "' to " + self.host + ":" + str(self.port))
        try:
            self.connect()
            self.client_socket.sendall(command.encode())
            print("Instance " + str(self.UUID) + ": Command sent, waiting for response")
            result = self.client_socket.recv(1024).decode().strip()
            print("Instance " + str(self.UUID) + ": Received result '" + result + "'")
            return self.Read(result)
        except Exception as e:
            print("Instance " + str(self.UUID) + ": Error " + str(e))
            self.client_socket = None  # Reset the socket to reconnect on the next command
        finally:
            if self.client_socket:
                self.client_socket.close()
                self.client_socket = None
            print("Instance " + str(self.UUID) + ": Connection closed")

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

# Example usage
if __name__ == "__main__":
    instance = Instance(1, "localhost")
    instance.Process(10, 20, "+")
