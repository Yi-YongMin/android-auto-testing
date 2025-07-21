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
