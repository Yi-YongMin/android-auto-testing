# 안드로이드 앱 자동화 테스트 (Appium + Jenkins)

이 프로젝트는 Appium + Jenkins 을 활용한 UI자동화 테스트를 위해 작성되었습니다.

## Structure

- `test_cases/`: Appium 기반 파이썬 테스트 스크립트
- `docs/`: 아키텍처 다이어그램과 테스트 결과 예시
- `Jenkinsfile`: CI 파이프라인 스크립트

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
  "appium:deviceName": "R3CTC0389GV",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.android.settings",
  "appium:appActivity": ".Settings",
  "appium:noReset": true
  }
</code></pre>
