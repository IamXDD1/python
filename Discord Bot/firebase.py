import firebase_admin
import datetime
from firebase_admin import firestore
from firebase_admin import credentials

cred = credentials.Certificate("setting.json")
firebase_admin.initialize_app(cred)

firestore_client = firestore.client()

def doc_ref(_client = firestore_client, col = '', doc = ''):
    return _client.collection(col).document(doc)

def getDocuments(document, except_id):
    doc_list = firestore_client.collection(document).stream()
    result_list = []

    for doc in doc_list:
        if doc.id != except_id:
            result_list.append(doc.id)

    return result_list

def checkIDexist(discord_id):
    id_list = getDocuments('Clients', 'Discord_ID')

    for id in id_list:
        if id == discord_id:
            return True

    return False

def getCurrTime():
    now = datetime.datetime.now()
    now = now + datetime.timedelta(hours=8)

    return now.strftime('%Y/%m/%d %H:%M:%S')

def checkLoggedInExpire(discord_id):
    dic_info = doc_ref(col='Clients', doc=discord_id).get().to_dict()
    str_lastUse = dic_info['lastUse']
    time_lastUse = datetime.datetime.strptime(str_lastUse, '%Y/%m/%d %H:%M:%S')
    time_curr = datetime.datetime.now()
    time_curr = time_curr + datetime.timedelta(hours=8)
    loggedIn_expire = time_curr - datetime.timedelta(minutes=30)

    if  loggedIn_expire.year > time_lastUse.year or \
        loggedIn_expire.month > time_lastUse.month or \
        loggedIn_expire.day > time_lastUse.day or \
        loggedIn_expire.hour > time_lastUse.hour or \
        loggedIn_expire.minute > time_lastUse.minute or \
        loggedIn_expire.second > time_lastUse.second:
        return True
    else:
        return False