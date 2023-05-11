import redis
from flask import Flask
import socket

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname) 

@app.route('/')
def ip():
    ip= IPAddr
    return f'<H1>Hostname:{hostname} IP Address {ip}</H1>' #.format(ip)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True,threaded=True)
