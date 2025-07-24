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

# 클릭 좌표
reward_x = 539
reward_y = 1505
pause_time = 0.1
max_clicks = 100
click_count = 0

# 광고 닫기 버튼의 resource-id
AD_CLOSE_ID = "com.cashwalk.cashwalk:id/ivClose"

for i in range(max_clicks):
    try:
        # 광고 닫기 버튼이 화면에 나타났는지 확인
        ad_close_buttons = driver.find_elements(by="id", value=AD_CLOSE_ID)
        if ad_close_buttons:
            ad_button = ad_close_buttons[0]
            bounds = ad_button.rect
            x = bounds['x'] + bounds['width'] // 2
            y = bounds['y'] + bounds['height'] // 2

            print("❗ 광고 감지됨. 닫기 버튼 클릭 중...")
            driver.execute_script("mobile: clickGesture", {
                "x": x,
                "y": y
            })
            time.sleep(1)
            continue  # 광고 닫은 후 클릭 루프로 복귀

        # 리워드 박스 클릭
        driver.execute_script("mobile: clickGesture", {
            "x": reward_x,
            "y": reward_y
        })

        click_count += 1
        print(f"[{click_count}] Reward box clicked")
        time.sleep(pause_time)

    except Exception as e:
        print("❗ 예외 발생:", str(e))
        break

driver.quit()
print(f"총 클릭 수: {click_count}")
