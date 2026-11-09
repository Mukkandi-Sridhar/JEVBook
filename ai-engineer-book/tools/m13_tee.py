"""Run code/tarkika_mcp.py and log every stdin/stdout line to the file given as the first argument."""
import json
import subprocess
import sys
import threading

log = open(sys.argv[1], "a")
proc = subprocess.Popen([sys.executable, "tarkika_mcp.py"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
lock = threading.Lock()


def record(direction, line):
    with lock:
        log.write(json.dumps({"dir": direction, "msg": json.loads(line)}) + "\n")
        log.flush()


def upstream():                        # client -> server
    for line in sys.stdin.buffer:
        record("client", line)
        proc.stdin.write(line)
        proc.stdin.flush()
    proc.stdin.close()


threading.Thread(target=upstream, daemon=True).start()
for line in proc.stdout:               # server -> client
    record("server", line)
    sys.stdout.buffer.write(line)
    sys.stdout.buffer.flush()
