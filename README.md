# MapleChoi
메이플스토리 캐릭터 정보 크롤링 웹사이트 Maple.Choi

### 개발 환경 및 기술 스택

Python 3.6 - Django 2.2<br/>
urllib3 / urllib5 / beautifulsoup4 / psycopg2<br/>
Virtualenv<br/>
HTML · CSS · Bootstrap<br/>
PostgreSQL 9.6<br/>
Visual Studio Code<br/>

### 배포 환경

Google Cloud Platform ( GCP )<br/>
Compute Engine vCPU 1 / 0.6 GB Mem / HDD / Singapore(asia-southeast1-b)<br/>
SQL PostgreSQL Elephant DB<br/>
Debian 9 (stretch) Python 3.6<br/>
http://choi-maple.kro.kr/Choi

### Maple.Choi 기타 사항

1주일 동안 진행했던 Maple.Choi 프로젝트입니다.<br/>
친구와 함께 파이썬 Django 프레임워크 연습을 같이 하게되어 프로젝트로 진행하게되었습니다.<br/>
크롤러 부분이 비효율적으로 동작하기 때문에 수정을 하려고 생각 중이며 Django ORM을<br/>
사용하여 DB에 담고 가져오게 됩니다.<br/>
<br/>
POST 방식 중 크롤링 부분 처리 시 속도가 많이 떨어지며 Django 코드 부분과 크롤러 수정을<br/>
통해서 속도 개선을 할 수 있습니다. 기회가 된다면 AJAX 통신을 통해서 페이지 로딩없이<br/>
데이터 통신 구현을 할 계획입니다.<br/>
