from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image
from time import sleep

#import base64
#import io
import os

# takeScreenShot: hide element 기능 off
# Screenshot_Clipping: hide element 기능 on
if __name__ == "__main__" or __name__ == "decimal":
    import Screenshot_Clipping
    import gSheet
    
else:
    from . import Screenshot_Clipping
    from . import gSheet

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
# notion 접근 -> getUrl 케이스
driver.get('https://www.notion.so/dableglobal/bb5cd2690a5c4b279485ca8e9d3ee1f6?v=1623ed86dbff41b5b21f33a681d7bdcb')

1. 로그인
2. 해당 페이지 --> 표 데이터 수집 및 URL 리스트 생성
3. 생성된 URL 리스트로 페이지 접근 및 스크린샷 캡처

+ 노션으로 사이트 리스트업
-> 익스텐션 실행 (완료)
-> 페이지 로드 (완료)
-> 스크린샷 (풀페이지) (완료)
+ 노션에 업로드 / 구글 시트에 업로드
"""


#chromeDriver = 'C:\\Users\\augle\\Downloads\\chromedriver_win32\\chromedriver.exe'

chrome_options = Options()
options = webdriver.ChromeOptions()

# 백그라운드 실행 옵션
#options.headless = True

options.add_argument('C:\\Users\\augle\\AppData\\Local\\Google\\Chrome\\User Data')

options.add_argument('disable-infobars')
options.add_argument('User-Agent={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36}')
# 사용자 로그인 환경 설정
#options.add_argument('--user-data-dir=C:\\Users\\augle\\AppData\\Local\\Google\\Chrome\\User Data')
# 블로켓 익스텐션 포함 실행
options.add_extension('C:\\Users\\augle\\Desktop\\develop\\bloket_autoTester\\desktop\\autoCapt\\0.3.0_0.crx')
# 개발자 도구 여는 옵션
#options.add_argument('--auto-open-devtools-for-tabs')
# normal load 방식 (headless에서 fullscreen 기능 사용시 필요)
#options.page_load_strategy = 'normal'

driver = webdriver.Chrome(executable_path=r'C:\\Users\\augle\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)
driver.implicitly_wait(15)

driver.maximize_window()
scrObj = Screenshot_Clipping.Screenshot

urlList = gSheet.getURL()
domainList = gSheet.getDomain()
title = gSheet.getTitle()

for i in range(1, len(urlList)):

    driver.get(urlList[i])
    driver.implicitly_wait(15)
    sleep(15)
    resultImg = scrObj.full_Screenshot(scrObj, driver, f"C:\\Users\\augle\\Desktop\\bloket_test\\desktop\\testresults\\", domainList[i] + '.png')

driver.close()
driver.quit()