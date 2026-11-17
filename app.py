import csv
import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse


PROJECT_DIR = Path(__file__).resolve().parent


class RockHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_DIR), **kwargs)

    def do_GET(self):
        if urlparse(self.path).path == "/api/canciones":
            self.send_canciones()
            return

        super().do_GET()

    def send_canciones(self):
        csv_path = PROJECT_DIR / "canciones_rock.csv"
        try:
            with csv_path.open(encoding="utf-8-sig", newline="") as file:
                canciones = list(csv.DictReader(file))
            payload = json.dumps(canciones, ensure_ascii=False).encode("utf-8")
        except OSError:
            self.send_error(500, "No se pudo leer canciones_rock.csv")
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


def main():
    address = ("127.0.0.1", 8000)
    server = ThreadingHTTPServer(address, RockHandler)
    print(f"Rock Clásico está disponible en http://{address[0]}:{address[1]}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nServidor detenido.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
