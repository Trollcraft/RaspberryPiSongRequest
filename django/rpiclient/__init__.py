import socket
import json
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
with open("./config.json", "r") as f:
    config = json.load(f)
    config["localIP"] = get_ip()
with open("./config.json", "w") as f:
    json.dump(config, f)
with open("./playlist.json", "r") as f:
    playlist = json.load(f)

