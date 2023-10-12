import selenium.webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
import subprocess
from packaging import version

"""
help(selenium)
print(selenium.__version__)
"""
########### selenium 4.0, 이상 버전에서 동작 ################
if version.parse(selenium.webdriver.__version__) > version.parse("4.0") :
    # option 설정 (브라우저 크기, 자동제어 문구 삭제, user-agent 설정 등)
    opt = selenium.webdriver.chrome.options.Options()
    opt.add_argument('--window-size=100, 200')

    opt.add_experimental_option("useAutomationExtension", False)
    opt.add_experimental_option("excludeSwitches", ["enable-automation"])

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    opt.add_argument('user-agent=' + user_agent)

    # service 설정 (크롬드라이버 설치 경로 설정, cmd창 안보이기 등)
    srv = selenium.webdriver.chrome.service.Service("c:/chromedriver/chromedriver.exe")
    srv.creation_flags = subprocess.CREATE_NO_WINDOW

    # 크롬 드라이버 시작
    driver =  selenium.webdriver.Chrome(opt, srv)
    driver.get("https://www.mss.go.kr/site/eng/main.do")

    # html body의 모든 text 정보 가져오기
    body_ele = driver.find_element("tag name", "body")
    contents = body_ele.text.split('\n')
    print(contents[:20])
else:
    print(selenium.webdriver.__version__)
