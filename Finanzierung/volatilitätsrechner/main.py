import json
import pprint
import requests

def getHistory():
  with open('history.json', 'r') as f:
    file = f.read()
    history = json.loads(file)
    return history
  
def saveHistory(history, entry, newCache):
  for i in range(len(history)):
    if history[i]['api'] == entry['api']:
      history[i]['cache'] = newCache
      history[i]['cached'] = True    
      with open('history.json', 'w', encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
      break

def getCacheFromHistory(entry):
  with open('history.json', 'r') as f:
    history = json.loads(f.read())
    for i in range(len(history)):
      if history[i]['api'] == entry['api']:
        return history[i]['cache']
    return None

def isCached(entry):
  if(entry['cached'] == True):
    return True
  else:
    return False

def fetchRequest(request):
  response = requests.get(request)
  responseData = json.loads(response.text)
  return responseData

def averageVolatility(data):
  dataKeys = list(data.keys())

  totalVolatility = 0
  lastCloseValue = 0
  todayCloseValue = 0

  for key in dataKeys:    
    if key.startswith('2024') or key.startswith('2023') or key.startswith('2022'):
      # continue with the rest of the code
      lastCloseValue = todayCloseValue
      todayCloseValue = float(data[key]['4. close'])
      if lastCloseValue != 0:
        volatility = todayCloseValue / lastCloseValue

        if volatility < 1:
          volatility = 1 - volatility
        else:
          volatility -= 1

        if volatility < 0:
          print(f"Volatility: {volatility}")

        totalVolatility += volatility
    else:
      continue

  averageVolatility = totalVolatility / len(dataKeys)

  return averageVolatility

def getData():
  historyData = getHistory()
  for entry in historyData:
    entryData = entry['cache']
    if not isCached(entry):
      response = fetchRequest(entry['api'])
      saveHistory(historyData, entry, response["Time Series (Daily)"])
      entryData = response["Time Series (Daily)"]

    volatility = averageVolatility(entryData)

    entry['volatility'] = volatility
    
    saveHistory(historyData, entry, entryData)

def outpoutData():
  historyData = getHistory()

  companies = []
  for entry in historyData:
    companies.append({
      'name': entry['name'],
      'volatility': f"{round(entry['volatility'] * 100, 2)} %"
    })

  companies.sort(key=lambda x: x['volatility'], reverse=True)

  return companies

def main():
  # Get Data
  # getData()

  # Output Data
  data = outpoutData()
  pprint.pprint(data)

if __name__ == "__main__":
  main()