
import os
import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
# user_data = "내가 원하는 경로"

options.add_argument(f"user-agent={user_agent}")



# options.add_argument(f"user-data-dir={user_data}")

options.add_experimental_option("detach", True) # 화면이 꺼지지 않고 유지

options.add_argument('--disable-blink-features=AutomationControlled')
# navator.webdriver True

def rdtime_12():
    time.sleep(random.uniform(1,2))
    return
def rdtime_23():
    time.sleep(random.uniform(2,3))
    return

###########################################################################


# def bamin_sold():
#     # driver = webdriver.Chrome(service=service,options=options)
#     driver = webdriver.Chrome(options=options)

#     # f = open ('ip.txt','r')
#     # b_id = f.readlines(0)
#     # b_pw = f.readlines(1)
#     # f.close()

#     rdtime_12()

#     driver.get('https://biz-member.baemin.com/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2F')
#     rdtime_12()

#     b_ids = driver.find_element(By.NAME, value="id")
#     rdtime_12()
#     b_ids.send_keys('maeno3308')
#     rdtime_12()
#     b_pws = driver.find_element(By.NAME, value="password")
#     rdtime_12()
#     b_pws.send_keys('@kwj300560011*704')

    
#     rdtime_12()
#     driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-1cxc4dz-0.hlLPsc").click()

#     rdtime_12()

#     driver.get('https://self.baemin.com/menu')
#     rdtime_12()
#     time.sleep(3)



#     banner = driver.find_element(By.XPATH, value='/html/body/div[4]/div/section/footer/button[2]/div')
#     banner.click()

#     rdtime_12()
    
# #################################### 검색
#     bsold = driver.find_element(By.CLASS_NAME, value='css-2tifa1')
#     rdtime_12()
#     bsold.send_keys('파스')
#     rdtime_12()
#     bsold.send_keys(Keys.ENTER)

#     rdtime_12()


# ####################### 품절버튼
#     rdtime_12()

#     품절수 = driver.find_elements(By.CSS_SELECTOR, value='.franchiseMenuList-module__bBee')
#     # for i in 품절수:
#         ####품절
#         # rdtime_12()
#         # i.click()
#         # rdtime_12()
#         # 품절하기 = driver.find_elements(By.CLASS_NAME, value='bsds-button.css-txre6z')
#         # 품절하기[2].click()
#         # rdtime_12()
#         # time.sleep(3)
#         # 창닫기 = driver.find_element(By.CSS_SELECTOR, value='.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s').click()
#         # rdtime_23()
#         # time.sleep(3)


#     상점선택 = driver.find_element(By.CSS_SELECTOR, value='.css-6vg3wo').click()
#     rdtime_23()
#     피자 = driver.find_elements(By.CSS_SELECTOR, value='.bsds-action-sheet-item.css-1gagrh8')
#     피자[1].click()
#     rdtime_23()


#     # 피자품절 = driver.find_elements(By.CSS_SELECTOR, value='.franchiseMenuList-module__bBee')
#     # for p in 피자품절:
#     #     rdtime_12()
#     #     p.click()
#     #     rdtime_12()
#     #     품절하기 = driver.find_elements(By.CLASS_NAME, value='bsds-button.css-txre6z')
#     #     품절하기[2].click()
#     #     rdtime_12()
#     #     time.sleep(3)
#     #     창닫기 = driver.find_element(By.CSS_SELECTOR, value='.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s').click()
#     #     rdtime_23()
#     #     time.sleep(3)   




#     상점선택 = driver.find_element(By.CSS_SELECTOR, value='.css-6vg3wo').click()
#     rdtime_23()
#     # 피자 = driver.find_elements(By.CSS_SELECTOR, value='.bsds-action-sheet-item.css-1gagrh8')
#     피자[2].click()

#     rdtime_23()
#     배민1품절 = driver.find_elements(By.CSS_SELECTOR, value='.franchiseMenuList-module__bBee')
#     for b1 in 배민1품절:
#         rdtime_12()
#         b1.click()
#         rdtime_12()
#         품절하기 = driver.find_elements(By.CLASS_NAME, value='bsds-button.css-txre6z')
#         품절하기[2].click()
#         rdtime_12()
#         time.sleep(3)
#         창닫기 = driver.find_element(By.CSS_SELECTOR, value='.bsds-icon-button.bsds-modal-header-button.css-1sh9h6s').click()
#         rdtime_23()
#         time.sleep(3)   





#     return






#     rdtime_12()






#     # how_window = driver.window_handles

#     # print(len(how_window))


#     # iframe_e = driver.find_element(By.id, value=)
#     # driver.switch_to.frame(iframe_e)





#     # for i in how_window:
#     #     if i != how_window[0]:
#     #         driver.switch_to.window(i)
#     #         driver.close()

#     # driver.switch_to.window(how_window[0])

            




#     # driver.quit


def bamin_op():
    driver = webdriver.Chrome(options=options)
    rdtime_12()

    driver.get('https://biz-member.baemin.com/login?returnUrl=https%3A%2F%2Fceo.baemin.com%2F')
    rdtime_12()

    b_ids = driver.find_element(By.NAME, value="id")
    rdtime_12()
    b_ids.send_keys('maeno3308')
    rdtime_12()
    b_pws = driver.find_element(By.NAME, value="password")
    rdtime_12()
    b_pws.send_keys('@kwj300560011*704')

    
    rdtime_12()
    driver.find_element(By.CLASS_NAME, "Button__StyledButton-sc-1cxc4dz-0.hlLPsc").click()

    rdtime_12()

    driver.get('https://self.baemin.com/menu')
    rdtime_12()
    time.sleep(3)



    # banner = driver.find_element(By.XPATH, value='/html/body/div[4]/div/section/footer/button[2]/div')
    # banner.click()

    # 창닫기2 = driver.find_element(By.CSS_SELECTOR, value='.c_lphytuw9_1utdzds5').click()

    rdtime_12()
    
#################################### 검색
    옵션클릭 = driver.find_elements(By.CSS_SELECTOR, value='.bsds-tab-item-overlay.css-fowwyy')
    # xxx = len(옵션클릭)
    # print(f'{xxx}  리스트갯수')
    옵션클릭[1].click()
    rdtime_12()
    
    검색 = driver.find_element(By.CLASS_NAME, 'css-2tifa1')
    rdtime_12()
    검색.send_keys('파스')
    rdtime_12()
    검색.send_keys(Keys.ENTER)
    rdtime_12()

    옵션상품 = driver.find_elements(By.CSS_SELECTOR, value='.bsds-typography-text16.franchiseOptionInfo-module__IzC8.css-12314f8')
    xxx = len(옵션상품)
    print(f'옵션상품은 {xxx} 입니다')
    rdtime_12()
    옵션상품[0].click()
    time.sleep(3)
    # 옵션품절클릭 = driver.find_elements(By.CSS_SELECTOR, value='.bsds-button.css-11bhmr4')
    # zzz = len(옵션품절클릭)
    # print(f'옵션상품은 {zzz} 입니다')
    # rdtime_12()
    # 옵션품절클릭[0].click()


    rdtime_12()
    옵션창닫기 = driver.find_elements(By.CSS_SELECTOR, value='.button-overlay.css-fowwyy')
    print(len(옵션창닫기))
    옵션창닫기[5].click()

    # for op in 옵션상품:
        




    return




bamin_op()


