from http.client import INTERNAL_SERVER_ERROR
import string
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from datetime import datetime, timedelta
from math import ceil

"""


시트 구성은 아래와 같습니다. (두번째 링크부터 사용, 첫번째는 익스텐션 적용용) 
 A열: URL
 B열: Domain
 C열: Result (screenshot upload)

"""
def weekOfMonth(dt):
    first_day = dt.replace(day = 1)

    adjusted_dom = (first_day.weekday()) % 7
    print(first_day.weekday())
    print(adjusted_dom, type(adjusted_dom))
    print(int(ceil(adjusted_dom/7.0) + 1))
    return int(ceil(adjusted_dom/7.0) + 1)

def getTitle():
    cur_date = datetime.today()
    
    week_index = weekOfMonth(cur_date)
    week_index = str(week_index)

    date_now = cur_date.today().date()
    
    title = date_now.strftime('%Y-%m-')
    
    title = title + '0' + week_index + '_WEB_TestSheet'
    print(week_index)
    return title

scope = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/drive'
]

JSON_NAME = 'C:\\Users\\augle\\Desktop\\develop\\bloket_autoTester\\desktop\\API_key\\blokettester-6d71cf8e2a3e.json'
credential = ServiceAccountCredentials.from_json_keyfile_name(JSON_NAME, scope)
gc = gspread.authorize(credential)
spreadsheet_url = 'https://docs.google.com/spreadsheets/d/165eWgdxoJE3tETzbdAtJylbkYxmSvTkCtCaymjAYis8/edit#gid=0'

'''
class testData:
    def __init__(self, url, domain):
        self.url = url
        self.domain = domain
'''

def getURL():
    doc = gc.open_by_url(spreadsheet_url)
    curSheet = doc.worksheet('test01')
    ULRs = curSheet.col_values('1')
    #row_data = curSheet.col_values(1)
    #range_list = curSheet.range('A2:B2')
    
    
    # for cell in range_list:
    #     print(cell.value)
    #print(row_data)
    return ULRs

def getDomain():
    doc = gc.open_by_url(spreadsheet_url)
    curSheet = doc.worksheet('test01')
    domains = curSheet.col_values('2')
    return domains

def uploadToDrive(directory, fileName):
    print('test')

getTitle()
#title = getTitle()
#urlList = getURL()