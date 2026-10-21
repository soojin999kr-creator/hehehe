가볍고 안정적인 Python 3.9 슬림 버전을 사용합니다.

FROM python:3.9-slim

작업할 디렉토리를 /app으로 설정합니다.

WORKDIR /app

라이브러리 설치를 위해 requirements.txt 파일을 컨테이너로 복사합니다.

COPY requirements.txt .

pip를 이용해 필수 라이브러리를 설치합니다. (캐시 무시)

RUN pip install --no-cache-dir -r requirements.txt

나머지 모든 소스 코드를 컨테이너의 /app 디렉토리로 복사합니다.

COPY . .

구글 클라우드 런의 기본 포트인 8080을 외부로 노출합니다.

EXPOSE 8080

uvicorn 웹 서버를 구동하여 FastAPI 애플리케이션(main.py의 app)을 실행합니다.

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
