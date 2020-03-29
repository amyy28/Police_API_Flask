import requests

def police(location):
    r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address="+location+",+Bangalore,+CA&key=API_KEY")
    data = r.json()
    d = data["results"][0]["geometry"]["location"]
    li = []
    r = requests.get("https://maps.googleapis.com/maps/api/place/textsearch/json?query=police station&location="+str(d['lat'])+","+str(d['lng'])+"&radius=1000&key=API_KEY")
    data = r.json()
    listPolice = data["results"]
    for i in range(0, len(listPolice)):
        li.append(listPolice[i]["name"])
    return li