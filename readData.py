import requests, json, time, threading
import pandas as pd

finalizado = False
xArray = [[],[],[],[],[],[],[],[],[],[]]

def getInfo(numero):
    print("Requisição " + str(numero + 1) + " em andamento")

    response = requests.get("https://giroscopio.netlify.app/api/gyroData?id=1")
    jsonResponse = json.loads(response.content)
    xArray[numero] = [jsonResponse["x"], jsonResponse["y"], jsonResponse["z"]]
    print("Requisição " + str(numero + 1) + " finalizada")

for i in range(10):
    threading.Thread(target=getInfo, daemon=True, args=(i,)).start()
    time.sleep(0.1)

time.sleep(2)

data = pd.read_csv("testFile.csv", index_col="id", header=0)

print(data)