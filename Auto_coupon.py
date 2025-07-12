from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = "https://coupon.netmarble.com/tskgb"
pid = input("본인의 PID(회원번호)를 입력하세요 : ").strip()
# 크롬 드라이버 자동 설치
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 1)

# 사용할 쿠폰 리스트
coupon_dic = {
    1: "RINKARMA",
    2: "SECRETCODE",
    3: "777SENARE",
    4: "JJOLJACK",    
    5: "LOVESENA",

    6: "SENAREGOGO",
    8: "GOODLUCK",
    9: "SEVENVSDARK",
    10: "7777777",

    12: "SURPRISE",
    13: "THEMONTHOFSENA",
    15: "7SENASENA7",
    
    16: "INTOTHESENA",
    18: "REBIRTHBACK",
    19: "WELCOMEBACK",
    
    23: "LODING",
    24: "GUILDWAR",
    25: "HEROSOMMON",
    27: "INFOCODEX",

    33: "BONVOYAGE",
    35: "INFINITETOWER",
    36: "STORYEVENT",
    37: "EVANKARIN",
    38: "SENARAID",
    39: "WELCOMESENA",

    41: "MOREKEYS",
    42: "SHOWMETHEMONEY",
    44: "MAILBOX",
    46: "RELEASEPET",
    48: "NOHOSCHRONICLE",
    49: "UPDATES",
    50: "THANKYOU",

    51: "SENAHAJASENA",
    55: "FORTAGNIA",
    56: "YUISSONG",
    57: "YONGSANIM",
    58: "PUKIDANCE",
    59: "ADVENTURER",

    62: "LEGENDSRAID",
    65: "HTRIBERANES",

    67: "TREASURE",
    68: "THEHOLYCROSS",
    69: "VALKYRIE",
    70: "LOVELYRUBY",
    
    72: "SENAEVENTS",
    73: "CMMAY",
    74: "PDKIMJUNGKI",
    75: "FUSEGETSPECIAL",
    76: "DARKKNIGHTS",
    77: "JULYSENAMONTH"
}


driver.get(url)
total = 77
i = 0
j = 0
for idx, coupon in coupon_dic.items():
    try:
        print(f"\n[{idx}] 쿠폰 처리 중: {coupon}")

        # PID 입력
        pid_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='회원번호 입력']")
        pid_input.clear()
        pid_input.send_keys(Keys.CONTROL + "a")
        pid_input.send_keys(Keys.DELETE)
        pid_input.send_keys(pid)
        time.sleep(0.8)

        # 쿠폰 입력
        coupon_input = driver.find_element(By.ID, "coupon-code")
        coupon_input.click()
        coupon_input.send_keys(Keys.CONTROL + "a")
        coupon_input.send_keys(Keys.DELETE)
        coupon_input.send_keys(coupon)
        time.sleep(0.8)

        # 사용하기 클릭
        submit_btn = driver.find_element(By.XPATH, "//button[text()='사용하기']")
        submit_btn.click()
        time.sleep(0.8)

        # 모달창에서 확인
        confirm_btn = driver.find_element(
            By.XPATH,
            '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[2]/button[2]',
        )
        confirm_btn.click()
        time.sleep(0.8)

        # 성공 분기 처리
        try:
            back_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "BackButton_text__AdLZQ")))
            print("→ 쿠폰 등록 성공")
            back_button.click()
            time.sleep(1)
            i += 1
        except:
            try:
                # 이미 등록된 경우
                confirm_btn = driver.find_element(
                    By.XPATH,
                    '//*[@id="__next"]/main/div/div[2]/div[2]/div[1]/div/div[3]/div/div/div[2]/button'
                )
                print("→ 이미 등록된 쿠폰입니다")
                j += 1
                confirm_btn.click()
                time.sleep(1)
            except Exception as e:
                print(f"❌ 예상되지 않은 모달 상태: {e}")

    except Exception as e:
        print(f"[{idx}] 처리 실패: {e}")
        continue

print(f"\n총 쿠폰 수: {total}개\n✅ {i}개 쿠폰 처리 완료\n❌ 이미 등록된 쿠폰: {j}개\n남은 쿠폰 수: {total - (i + j)}개")
driver.quit()
input("\n엔터를 누르면 종료됩니다...")
