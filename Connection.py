import requests
import json
import urllib.parse

name = "" #Initialization of global vars
pswd = ""
Firsttoken = ""
id = ""
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
GTKCookie = ""

def GetGTKCookie():
    headersGTK={
        "User-Agent" : userAgent,
    }
    r = requests.get("https://api.ecoledirecte.com/v3/login.awp?gtk=1&v=4.75.0", headers=headersGTK)
    cookie_string = r.headers["Set-Cookie"]
    Firsttoken = r.headers["X-Token"]
    global GTKCookie
    GTKCookie = cookie_string.split(";")[0]
    return cookie_string.split(";")[0]


def ConnectToEd(username, password):
    global name, pswd, Firsttoken
    name, pswd = username, password
    GetGTKCookie()
    print(GTKCookie)
    headersConnection={
        "User-Agent" : userAgent,
        "Cookie" : GTKCookie,
        "X-Gtk" : GTKCookie.split("=")[1],
    }
    DataConnection={
        "identifiant":username,
        "motdepasse": password,
        "isReLogin": False,
        "uuid":"",
        "fa":[],
    }
    r= requests.post("https://api.ecoledirecte.com/v3/login.awp?v=4.75.0", data={"data": json.dumps(DataConnection)}, headers=headersConnection)
    data =r.json()
    print(data)
    if(data["token"] == ""):
        return 0 #Return 0 if the connection failed
    headers2={
        "User-Agent" : userAgent,
        "X-Token": data["token"],
        "X-Gtk" : GTKCookie.split("=")[1],
        "Cookie" : GTKCookie,
    }
    QueryString1={
        "verbe":"get",
        "v":"4.57.1",
    }
    dataConnection2={}
    r2 = requests.post("https://api.ecoledirecte.com/v3/connexion/doubleauth.awp", data={"data": json.dumps(dataConnection2)}, headers=headers2, params=QueryString1)
    data2=r2.json()
    print(data2)
    if(r2.headers["X-Token"] == ""):
        return 0 #Return 0 if the connection failed
    Firsttoken = r2.headers["X-Token"]
    return data2["data"]

def ConnectToEdPart2(answer):
    print(str(answer))
    dataConnection3={
        "choix" : answer.decode(),
    }
    queryString3={
       "verbe" : "post",
    }
    Headers3={
        "X-Token" : Firsttoken,
        "User-Agent" : userAgent,
        "X-Gtk" : GTKCookie.split("=")[1],
        "Cookie" : GTKCookie,
    }
    r3 = requests.post("https://api.ecoledirecte.com/v3/connexion/doubleauth.awp", data={"data": json.dumps(dataConnection3)}, headers=Headers3, params=queryString3)
    data3 = r3.json()
    dataConnection4={
        "identifiant":name,
        "motdepasse": pswd,
        "isReLogin": False,
        "uuid":"",
        "fa":[{
            "cn":data3["data"]["cn"],
            "cv":data3["data"]["cv"],
        }]
    }
    Headers4={
        "X-Token":r3.headers["X-Token"],
        "User-Agent" : userAgent,
        "X-Gtk" : GTKCookie.split("=")[1],
        "Cookie" : GTKCookie,

    }
    r4 = requests.post("https://api.ecoledirecte.com/v3/login.awp", data={"data": json.dumps(dataConnection4)}, headers=Headers4)
    global id
    id = r4.json()["data"]["accounts"][0]["id"]
    return r4.headers["X-Token"]


def AskForNotes(Token):
    dataNotesRequest={
      "anneeScolaire": "",
    }
    headersNoteRequest={
        "X-Token" : Token,
        "User-Agent" : userAgent,
        "X-Gtk" : GTKCookie.split("=")[1],
        "Cookie" : GTKCookie,

    }
    queryStringNoteRequest={
        "verbe" : "get",
    }
    notesRequest = requests.post(f"https://api.ecoledirecte.com/v3/eleves/{id}/notes.awp", data={"data": json.dumps(dataNotesRequest)}, headers=headersNoteRequest, params=queryStringNoteRequest)
    dataNotes = notesRequest.json()
    return dataNotes["data"]
