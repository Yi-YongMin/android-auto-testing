# 안드로이드 앱 자동화 테스트 (Appium)

이 프로젝트는 Appium 을 활용한 UI자동화 테스트를 위해 작성되었습니다.
결과물 -> [자동화 기초 영상 URL](https://drive.google.com/file/d/1Q5EhVsPalGPAX3cr6sZsx4P8GHSIILBt/view?usp=sharing)

## Structure

- `test_cases/`: Appium 기반 파이썬 테스트 스크립트 (준비 기간이 빠듯하여 한 가지로 대체)
- 캐시워크 첫 화면에서 elementId + resource-id를 통한 이벤트 제어와 xy좌표를 통한 이벤트 제어

### 250721(Mon)

- galaxy를 pc와 연결하고 adb shell에 진입한 뒤 , pm list packages 가 불가한 상태가 발생함.
- USB3.0을 2.0으로 바꾸고 재시도하니 해결됨. 일부 고속 포트가 문제를 발생시킨다고,,,
- adb start-server -> adb devices -> adb shell

### 250722(Tue)

- adb shell monkey -p 를 이용한 앱 실행.
- powershell에서 adb shell dumpsys activity activities > activity.txt 를 통해 현재 실행 중인 앱의 액티비티 확인.
- appium driver install uiautomator2 를 통해서 드라이버 설치
- appium inspector에서 json형식을 갖춘 뒤 session을 실행해보려 하였으나 , 환경변수 관련 문제로 인해 오류발생. ANDROID_HOME과 ANDROI_SDK_ROOT , 그리고 Path에 아래 값들 추가.
  %ANDROID_HOME%\platform-tools
  %ANDROID_HOME%\emulator
  %ANDROID_HOME%\tools
  %ANDROID_HOME%\tools\bin

- 또한 환경변수 확인을 위해서 CMD,bash,powershell에서 각기 다른 문법 사용

  > CMD: %ANDROID_HOME%  
  > Git Bash: $ANDROID_HOME  
  > PowerShell: $Env:ANDROID_HOME

- 또한 appium-doctor를 통해 문제점 확인

1. JAVA_HOME 미설정 -> openjdk17 설치 후 환경변수 설정
2. android , apkanlayzer.bat 누락 -> android studio에서 Command-line Tools (latest) 설치

여전히 Start Session 실패 상태.

### 250723(Wed)

- appium과 드라이버간 호환성 문제였던 것으로 확인.
<pre><code>npm uninstall -g appium
npm install -g appium@latest</code></pre>
- 그리고 Appium inspector에서 JSON Representation 은 하기와 같이 채우기. -> appium 버전1에서는 path에 /wd/hub로 Remote Path를 설정해야했으나 , 버전2부터는 /로 변경
<pre><code>
{
  "platformName": "Android",
  "appium:deviceName": "실제디바이스ID",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.cashwalk.cashwalk",
  "appium:appActivity": ".v2.view.main.MainActivity2",
  "appium:noReset": true
}
</code></pre>

### 250724(Thur)

- 실제로 클릭이벤트 및 광고창 닫기 자동화까지 스크립트 완성
- 한가지 알아낸 점은 실제 터치 시뮬레이션을 수행하기 때문에 ADB 명령을 전달하고 반응을 대기하는 과정에서 0.1초로 설정한 것보다 더 긴 지연이 발생함.
- 하지만 기본적인 자동화는 완성
  [자동화 기초 영상 URL](https://drive.google.com/file/d/1Q5EhVsPalGPAX3cr6sZsx4P8GHSIILBt/view?usp=sharing)

### 250727(Sun)

- 단순 xy좌표 클릭으로 coinbox 클릭이 아닌 , elementId를 통한 탐색으로 클릭.
- 만약 더 이상 리워드가 존재하지 않으면 클릭을 종료하는 로직까지 추가
