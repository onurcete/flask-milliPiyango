import requests
import json
import codecs

def getDates():

    dateURL = "http://www.mpi.gov.tr/sonuclar/listCekilisleriTarihleri.php?tur=piyango&_dc"
    rr = requests.get(url = dateURL, verify=False) 
    #data=rr.text
    #print(data)
    #print(type(data))

    #d = json.loads(data)
    dates=codecs.decode(rr.text.encode(), 'utf-8-sig')
    data = json.loads(dates)

    dates=[]
    for i in range(len(data)):
        dates.append(data[i]["tarih"])
    
    return dates