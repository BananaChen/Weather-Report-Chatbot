import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WeatherReport():
    def __init__(self):
        self.options = Options()
        self.options.binary_location = '/app/.apt/usr/bin/google-chrome'
        self.options.add_argument('--headless')
        self.options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(options = self.options)
        #chromedriver = "/Users/charles/Downloads/chromedriver"
        #self.driver = webdriver.Chrome(chromedriver)
        self.soup = self.getPageSourceHtml()
        self.driver.close()

    def getPageSourceHtml(self):
        self.driver.get('https://www.cwb.gov.tw/V7/forecast/')  # 輸入範例網址，交給瀏覽器 
        pageSource = self.driver.page_source  # 取得網頁原始碼
        soup = BeautifulSoup(pageSource, "html.parser")# 轉成html element 的檔案
        return soup

    def getTemperature(self, cityId):
        city = self.soup.find("tr", {"id": cityId})
        i = 0
        for rows in city.find_all("td"):
            if (i == 1):
                return rows.string
            i += 1
        return "No data found"

    def getRainProb(self, cityId):
        city = self.soup.find("tr", {"id": cityId})
        i = 0
        for rows in city.find_all("td"):
            if (i == 2):
                return rows.string
            i += 1
        return "No data found"
    
    def tempRemind(self, temp):
        if(temp):
            return "天冷記得要保暖ㄛ"

    def rainRemind(self, rainProb):
        if(int(rainProb.split('%')[0]) < 50):
            return "sunny"
        else:
            return "rain"

    def closeDriver(self):
        self.driver.close()  # 關閉瀏覽器

    def findCityId(self, cityStr):
        if (cityStr == "基隆" or cityStr == "基隆市"):
            return "KeelungList"
        elif (cityStr == "台北" or cityStr == "台北市"):
            return "TaipeiCityList"
        elif (cityStr == "新北" or cityStr == "新北市"):
            return "TaipeiList"
        elif (cityStr == "桃園" or cityStr == "桃園市"):
            return "TaoyuanList"
        elif (cityStr == "新竹市"):
            return "HsinchuCityList"
        elif (cityStr == "新竹縣"):
            return "HsinchuList"
        elif (cityStr == "苗栗" or cityStr == "苗栗縣"):
            return "MiaoliList"
        elif (cityStr == "台中" or cityStr == "台中市"):
            return "TaichungList"
        elif (cityStr == "彰化" or cityStr == "彰化縣"):
            return "ChanghuaList"
        elif (cityStr == "南投" or cityStr == "南投縣"):
            return "NantouList"
        elif (cityStr == "雲林" or cityStr == "雲林縣"):
            return "YunlinList"
        elif (cityStr == "嘉義市"):
            return "ChiayiCityList"
        elif (cityStr == "嘉義縣"):
            return "ChiayiList"
        elif (cityStr == "宜蘭" or cityStr == "宜蘭縣"):
            return "YilanList"
        elif (cityStr == "花蓮" or cityStr == "花蓮縣"):
            return "HualienList"
        elif (cityStr == "台東" or cityStr == "台東縣"):
            return "TaitungList"
        elif (cityStr == "台南" or cityStr == "台南市"):
            return "TainanList"
        elif (cityStr == "高雄" or cityStr == "高雄市"):
            return "KaohsiungCityList"
        elif (cityStr == "屏東" or cityStr == "屏東縣"):
            return "PingtungList"
        elif (cityStr == "連江縣" or cityStr == "馬祖"):
            return "MatsuList"
        elif (cityStr == "金門" or cityStr == "金門縣"):
            return "KinmenList"
        elif (cityStr == "澎湖" or cityStr == "澎湖縣"):
            return "PenghuList"
        else:
            return False

