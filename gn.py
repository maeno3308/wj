#region 메인세팅

import os
import time
#os.system('pip install --upgrade selenium')
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *
import random
from datetime import datetime, timedelta
# import pyautogui


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.relative_locator import locate_with


options = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
# user_data = "내가 원하는 경로"
options.add_argument(f"user-agent={user_agent}")
# options.add_argument(f"user-data-dir={user_data}")
options.add_experimental_option("detach", True) # 화면이 꺼지지 않고 유지

# options.add_argument("--start-maximized") # 최대 크기로 시작
# options.add_argument("--start-fullscreen") # 전체 화면(F11)으로 시작
# options.add_argument("window-size=500,500") # 화면 크기 지정
# options.add_argument("--headless") # 헤드리스 모드
# options.add_argument("--disable-gpu")
# options.add_argument("--mute-audio") # 음소거
# options.add_argument("incognito") # 시크릿 모드
# options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 불필요한 메세지 제거
# options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 자동화 메세지 제거
# service = Service(ChromeDriverManager().install())

options.add_argument('--disable-blink-features=AutomationControlled')
# navator.webdriver True 옵션 한줄로 로봇아닌 사람
headers = {'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}


############################################################################
win = tk.Tk()
win.title('GN')
win.geometry("550x700+800+100") # 창크기,위치
win.resizable(0,0)
#########################################################################


###########################################################################
def rdtime_12():
    time.sleep(random.uniform(1,2))
    return
def rdtime_23():
    time.sleep(random.uniform(2,3))
    return
###########################################################################
#endregion


#region 오늘만품절함수

def 오늘만품절 ():
    엔트리값 = 엔트리.get()
    상품명이없다면 = len(엔트리값)

    if 상품명이없다면 == 0 or 상품명이없다면 == 1 :
        showwarning('상품명오류','상품명은 두글자 이상으로 적어주세요')
    else :
        a_result = askquestion('오늘만품절',f'{엔트리값}를 오늘만품절 하시겠습니까?')
        if a_result == 'yes':
            if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
                # print('dd')
                driver = 배민로그인()
                배민_오늘만품절(driver)
                
            if tky_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 땡겨요로그인()
                땡겨요_오늘만품절(driver)
                
            if ygy_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 요기요로그인()
                요기요_오늘만품절(driver)
                
            if cp_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 쿠팡로그인()
                쿠팡_오늘만품절(driver)
                
            if gn_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 굽네로그인()
                굽네_오늘만품절(driver)
        else:
            text_box.insert('end','취소했습니다\n') #문자열마직막줄에 입력3

    return



def 배민_오늘만품절(driver):
    rdtime_23()
    배너클릭(driver)
    rdtime_23()
    ###################검색어입력
    배민검색어(driver)
    # try:
    #     # driver = webdriver.Chrome(options=options)
    #     rdtime_23()
    #     엔트리값 = 엔트리.get()
    #     검색 = driver.find_element(By.CLASS_NAME, 'css-2tifa1')
    #     rdtime_12()
    #     검색.send_keys(엔트리값)
    #     rdtime_12()
    #     검색.send_keys(Keys.ENTER)
    #     rdtime_12()     
    # except:
    #     text_box.insert('end','검색실패\n') #문자열마직막줄에 입력3

#region 오늘만품절함수

#############################배민상품 판매중선택
    판매상태 = driver.find_elements(By.CSS_SELECTOR,'.baesisi-icon.bsds-icon.css-1bu3lxy')
    판매상태[1].click()
    rdtime_23()
    판매중 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/button[2]/div[2]')
    판매중.click()
    rdtime_23()

##############################베민메뉴품절
    count = 0
    while True:
        검색된상품 = driver.find_elements(By.CSS_SELECTOR, '.menuInfo-module__p2u1')
        s_num = len(검색된상품)
        print(s_num)
        if s_num != 0:
            검색된상품[0].click()
            rdtime_23()
            품절클릭 =driver.find_elements(By.CSS_SELECTOR, '.bsds-button.css-txre6z')
            품절클릭[0].click()
            rdtime_23()

            품절클릭창닫기 =driver.find_elements(By.CSS_SELECTOR, '.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s')
            품절클릭창닫기[0].click()
            rdtime_23()    
        else:
            break
######굽네피자 품절
    매장선택 = driver.find_elements(By.CSS_SELECTOR,'.css-6vg3wo')
    매장선택[0].click()
    rdtime_23()
    굽네피자 = driver.find_elements(By.CSS_SELECTOR,'.bsds-action-sheet-item.css-1gagrh8')
    굽네피자[1].click()
    rdtime_23()

    count = 0
    while True:
        검색된상품 = driver.find_elements(By.CSS_SELECTOR, '.menuInfo-module__p2u1')
        s_num = len(검색된상품)
        if s_num != 0:
            검색된상품[0].click()
            rdtime_23()
            품절클릭 =driver.find_elements(By.CSS_SELECTOR, '.bsds-button.css-txre6z')
            품절클릭[0].click()
            rdtime_23()

            품절클릭창닫기 =driver.find_elements(By.CSS_SELECTOR, '.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s')
            품절클릭창닫기[0].click()
            rdtime_23()    
        else:
            break        

########배민원 품절
    매장선택 = driver.find_elements(By.CSS_SELECTOR,'.css-6vg3wo')
    매장선택[0].click()
    rdtime_23()
    배민1 = driver.find_elements(By.CSS_SELECTOR,'.bsds-action-sheet-item.css-1gagrh8')
    배민1[2].click()
    rdtime_23()

    count = 0
    while True:
        검색된상품 = driver.find_elements(By.CSS_SELECTOR, '.menuInfo-module__p2u1')
        s_num = len(검색된상품)
        print(s_num)
        if s_num != 0:
            검색된상품[0].click()
            rdtime_23()
            품절클릭 =driver.find_elements(By.CSS_SELECTOR, '.bsds-button.css-txre6z')
            품절클릭[0].click()
            rdtime_23()

            품절클릭창닫기 =driver.find_elements(By.CSS_SELECTOR, '.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s')
            품절클릭창닫기[0].click()
            rdtime_23()    
        else:
            break               
#endregion

#region 배민옵션품절

######배민옵션클릭과검색
    rdtime_12()
    옵션클릭 =driver.find_elements(By.CSS_SELECTOR, '.bsds-tab-item.css-1t8gcgu')
    옵션클릭[0].click()
    rdtime_23()

    옵션검색 = driver.find_element(By.CLASS_NAME, 'css-2tifa1')
    rdtime_12()
    옵션검색.send_keys('맵달')
    rdtime_23()
    옵션검색.send_keys(Keys.ENTER)
    rdtime_23()

    판매상태 = driver.find_elements(By.CSS_SELECTOR,'.baesisi-icon.bsds-icon.css-1bu3lxy')
    판매상태[1].click()
    rdtime_23()
    판매중 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/button[2]/div[2]')
    판매중.click()
    rdtime_23()

#######배민옵션품절
    count = 0
    while True:
        rdtime_12()
        품절클릭 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-12agwq6')
        품절클릭[0].click()
        rdtime_23()

        if count == 0:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        if count == 1:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        품절하기 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-bf39l8')
        품절하기[0].click()
        rdtime_23()

        try:
            최소옵션품절 = driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div[2]/button/div')
            if 최소옵션품절 != 0:
                최소옵션품절.click()
                rdtime_23()
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                count += 1
                rdtime_23()
        except:
            time.sleep(1)

############################굽네파자 옵션품절
    rdtime_12()
    매장선택 = driver.find_elements(By.CSS_SELECTOR,'.baesisi-icon.bsds-icon.css-1bu3lxy')
    매장선택[0].click()
    rdtime_23()
    굽네피자 = driver.find_elements(By.CSS_SELECTOR,'.bsds-action-sheet-item.css-1gagrh8')
    굽네피자[1].click()
    rdtime_23()
    rdtime_12()

    count = 0
    while True:
        rdtime_12()
        품절클릭 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-12agwq6')
        품절클릭[0].click()
        rdtime_23()

        if count == 0:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        if count == 1:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        품절하기 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-bf39l8')
        품절하기[0].click()
        rdtime_23()

        try:
            최소옵션품절 = driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div[2]/button/div')
            if 최소옵션품절 != 0:
                최소옵션품절.click()
                rdtime_23()
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                count += 1
                rdtime_23()
        except:
            time.sleep(1)


################################배민원옵션품절
    rdtime_23()
    매장선택 = driver.find_elements(By.CSS_SELECTOR,'.baesisi-icon.bsds-icon.css-1bu3lxy')
    매장선택[0].click()
    rdtime_23()
    배민1 = driver.find_elements(By.CSS_SELECTOR,'.bsds-action-sheet-item.css-1gagrh8')
    배민1[2].click()
    rdtime_23()

    count = 0
    while True:
        rdtime_12()
        품절클릭 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-12agwq6')
        품절클릭[0].click()
        rdtime_23()

        if count == 0:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        if count == 1:
            품절라디오 = driver.find_elements(By.CSS_SELECTOR,'.bsds-radio.css-13mzxte')
            try:
                품절라디오[count].click()
                rdtime_23()
            except:
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                break
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()

        품절하기 = driver.find_elements(By.CSS_SELECTOR,'.bsds-button.css-bf39l8')
        품절하기[0].click()
        rdtime_23()

        try:
            최소옵션품절 = driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div[2]/button/div')
            if 최소옵션품절 != 0:
                최소옵션품절.click()
                rdtime_23()
                취소하기 = driver.find_element(By.CSS_SELECTOR,'.bsds-button.css-19v7nua').click()
                count += 1
                rdtime_23()
        except:
            time.sleep(1)
    
    return
#endregion

def 땡겨요_오늘만품절(driver):
    검색어 = 엔트리.get()
    배너클릭(driver)
    rdtime_23()
##########################배너클릭후 품절페이지 이동
    try:
        품절설정 = driver.find_element(By.ID, 'mf_wfm_side_gen_menuParent_2_gen_menuSub_1_btn_child').click()
        rdtime_23()
        품절어 = driver.find_element(By.ID, 'mf_wfm_contents_wfm_tabcontents_ibx_menuSearch').send_keys(검색어)
        rdtime_23()
        검색클릭 = driver.find_element(By.ID, 'mf_wfm_contents_wfm_tabcontents_btn_search').click()
        rdtime_23()
    except:
        rdtime_12()



##################메뉴품절
    while True:
        try:
            메뉴품절 = driver.find_element(By.LINK_TEXT, '품절').click()
            rdtime_23()
            확인 = driver.find_element(By.XPATH, '//input[@value="확인"]').click()
            rdtime_23()
        except:
            rdtime_12()
            driver.execute_script("window.scrollTo(0,0)")
            rdtime_23()
            break
####################옵션선택및검색
    try:
        옵션선택클릭 = driver.find_element(By.ID, 'mf_wfm_contents_btn_optionSldot').click()
        rdtime_23()
        옵션명검색 = driver.find_element(By.ID, 'mf_wfm_contents_wfm_tabcontents_ibx_optnSearch')
        옵션명검색.send_keys(검색어)
        rdtime_23()
        옵션검색클릭 = driver.find_element(By.ID, 'mf_wfm_contents_wfm_tabcontents_btn_search').click()
        rdtime_23()
    except:
        rdtime_12()
#########################옵션품절
    try:
        while True:
            try:
                메뉴품절 = driver.find_element(By.LINK_TEXT, '품절').click()
                rdtime_23()
                while True:
                    try:
                        확인 = driver.find_element(By.XPATH, '//input[@value="확인"]').click()
                        rdtime_23()
                    except:
                        break
            except:
                break
    except:
        rdtime_12()    
    return

def 요기요_오늘만품절(driver):
    검색어 = 엔트리.get()
    배너클릭(driver)    
    #######################메뉴품절
    rdtime_23()
    try:
        검색어입력 = driver.find_element(By.NAME, value='keyword').send_keys(검색어)
        rdtime_23()
        rdtime_23()
        검색결과 = driver.find_elements(By.XPATH, '//button[@value="today"]')
        for i in 검색결과:
            i.click()
            rdtime_23()
    except:
        rdtime_12()    
        
    driver.get('https://ceo.yogiyo.co.kr/soldout/option')
    rdtime_23()
    
    ###################옵션품절
    try:
        # rdtime_12()
        # 옵션품절클릭 = driver.find_element(By.XPATH, '//*[@id="common-layout-wrapper-id"]/div[2]/div[1]/div[2]/a').click()
        rdtime_23()
        옵션품절검색 = driver.find_element(By.NAME, value='keyword').send_keys(검색어)
        rdtime_23()

        옵션품절 = driver.find_elements(By.XPATH, '//button[@value="today"]')
        for i in 옵션품절:
            i.click()
            rdtime_23()
            try:
                필수선택 = driver.find_element(By.CSS_SELECTOR, '.sc-bczRLJ.claiZC.sc-eCYdqJ.hsiXYt')
                if 필수선택 != 0:
                    필수선택.click()
                    rdtime_23()
            except:
                rdtime_12()
    except:
        rdtime_12()    

    
    return

def 쿠팡_오늘만품절(driver):
#################메뉴이동 배너닫기
    검색어 = 엔트리.get()

    driver.get('https://store.coupangeats.com/merchant/management/menu/')
    rdtime_23()
    배너클릭(driver)
    rdtime_23()
    try:
        배너닫기 = driver.find_element(By.CSS_SELECTOR, '.dialog-modal-wrapper__body--close-button').click()
        rdtime_23()
        배너닫기2 = driver.find_element(By.XPATH, '//span[text() = "확인"]').click()
        rdtime_23()        
    except:
        rdtime_12()

################################메뉴품절
    검색어입력 = driver.find_element(By.XPATH, '//input[@placeholder="검색"]').send_keys(검색어)
    rdtime_23()
    xx = 0
    while True:
        try:
            판매중 = driver.find_elements(By.CLASS_NAME, 'e7ls0530.css-1ymnf1a.ebyda14')
            판매중[xx].click()
            rdtime_23()
            오늘만품절 = driver.find_element(By.XPATH, '//li[text() = "오늘만 품절"]').click()
            rdtime_23()
            변경완료 = driver.find_element(By.XPATH, '//span[text()="변경완료"]').click()
            rdtime_23()
            xx += 1
        except:
            break

###############################옵션품절
    try:
        옵션그룹 = driver.find_element(By.XPATH, '//div[text()="옵션 그룹"]').click()
        rdtime_23()
        옵션입력 = driver.find_element(By.XPATH, '//input[@placeholder="검색"]').send_keys(검색어)
        rdtime_23()
    except:
        rdtime_12()

    xx = 1
    while True:
        try:
            판매중 = driver.find_elements(By.CSS_SELECTOR, '.css-k0likx.ebyda11')
            판매중[xx].click()
            rdtime_23()
            오늘만품절 = driver.find_element(By.XPATH, '//li[text() = "오늘만 품절"]').click()
            rdtime_23()
            xx += 1
        except:
            break


    return

def 굽네_오늘만품절(driver):
######################메뉴이동 및 배너클릭 검색
    try:
        검색어 = 엔트리.get()

        driver.get('http://office.goobne.co.kr:9494/office/menu/soldout_list')
        rdtime_23()
        배너클릭(driver)
        rdtime_23()
        판매여부 = driver.find_element(By.XPATH, '//span[text() = "선택"]').click()
        rdtime_23()
        판매 = driver.find_element(By.XPATH, '//li[text() = "판매"]').click()
        rdtime_23()    
        검색어입력 = driver.find_element(By.ID, 'search_txt').send_keys(검색어)
        rdtime_23()
        조회하기 = driver.find_element(By.XPATH, '//span[text() = "조회하기"]').click()
        rdtime_23()
        전체선택 = driver.find_element(By.ID, 'All').click()
        rdtime_23()
        선택상태변경 = driver.find_element(By.XPATH, '//span[text() = "선택 상태변경"]').click()
        rdtime_23()

    except:
        rdtime_23()


        ###########################메뉴 품절
    try:
        
        품절클릭 = driver.find_element(By.ID, 'check1').click()
        rdtime_23()
        날짜클릭 = driver.find_element(By.ID, 'datepicker').click()
        rdtime_23()
        날짜선택 = driver.find_element(By.CSS_SELECTOR, '.ui-state-default.ui-state-highlight.ui-state-hover').click() 
        rdtime_23()

        시간클릭 = driver.find_elements(By.CSS_SELECTOR, '.nice-select.selectpicker')
        시간클릭[2].click()
        rdtime_23()
        시간선택 = driver.find_element(By.XPATH, '//*[@data-value="23"]').click()
        rdtime_23()

        분클릭 = driver.find_elements(By.CSS_SELECTOR, '.nice-select.selectpicker')
        분클릭[3].click()
        rdtime_23()
        분선택 = driver.find_element(By.XPATH, '//*[@data-value="59"]').click()
        rdtime_23()

        변경완료 = driver.find_element(By.XPATH, '//button[text() = "변경완료"]').click()
        rdtime_23()

        da = Alert(driver)
        da.accept()
        rdtime_23()
        da = Alert(driver)
        da.accept()
        rdtime_23()
    except:
        rdtime_12()
    


    return

#endregion

#region 품절해제

def 품절해제 (): 
    엔트리값 = 엔트리.get()
    상품명이없다면 = len(엔트리값)

    if 상품명이없다면 == 0 or 상품명이없다면 == 1 :
        showwarning('상품명오류','상품명은 두글자 이상으로 적어주세요')
    else:
        a_result = askquestion('오늘만품절',f'{엔트리값}를 품절해제 하시겠습니까?')

        if a_result == 'yes':
            if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
                # print('dd')
                driver = 배민로그인()
                배민_품절해제(driver)
                
            if tky_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 땡겨요로그인()
                땡겨요_품절해제(driver)
            
            if ygy_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 요기요로그인()
                요기요_품절해제(driver)
                
            if cp_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 쿠팡로그인()
                쿠팡_품절해제(driver)
                    
            if gn_ck.get() == 1 : # 배민체크되어있는지 확인
                driver = 굽네로그인()
                굽네_품절해제(driver)
        else:
            text_box.insert('end','취소했습니다\n') #문자열마직막줄에 입력3
    return

def 배민_품절해제(driver):
    try:
        driver.get('https://self.baemin.com/menu')
        rdtime_23()
    except:
        rdtime_23()
    rdtime_23()
    배너클릭(driver)
    rdtime_12()



#####################배민품절 해제
    try:
        판매상태 = driver.find_element(By.XPATH, '//span[text()="판매상태"]').click()
        rdtime_23()
        품절 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-item.css-1gagrh8')
        품절[4].click() 
        rdtime_23()
        배민옵션품절해제(driver)
    except:
        rdtime_12()

##################배민피자품절해제
    try:
        가게클릭 = driver.find_elements(By.CSS_SELECTOR, '.css-6vg3wo')
        가게클릭[0].click()
        rdtime_23()
        배민피자선택 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-overlay.css-fowwyy')
        배민피자선택[3].click()
        rdtime_23()
        배민옵션품절해제(driver)
    except:
        rdtime_12()

#####################배민1 품절해제
    try:
        가게클릭 = driver.find_elements(By.CSS_SELECTOR, '.css-6vg3wo')
        가게클릭[0].click()
        rdtime_12()
        배민1선택 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-overlay.css-fowwyy')
        배민1선택[4].click()
        rdtime_23()
        배민옵션품절해제(driver)
    except:
        rdtime_12()


#####################################################################
#####################배민옵션 품절 해제
    try:

        rdtime_12()
        옵션클릭 =driver.find_elements(By.CSS_SELECTOR, '.bsds-tab-item.css-1t8gcgu')
        옵션클릭[0].click()
        rdtime_23()


        판매상태 = driver.find_element(By.XPATH, '//span[text()="판매상태"]').click()
        rdtime_23()
        품절 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-item.css-1gagrh8')
        품절[4].click() 
        rdtime_23()
        배민옵션품절해제(driver)
    except:
        rdtime_12()
###################배민피자옵션 품절해제
    try:
        가게클릭 = driver.find_elements(By.CSS_SELECTOR, '.css-6vg3wo')
        가게클릭[0].click()
        rdtime_23()
        배민피자선택 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-overlay.css-fowwyy')
        배민피자선택[3].click()
        rdtime_23()    
        배민옵션품절해제(driver)
    except:
        rdtime_12()

###################배민1옵션 품절해제
    try:
        가게클릭 = driver.find_elements(By.CSS_SELECTOR, '.css-6vg3wo')
        가게클릭[0].click()
        rdtime_12()
        배민1선택 = driver.find_elements(By.CSS_SELECTOR, '.bsds-action-sheet-overlay.css-fowwyy')
        배민1선택[4].click()
        rdtime_23()
        배민옵션품절해제(driver)
    except:
        rdtime_12()    

    return

def 땡겨요_품절해제(driver):
    rdtime_23()
    배너클릭(driver)
    rdtime_23()
###################땡겨요품절해제
    try:
        품절해제클릭 = driver.find_element(By.XPATH,'//*[text()="품절설정"]').click()
        rdtime_23()
        while True:
            품절해제 = driver.find_elements(By.LINK_TEXT,'품절해제')
            if len(품절해제) == 0:
                break
            else:
                품절해제[0].click()
                rdtime_23()

        옵션품절 = driver.find_element(By.LINK_TEXT,'옵션품절').click()
        while True:
            품절해제 = driver.find_elements(By.LINK_TEXT,'품절해제')
            if len(품절해제) == 0:
                break
            else:
                품절해제[0].click()
                rdtime_23()
                확인 = driver.find_element(By.XPATH,'//input[@value="확인"]').click()  
                rdtime_23()
                rdtime_23()
    except:
        rdtime_12()
    return

def 요기요_품절해제(driver):
###################요기요품절해제
    try:
        driver.get('https://ceo.yogiyo.co.kr/soldout/menu')
        rdtime_23()
    except:
        rdtime_23()

    rdtime_23()
    배너클릭(driver)
    rdtime_23()

    try:
        품절해제클릭 = driver.find_elements(By.XPATH,'//button[@value="sale"]')
        print(len(품절해제클릭))
        xx = 0
        for i in 품절해제클릭:
            품절해제클릭[xx].click()
            rdtime_23()
            xx += 1

        rdtime_12()
        옵션품절클릭 = driver.find_element(By.LINK_TEXT, '옵션품절').click()
        rdtime_23()
        옵션품절검색 = driver.find_element(By.NAME, value='keyword').send_keys('맵달')
        rdtime_23()  
        품절해제클릭 = driver.find_elements(By.XPATH,'//button[@value="sale"]')
        print(len(품절해제클릭))
        xx = 0
        for i in 품절해제클릭:
            품절해제클릭[xx].click()
            rdtime_23()
            xx += 1  
    except:
        rdtime_12()







    return

def 쿠팡_품절해제(driver):

#####################쿠팡 품절해제
    driver.get('https://store.coupangeats.com/merchant/management/menu/')
    rdtime_23()
    rdtime_23()
    배너클릭(driver)

################################메뉴품절
    검색어입력 = driver.find_element(By.XPATH, '//input[@placeholder="검색"]').send_keys('맵달')
    rdtime_23()
    xx = 0
    while True:
        try:
            # 판매중 = d
            오늘만품절 = driver.find_element(By.XPATH, '//div[text() = "오늘만 품절"]').click()
            rdtime_23()
            판매중 = driver.find_element(By.XPATH, '//li[text() = "판매중"]').click()
            rdtime_23()
            변경완료 = driver.find_element(By.XPATH, '//span[text()="변경완료"]').click()
            rdtime_23()
            xx += 1
        except:
            break

################################옵션품절
    검색어입력 = driver.find_element(By.XPATH, '//input[@placeholder="검색"]').send_keys('맵달')
    rdtime_23()
    xx = 0
    while True:
        try:
            오늘만품절 = driver.find_element(By.XPATH, '//div[text() = "오늘만 품절"]').click()
            rdtime_23()
            판매중 = driver.find_element(By.XPATH, '//li[text() = "판매중"]').click()
            rdtime_23()
            xx += 1
        except:
            break
        
    return


def 굽네_품절해제(driver):
    # rdtime_23()
    # 배너클릭(driver)
    # rdtime_23()
    ######################굽네홈 품절해제
    try:
        검색어 = 엔트리.get()

        driver.get('http://office.goobne.co.kr:9494/office/menu/soldout_list')
        rdtime_23()
        판매여부 = driver.find_element(By.XPATH, '//span[text() = "선택"]').click()
        rdtime_23()
        판매 = driver.find_element(By.XPATH, '//li[text() = "일시품절"]').click()
        rdtime_23()    
        검색어입력 = driver.find_element(By.ID, 'search_txt').send_keys('검색어')
        rdtime_23()
        조회하기 = driver.find_element(By.XPATH, '//span[text() = "조회하기"]').click()
        rdtime_23()
    
        조회된 = driver.find_elements(By.XPATH, '//td[contains(text(),"조회된 메뉴가")]')
        조회여부 = (len(조회된))
        print(조회여부)
        if 조회여부 != 0:
            
            전체선택 = driver.find_element(By.ID, 'All').click()
            rdtime_23()
            선택상태변경 = driver.find_element(By.XPATH, '//span[text() = "선택 상태변경"]').click()
            rdtime_23()


            판매클릭 = driver.find_element(By.ID, 'check3').click()
            rdtime_23()
            변경완료 = driver.find_element(By.XPATH, '//button[text() = "변경완료"]').click()
            rdtime_23()

            da = Alert(driver)
            da.accept()
            rdtime_23()
            da = Alert(driver)
            da.accept()
            rdtime_23()
        else:
            rdtime_12()
    except:
        rdtime_23()

    return



#endregion


#region 일시정지
def 일시정지():
    text_box.insert('end','쿠팡은 일시정지 해지가 되지않아 앱으로 이용하시기 바랍니다\n') #문자열마직막줄에 입력3
    a_result = askquestion('일시정지','운영을 중지 하겠습니까?')

    if a_result == 'yes':
        if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
            # print('dd')
            driver = 배민로그인()
            배민_일시정지(driver)
            
        if tky_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 땡겨요로그인()
            땡겨요_일시정지(driver)
            
        if ygy_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 요기요로그인()
            요기요_일시정지(driver)
            
        if cp_ck.get() == 1 : # 배민체크되어있는지 확인
            rdtime_12()
            # driver = 쿠팡로그인()
            # 쿠팡_오늘만품절(driver)
            
        if gn_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 굽네로그인()
            굽네_일시정지(driver)
    else:
        text_box.insert('end','취소했습니다\n') #문자열마직막줄에 입력3
    return

def 배민_일시정지(driver):
    #####################일시정지
    driver.get('https://self.baemin.com/shops')
    rdtime_23()
    배너클릭(driver)
    try:
        rdtime_23()
        전체영업중지 = driver.find_element(By.CSS_SELECTOR, '#btn-shop-all-suspend').click()
        rdtime_23()
        적용 = driver.find_element(By.XPATH, '//button[text()="적용"]').click()
        rdtime_23()
    except:
        rdtime_23()
    return


def 땡겨요_일시정지(driver):
    #############################영업 임시중지
    rdtime_12()
    배너클릭(driver)
    rdtime_23()
    try:
        rdtime_23()
        영업임시중지클릭 = driver.find_element(By.CSS_SELECTOR, '#mf_wfm_side_gen_menuParent_0_gen_menuSub_1_btn_child').click()
        rdtime_23()
        변경 = driver.find_element(By.XPATH,'//input[@value="변경"]').click()
        rdtime_23()
        중지 = driver.find_element(By.XPATH,'//label[text()="영업임시중지"]').click()
        rdtime_23()
        중지 = driver.find_element(By.XPATH,'//option[text()="가게사정"]').click()
        rdtime_23()
        중지 = driver.find_element(By.XPATH,'//input[@value="저장"]').click()
        rdtime_23()
        확인 = driver.find_element(By.XPATH,'//input[@value="확인"]').click()
        rdtime_23()
    except:
        rdtime_12()
    return

def 요기요_일시정지(driver):
    try:
        driver.get('https://ceo.yogiyo.co.kr/pause')
        rdtime_23()
    except:
        rdtime_23()
    배너클릭(driver)
    rdtime_23()

    try:
        시간클릭30 = driver.find_element(By.XPATH, '//div[text()="30분"]').click()
        rdtime_23()
        일시정지 = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        rdtime_23()    
    except:
        rdtime_12()
    return

def 쿠팡_일시정지(driver):
    rdtime_12()
    # 배너클릭(driver)
    # rdtime_23()
    return

def 굽네_일시정지(driver):
    rdtime_12()
    배너클릭(driver)
    rdtime_12()
    try:
        rdtime_23()
        매장관리 = driver.find_element(By.XPATH, '//span[text() = "매장 관리"]').click()
        rdtime_23()
        매장관리2 = driver.find_element(By.XPATH, '//a[text() = "매장 관리"]').click()
        rdtime_23()
        주문가능 = driver.find_element(By.XPATH, '//span[text() = "주문가능"]').click()
        rdtime_23()    
        주문불가능 = driver.find_element(By.XPATH, '//li[text() = "주문불가능"]').click()
        rdtime_23()    
        저장 = driver.find_element(By.XPATH, '//span[text() = "저장"]').click()
        rdtime_23()    
        da = Alert(driver)
        da.accept()
        rdtime_23()
        da = Alert(driver)
        da.accept()
        rdtime_23()
    except:
        rdtime_12()
    return

#endregion

#region 댓글달기
def 댓글달기():
    a_result = askquestion('댓글달기','댓글달기 하겠습니까?')
    if a_result == 'yes':
        if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
            # print('dd')
            driver = 배민로그인()
            배민_댓글달기(driver)
            
        if tky_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 땡겨요로그인()
            땡겨요_댓글달기(driver)
            
        if ygy_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 요기요로그인()
            요기요_댓글달기(driver)
            
        if cp_ck.get() == 1 : # 배민체크되어있는지 확인
            rdtime_12()
            # driver = 쿠팡로그인()
            # 쿠팡_오늘만품절(driver)
            
        if gn_ck.get() == 1 : # 배민체크되어있는지 확인
            driver = 굽네로그인()
            굽네_일시정지(driver)
    else:
        text_box.insert('end','취소했습니다\n') #문자열마직막줄에 입력3
    return

def 배민_댓글달기(driver):
    #############################배너클릭중지
    rdtime_12()
    배너클릭(driver)
    rdtime_23()

#############배민댓글달기
    try:
        driver.get('https://self.baemin.com/shops/13927279/reviews')
        rdtime_23()
    except:
        rdtime_23()
    ##############배민댓글달기
    try:
        사장님댓글달기 = driver.find_elements(By.CSS_SELECTOR,'.button.medium.secondary')
        xx = 0
        for x in 사장님댓글달기:
            사장님댓글달기[xx].click()
            rdtime_23()
            댓글창 = driver.find_elements(By.CSS_SELECTOR,'.b_lqxa9reo_12i8sxib.b_lqxa9reo_lv96zi8.b_lqxa9reo_12i8sxid')
            with open ('g_comment.txt','r',encoding='UTF8') as f:
                댓글 = f.read()
                댓글창[1].send_keys('\n')
                댓글창[1].send_keys(댓글)
                rdtime_23()
                등록 = driver.find_element(By.XPATH,'//p[text()="등록"]').click()
                rdtime_23()
            xx += 1    
    except:
        rdtime_12()
    ##############배민피자 댓글달기
    try:
        배민피자선택 = driver.find_element(By.XPATH, '//option[@value="13977001"]').click()
        rdtime_23()
        사장님댓글달기 = driver.find_elements(By.CSS_SELECTOR,'.button.medium.secondary')
        xx = 0
        for x in 사장님댓글달기:
            사장님댓글달기[xx].click()
            rdtime_23()
            댓글창 = driver.find_elements(By.CSS_SELECTOR,'.b_lqxa9reo_12i8sxib.b_lqxa9reo_lv96zi8.b_lqxa9reo_12i8sxid')
            with open ('g_comment.txt','r',encoding='UTF8') as f:
                댓글 = f.read()
                댓글창[1].send_keys('\n')
                댓글창[1].send_keys(댓글)
                rdtime_23()
                등록 = driver.find_element(By.XPATH,'//p[text()="등록"]').click()
                rdtime_23()
            xx += 1    
    except:
        rdtime_12()
##############배민원 댓글달기
    try:
        배민피자선택 = driver.find_element(By.XPATH, '//option[@value="13927284"]').click()
        rdtime_23()
        사장님댓글달기 = driver.find_elements(By.CSS_SELECTOR,'.button.medium.secondary')
        xx = 0
        for x in 사장님댓글달기:
            사장님댓글달기[xx].click()
            rdtime_23()
            댓글창 = driver.find_elements(By.CSS_SELECTOR,'.b_lqxa9reo_12i8sxib.b_lqxa9reo_lv96zi8.b_lqxa9reo_12i8sxid')
            with open ('g_comment.txt','r',encoding='UTF8') as f:
                댓글 = f.read()
                댓글창[1].send_keys('\n')
                댓글창[1].send_keys(댓글)
                rdtime_23()
                등록 = driver.find_element(By.XPATH,'//p[text()="등록"]').click()
                rdtime_23()
            xx += 1    
    except:
        rdtime_12()
    return

def 땡겨요_댓글달기(driver):
    #############################배너클릭중지
    rdtime_12()
    배너클릭(driver)
    rdtime_23()
# ##############땡겨요 댓글달기

    try:
        driver.get('https://boss.ddangyo.com/#SH0201')
        rdtime_23()
        리뷰관리클릭 = driver.find_element(By.XPATH,'//*[text()="리뷰관리"]').click()
        rdtime_23()
        rdtime_23()
    except:
        rdtime_23()

    try:
        while True:
            사장님댓글등록 = driver.find_elements(By.XPATH,'//*[@value="사장님 댓글 등록"]')
            댓글수 = len(사장님댓글등록)
            print(댓글수)
            if 댓글수 != 0:
                사장님댓글등록[0].click()
                rdtime_23()
                댓글쓰기 = driver.find_element(By.ID,'mf_wfm_contents_wfm_tabFrame_gen_generator1_0_txa_rplyCont')
                with open ('g_comment.txt','r',encoding='UTF8') as f:
                    댓글5 = f.read()
                댓글쓰기.send_keys('\n')
                time.sleep(1)
                댓글쓰기.send_keys(댓글5)
                rdtime_23()
                등록 = driver.find_element(By.XPATH,'//input[@value="등록"]').click()
                rdtime_23()
                확인 = driver.find_element(By.XPATH,'//input[@value="확인"]').click()
                rdtime_23()
            else:
                break
    except:
        rdtime_12()
    return

def 요기요_댓글달기(driver):
    #############################요기요 배너클릭
    rdtime_12()
    배너클릭(driver)
    rdtime_23()

##############요기요 댓글달기

    try:
        driver.get('https://ceo.yogiyo.co.kr/reviews')
        rdtime_23()
    except:
        rdtime_23()

    try:
        평점 = driver.find_elements(By.CSS_SELECTOR, '.Typography__StyledTypography-sc-r9ksfy-0.cknzqP')
        xx = 0
        for x in 평점:
            점수 = float(평점[xx].text)
            if 점수 >= 4.0:
                rdtime_23()
                댓글쓰기클릭 =  driver.find_elements(By.CSS_SELECTOR, '.sc-dkzDqf.cxmxbn')
                print(len(댓글쓰기클릭))
                댓글쓰기클릭[0].click()
                rdtime_23()
                댓글쓰기 = driver.find_element(By.CSS_SELECTOR, '.ReviewReply__CustomTextarea-sc-1536a88-4.efgGYK')
                with open ('g_comment.txt','r',encoding='UTF8') as f:
                    댓글5 = f.read()
                댓글쓰기.send_keys('\n')
                time.sleep(1)
                댓글쓰기.send_keys(댓글5)
                rdtime_23()
                xx += 1
            elif 점수 < 4.0:
                rdtime_23()
                댓글쓰기클릭 =  driver.find_elements(By.CSS_SELECTOR, '.sc-dkzDqf.cxmxbn')
                print(len(댓글쓰기클릭))
                댓글쓰기클릭[0].click()
                rdtime_23()
                댓글쓰기 = driver.find_element(By.CSS_SELECTOR, '.ReviewReply__CustomTextarea-sc-1536a88-4.efgGYK')
                with open ('b_comment.txt','r',encoding='UTF8') as f:
                    댓글4 = f.read()
                댓글쓰기.send_keys('\n')
                time.sleep(1)
                댓글쓰기.send_keys(댓글4)
                rdtime_23()            
                xx += 1
    except:
        rdtime_12()

    return

def 쿠팡_댓글달기(driver):
    #############################배너클릭중지
    rdtime_12()
    배너클릭(driver)
    rdtime_23()
    #############쿠팡댓글달기
    try:
        driver.get('https://store.coupangeats.com/merchant/management/reviews')
        rdtime_23()
    except:
        rdtime_23()

    try:
        사장님댓글달기 = driver.find_elements(By.XPATH, '//button[text()="사장님 댓글 등록하기"]')
        xx = 0
        for x in 사장님댓글달기:
            사장님댓글달기[xx].click()
            with open ('g_comment.txt','r',encoding='UTF8') as f:
                댓글 = f.read()
                time.sleep(1)
                댓글쓰기 = driver.find_element(By.XPATH,'//textarea[@name="review"]')
                rdtime_23()
                댓글쓰기.send_keys('\n')
                댓글쓰기.send_keys(댓글)
                rdtime_23()
                등록 = driver.find_element(By.XPATH,'//span[text()="등록"]').click()
            xx += 1
            rdtime_23()

    except:
        rdtime_12()    
    return

#endregion


#region 여러가지수행함수

def 배민검색어(driver):
    try:
        rdtime_23()
        엔트리값 = 엔트리.get()
        검색 = driver.find_element(By.CLASS_NAME, 'css-2tifa1')
        rdtime_12()
        검색.send_keys(엔트리값)
        rdtime_12()
        검색.send_keys(Keys.ENTER)
        rdtime_12()     
    except:
        text_box.insert('end','검색실패\n') #문자열마직막줄에 입력3
    return


def 배민옵션품절해제(driver):
    driver.maximize_window()
    rdtime_12()
    try:
        while True:
            dddd = driver.find_element(By.XPATH,'//*[text()="품절 해제"]')
            dx = '품절 해제'
            if dddd.text != dx:
                break
            else:
                sclick = driver.find_element(locate_with(By.CSS_SELECTOR,".bsds-button.css-a2ehx").near(dddd)).click()
                rdtime_23()
    except:
        rdtime_12()     
    return       

def 대행중지():

    if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
        if 선택콤보.get() == '오늘만품절' :


            배민로그인()
            # bamin_soldout()
            # print(b_id)
            # print(b_pw)
    return

def 대행개시():

    if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
        if 선택콤보.get() == '오늘만품절' :


            배민로그인()
            # bamin_soldout()
            # print(b_id)
            # print(b_pw)
    return

def 배달비올리기():

    if bamin_ck.get() == 1 : # 배민체크되어있는지 확인
        if 선택콤보.get() == '오늘만품절' :


            배민로그인()
            # bamin_soldout()
            # print(b_id)
            # print(b_pw)
    return




def 배너클릭(driver):
    with open("banner.txt","r",encoding="UTF8") as f:
        banner = f.readlines()
        banner = [line.rstrip('\n') for line in banner]
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[0]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[1]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[2]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[3]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[4]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[5]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[6]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[7]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[8]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    try:
        배너클릭 = driver.find_element(By.CSS_SELECTOR, banner[9]).click()
        time.sleep(2)
    except:
        time.sleep(0.3)
    return driver        

def 임시():
    time.sleep(1)
    return

#endregion


#region 로그인함수
def 배민로그인():
    driver = webdriver.Chrome(options=options)

    f = open ('idpw.txt','r',encoding='UTF8')
    bid_pw = f.readlines()
    bid_pw = [line.rstrip('\n') for line in bid_pw]

    driver.get('https://biz-member.baemin.com/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2F')
    rdtime_23()
    try:
        b_ids = driver.find_element(By.NAME, value="id")
        b_ids.send_keys(bid_pw[1])
        rdtime_12()

        b_pws = driver.find_element(By.NAME, value="password")
        b_pws.send_keys(bid_pw[2])
        rdtime_12()
        rdtime_12()


        로그인클릭 = driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-1cxc4dz-0.hlLPsc").click()
        time.sleep(2)
        rdtime_23()
        driver.get('https://self.baemin.com/menu')
        rdtime_12()
        text_box.insert('end','배민로그인성공\n')
        rdtime_23()
    except:
        text_box.insert('end','배민로그인실패\n')
    
    # try:
    #     배너값1 = f'.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s' #xpath 1일간보지않기
    #     배너창닫기1 = driver.find_elements(By.CSS_SELECTOR, value=배너값1)
            
    #     if 배너창닫기1 != 0:
    #         배너창닫기1[0].click()
    #         text_box.insert('end','배너클릭성공\n') #문자열마직막줄에 입력3
    # except:
    #     # print('배너를 못찾음')
    #     text_box.insert('end','배너클릭실패\n') #문자열마직막줄에 입력3
    
    return driver

def 땡겨요로그인():
    driver = webdriver.Chrome(options=options)
    rdtime_12()
    driver.get('https://boss.ddangyo.com/')
    rdtime_23()
    rdtime_12()
    땡_아이디 = driver.find_element(By.CLASS_NAME, 'w2input')
    rdtime_12()
    땡_아이디.send_keys('maeno3308')
    rdtime_23()
    땡_비번 = driver.find_element(By.ID, value='mf_sct_pwd')
    rdtime_12()
    땡_비번.send_keys('@kwj300560011*')
    rdtime_23()
    로그인클릭 = driver.find_element(By.ID, 'mf_wq_uuid_34')
    로그인클릭.click()
    rdtime_23()
    rdtime_23()
    return driver

def 요기요로그인():
    driver = webdriver.Chrome(options=options)
    driver.get('https://ceo.yogiyo.co.kr/login')
    rdtime_12()
    rdtime_23()
    try:
        요_아이디 = driver.find_element(By.NAME, value='username').send_keys('maeno3308')
        rdtime_23()
        요_비번 = driver.find_element(By.NAME, value='password').send_keys('@kwj300560011*')
        rdtime_23()
        로그인클릭 = driver.find_element(By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/form/button/div').click()
        rdtime_23()
        rdtime_23()
    except:
        rdtime_12()
    return driver

def 쿠팡로그인():
########################쿠팡로그인
    try:
        driver = webdriver.Chrome(options=options)
        driver.get('https://store.coupangeats.com/merchant/login')
        rdtime_23()
        rdtime_23()

        f = open ('idpw.txt','r',encoding='UTF8')
        bid_pw = f.readlines()
        bid_pw = [line.rstrip('\n') for line in bid_pw]
        # print(bid_pw[10])
        # print(bid_pw[11])
        쿠_아이디 = driver.find_element(By.ID, 'loginId').send_keys(bid_pw[10])
        rdtime_23()
        쿠_비번 = driver.find_element(By.ID, value='password').send_keys(bid_pw[11])
        rdtime_23()

        로그인클릭 = driver.find_element(By.TAG_NAME, 'button').click()
        rdtime_23()
        rdtime_23()
    except:
        rdtime_12()
    return driver

def 굽네로그인():
    #################굽네홈 로그인
    try:
        driver = webdriver.Chrome(options=options)
        rdtime_23()
        f = open ('idpw.txt','r',encoding='UTF8')
        bid_pw = f.readlines()
        bid_pw = [line.rstrip('\n') for line in bid_pw]
        print(bid_pw[13])
        print(bid_pw[14])
        driver.get('http://office.goobne.co.kr:9494/office/')
        rdtime_23()
        rdtime_23()
        매장관리자 = driver.find_element(By.XPATH, '//*[text() = "매장관리자"]').click()
        rdtime_23()
        굽_아이디 = driver.find_element(By.ID, 'userid').send_keys(bid_pw[13])
        rdtime_23()
        굽_비번 = driver.find_element(By.ID, value='passwd').send_keys(bid_pw[14])
        rdtime_23()
        로그인클릭 = driver.find_element(By.ID, 'lgnact').click()
        rdtime_23()
    except:
        rdtime_12()
    return driver

def 카카오로그인():
    # driver = webdriver.Chrome(service=service,options=options)
    driver = webdriver.Chrome(options=options)

    f = open ('ip.txt','r')
    b_id = f.readlines(0)
    b_pw = f.readlines(1)
    # f.close()
    driver.get('https://biz-member.baemin.com/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2F')
    rdtime_12()
    
    b_ids = driver.find_element(By.NAME, value="id")
    rdtime_12()
    b_ids.send_keys(b_id)

    b_pws = driver.find_element(By.NAME, value="password")
    rdtime_12()
    b_pws.send_keys(b_pw)
    rdtime_12()
    return

#endregion


#region 윈도우 tkinter 사용

bamin_ck = tk.IntVar()
배민체크 = tk.Checkbutton(win, text='배 민', variable=bamin_ck)
# 배민체크.select()
배민체크.place(x=10, y=10)


tky_ck = tk.IntVar()
땡겨요체크 = tk.Checkbutton(win, text='땡겨요', variable=tky_ck)
# 땡겨요체크.select()
땡겨요체크.place(x=80, y=10)

ygy_ck = tk.IntVar()
요기요체크 = tk.Checkbutton(win, text='요기요', variable=ygy_ck)
요기요체크.select()
요기요체크.place(x=150, y=10)


cp_ck = tk.IntVar()
쿠팡체크 = tk.Checkbutton(win, text='쿠 팡', variable=cp_ck)
# 쿠팡체크.select()
쿠팡체크.place(x=220, y=10)


gn_ck = tk.IntVar()
굽네홈 = tk.Checkbutton(win, text='굽네홈', variable=gn_ck)
# 굽네홈.select()
굽네홈.place(x=290, y=10)

# kko_ck = tk.IntVar()
# 카카오체크 = tk.Checkbutton(win, text='카카오', variable=kko_ck)
# # 카카오체크.select()
# 카카오체크.place(x=360, y=10)


상황안내 = tk.Label(win, text='오늘만품절 상품명', width=15)
상황안내.place(x=30,y=60)

엔트리  = tk.Entry(win, width=20)
엔트리.insert(0, '맵달')
엔트리.place(x=150,y=60)

오늘만품절 = tk.Button(win, width =12, height=2,text='오늘만품절',command=오늘만품절)
오늘만품절.place(x=300,y=48)

품절해제 = tk.Button(win, width =12, height=2,text='품절해제',command=품절해제)
품절해제.place(x=420,y=48)
# 선택콤보 = ttk.Combobox(win, width=20, state='readonly')
# 선택콤보 ['values'] = ['선택하세요','일시중지','댓글달기','배달비올리기','배달비내리기']
# 선택콤보.current(0)
# 선택콤보.place(x=20,y=150)

# 시작 = tk.Button(win, width =10, height=2,text='시 작',command=임시)
# 시작.place(x=200,y=140)


일시정지 = tk.Button(win, width =10, height=2,text='일시정지',command=일시정지)
일시정지.place(x=20,y=150)

일시정지해제 = tk.Button(win, width =10, height=2,text='일시정지해제',command=일시정지)
일시정지해제.place(x=120,y=150)

댓글달기 = tk.Button(win, width =10, height=2,text='댓글달기',command=임시)
댓글달기.place(x=220,y=150)

# 배달비올리기 = tk.Button(win, width =10, height=2,text='배달비올리기',command=임시)
# 배달비올리기.place(x=220,y=150)


# 배달비기본 = tk.Button(win, width =10, height=2,text='배달비기본',command=임시)
# 배달비기본.place(x=320,y=150)


text_box  = tk.Text(win, width=70, height=25)
text_box.place(x=20,y=200)
# with open ('notice.txt','r',encoding='UTF8') as f:
#     notice = f.read()
#     text_box.insert('end', notice)




선택콤보 = ttk.Combobox(win, width=10, state='readonly')
선택콤보 ['values'] = ['요일선택','일시중지','댓글달기','대행중지','대행개시']
선택콤보.current(0)
선택콤보.place(x=20,y=550)



아이디_비번 = tk.Button(win, width =15, height=2,text='아이디_비번',command=임시)
아이디_비번.place(x=20,y=640)

댓글 = tk.Button(win, width =15, height=2,text='댓 글',command=임시)
댓글.place(x=150,y=640)

발주하기 = tk.Button(win, width =15, height=2,text='발주하기(창)',command=임시)
발주하기.place(x=280,y=640)

오늘매출 = tk.Button(win, width =15, height=2,text='오늘매출',command=임시)
오늘매출.place(x=410,y=640)

win.mainloop()
#endregion



