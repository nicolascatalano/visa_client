import socket
import pyvisa

HOST = "0.0.0.0"
PORT = 5000

rm = pyvisa.ResourceManager()
resources = rm.list_resources()

if not resources:
    raise RuntimeError("No se encontraron instrumentos VISA")

print("Recursos encontrados:", resources)

inst = rm.open_resource(resources[0])
inst.timeout = 3000
inst.write_termination = '\n'
inst.read_termination = '\n'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Servidor escuchando en {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print("Conexión desde:", addr)

    try:
        data = conn.recv(4096)
        if not data:
            conn.close()
            continue

        cmd = data.decode("utf-8").strip()
        print("Comando recibido:", cmd)

        if cmd.upper().startswith("Q:"):
            scpi = cmd[2:]
            resp = inst.query(scpi)
            conn.sendall(resp.encode("utf-8"))
        elif cmd.upper().startswith("W:"):
            scpi = cmd[2:]
            inst.write(scpi)
            conn.sendall(b"OK")
        else:
            conn.sendall(b"ERROR: usar Q:comando o W:comando")

    except Exception as e:
        msg = f"ERROR: {e}"
        conn.sendall(msg.encode("utf-8"))

    finally:
        conn.close()