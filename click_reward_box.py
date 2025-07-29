from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

# Appium 설정
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "실제디바이스ID"
options.automation_name = "UiAutomator2"
options.app_package = "com.cashwalk.cashwalk"
options.app_activity = ".v2.view.main.MainActivity2"
options.no_reset = True

# Appium 서버 연결
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
time.sleep(2)

pause_time = 0.1
max_clicks = 100
click_count = 0

# 요소 ID 정의
COINBOX_ID = "com.cashwalk.cashwalk:id/coinbox"
AD_CLOSE_ID = "com.cashwalk.cashwalk:id/ivClose"

AD_CLOSE_IDS = [
    "com.cashwalk.cashwalk:id/ivClose",          # 기존 ID
    "com.cashwalk.cashwalk:id/iv_ad_close_btn"   # 초기화 후 등장하는 새 ID
]

while click_count < max_clicks:
    try:
        ad_close_buttons = []
        for close_id in AD_CLOSE_IDS:
            ad_close_buttons = driver.find_elements(by="id", value=close_id)
            if ad_close_buttons:
                break  # 발견되면 중단

        if ad_close_buttons:
            btn = ad_close_buttons[0]
            bounds = btn.rect
            x = bounds['x'] + bounds['width'] // 2
            y = bounds['y'] + bounds['height'] // 2
            print("※※※ 광고 감지됨. 닫기 버튼 클릭")
            driver.execute_script("mobile: clickGesture", {"x": x, "y": y})
            time.sleep(1)
            continue

        # 2. coinbox가 화면에 존재하는지 확인
        coinboxes = driver.find_elements(by="id", value=COINBOX_ID)
        if not coinboxes:
            print("-----더 이상 리워드가 존재하지 않음. 클릭 종료.")
            break

        # 3. coinbox 클릭 (좌표 계산)
        coinbox = coinboxes[0]
        bounds = coinbox.rect
        cx = bounds['x'] + bounds['width'] // 2
        cy = bounds['y'] + bounds['height'] // 2

        driver.execute_script("mobile: clickGesture", {
            "x": cx,
            "y": cy
        })

        click_count += 1
        print(f"[{click_count}] Reward box clicked")
        time.sleep(pause_time)

    except Exception as e:
        print("※※※※ 예외 발생:", str(e))
        break

driver.quit()
print(f"총 클릭 수: {click_count}")
