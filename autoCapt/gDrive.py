from googleapiclient.discovery import build 
from httplib2 import Http 
from oauth2client import file, client, tools 

scope = 'https://www.googleapis.com/auth/drive.file' 
store = file.Storage('C:\\Users\\augle\\Desktop\\develop\\bloket_autoTester\\desktop\\API_key\\storage.json') 
creds = store.get() 
JSON_NAME = 'C:\\Users\\augle\\Desktop\\develop\\bloket_autoTester\\desktop\\API_key\\bloket_drive.json'

try : 
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args() 
except ImportError: 
    flags = None 
    
if not creds or creds.invalid: 
    print('make new cred') 
    flow = client.flow_from_clientsecrets(JSON_NAME, scope)
    creds = tools.run_flow(flow, store, flags) if flags else tools.run_flow(flow, store)

DRIVE = build('drive', 'v3', http=creds.authorize(Http()))

FILES = (
    ('C:\\Users\\augle\\Desktop\\bloket_test\\desktop\\2021-06-02_WEB_TestSheet\\pixiv.net.png'),
)

for file in FILES:
    file_name = file
    metadata = {
        'name': file_name,
        'parents': ['1MGMIKq2_JoWHxjX--GTwE_O5sTqDsa6G'],
        'mimeType': None
    }
    res = DRIVE.files().create(body=metadata, media_body=file_name).execute()