import requests, json, time, threading, csv
import pandas as pd
import numpy as np

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

new_row_data = xArray

csv_file_path = './testFile.csv'

lineNumber = 0

with open(csv_file_path, mode='r') as file:

    reader = csv.reader(file)

    lineNumber = sum(1 for row in reader)

with open(csv_file_path, mode='a', newline='') as file:

    writer = csv.writer(file)

    writer.writerow([lineNumber] + new_row_data)