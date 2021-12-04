import time
import json

start_time = time.time()

with open('input.json') as file:
	inputData = json.load(file)

units = dict.fromkeys(inputData[0]["units"], None)
#units = {key: None for key in inputData[0]["units"]}


print("--- %s seconds ---" % (time.time() - start_time))