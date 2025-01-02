import requests
import json

name = ""
pswd = ""
Firsttoken = ""

def ConnectToEd(username, password):
    global name, pswd, Firsttoken
    name, pswd = username, password
    headersConnection={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }
    DataConnection={
        "identifiant":username,
        "motdepasse": password,
        "isReLogin": False,
        "uuid":"",
        "fa":[],
    }
    r= requests.post("https://api.ecoledirecte.com/v3/login.awp", data={"data": json.dumps(DataConnection)}, headers=headersConnection)
    data =r.json()
    headers2={
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "X-Token": data["token"]
    }
    QueryString1={
        "verbe":"get",
        "v":"4.57.1",
    }
    dataConnection2={}
    r2 = requests.post("https://api.ecoledirecte.com/v3/connexion/doubleauth.awp", data={"data": json.dumps(dataConnection2)}, headers=headers2, params=QueryString1)
    data2=r2.json()
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
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
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
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }
    r4 = requests.post("https://api.ecoledirecte.com/v3/login.awp", data={"data": json.dumps(dataConnection4)}, headers=Headers4)
    return r4.headers["X-Token"]


def AskForNotes(Token):
    dataNotesRequest={
      "anneeScolaire": "",
    }
    headersNoteRequest={
        "X-Token" : Token,
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }
    queryStringNoteRequest={
        "verbe" : "get",
    }
    notesRequest = requests.post("https://api.ecoledirecte.com/v3/eleves/xxxx/notes.awp", data={"data": json.dumps(dataNotesRequest)}, headers=headersNoteRequest, params=queryStringNoteRequest)
    dataNotes = notesRequest.json()
    return dataNotes["data"]
