import requests
import json
import codecs

def sonIki(lst,kpn):
    if kpn[-2:] in lst[2]:
        return 1
    else:
        return 0

def sonUc(lst,kpn):
    if kpn[-3:] in lst[2]:
        return 1
    else:
        return 0

def sonDort(lst,kpn):
    if kpn[-4:] in lst[2]:
        return 1
    else:
        return 0

def sonBes(lst,kpn):
    if kpn[-5:] in lst[2]:
        return 1
    else:
        return 0

def sonAlti(lst,kpn):
    if kpn[-6:] in lst[2]:
        return 1
    else:
        return 0

def amorti(lst,kpn):
    if kpn[6:] in lst[2]:
        return 1
    else:
        return 0

def teselli(lst,kpn):
    if kpn in lst[2]:
        return 1
    else:
        return 0

def sonYedi(lst,kpn):
    if kpn in lst[2]:
        return 1
    else:
        return 0

def conn(kpn,dt):
    #kpn = '1111111'
    #dt = '20191231'
    #kpn = input("Kupon numarası giriniz: ") 

    resultURL = "http://www.mpi.gov.tr/sonuclar/cekilisler/piyango/"+dt+".json"
    dateURL = "http://www.mpi.gov.tr/sonuclar/listCekilisleriTarihleri.php?tur=piyango&_dc"

    # sending get request and saving the response as response object 
    r = requests.get(url = resultURL, verify=False) 
    rr = requests.get(url = dateURL, verify=False) 
    
    # extracting data in json format 
    dataReusltUrl = r.json() 

    dates=codecs.decode(rr.text.encode(), 'utf-8-sig')
    dataDates = json.loads(dates)
    
    #result ve dates verilerini listeye atm
    results=[]
    for i in range(10):#!Range'i tam bulmamız gerekiyor.
        results.append([dataReusltUrl["sonuclar"][i]["ikramiye"],dataReusltUrl["sonuclar"][i]["tip"],dataReusltUrl["sonuclar"][i]["numaralar"]])
    dates=[]
    for i in range(len(dataDates)):
        dates.append(dataDates[i]["tarih"])



    for i in range(len(results[:])):
        if results[i][1] == '$7_RAKAM':
            res=sonYedi(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son Yedi Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'SON_ALTI_RAKAM':
            res=sonAlti(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son Altı Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'SON_BES_RAKAM':
            res=sonBes(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son Beş Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'SON_DORT_RAKAM':
            res=sonDort(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son Dört Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'SON_UC_RAKAM':
            res=sonUc(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son Üç Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'SON_IKI_RAKAM':
            res=sonIki(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Son İki Rakam.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'AMORTI':
            res=amorti(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Amorti.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
        elif results[i][1] == 'TESELLI':
            res=teselli(results[i],kpn)
            if res == 1:
                print("Tebrikler {} TL kazandınız Teselli.".format(dataReusltUrl["sonuclar"][i]["ikramiye"]))
                break
    return [kpn,dataReusltUrl["sonuclar"][i]["ikramiye"],dates]

