import requests
import json
import time
import threading
import numpy as np

finalizado = False
xArray = np.zeros((10))
yArray = np.zeros((10))
zArray = np.zeros((10))

print(xArray)

def getInfo(numero):
    print("Requisição " + str(numero + 1) + " em andamento")

    response = requests.get("https://giroscopio.netlify.app/api/gyroData?id=1")
    jsonResponse = json.loads(response.content)
    xArray[numero] = jsonResponse["x"]
    yArray[numero] = jsonResponse["y"]
    zArray[numero] = jsonResponse["z"]
    print("Requisição " + str(numero + 1) + " finalizada")

for i in range(10):
    threading.Thread(target=getInfo, daemon=True, args=(i,)).start()
    time.sleep(0.1)

time.sleep(2)
print(xArray, yArray, zArray)