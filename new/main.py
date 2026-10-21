from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import uvicorn

app = FastAPI()

# CORS 설정 (Google Apps Script 등 외부에서 원활하게 호출할 수 있도록 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 클라이언트로부터 받을 데이터 구조 정의 (Pydantic 모델)
class SortRequest(BaseModel):
    data: list[int]

# 루트 경로 확인용
@app.get("/")
def read_root():
    return {"status": "running", "message": "Bubble Sort Cloud Run Server is active!"}

# 버블 정렬 알고리즘 수행 엔드포인트
@app.post("/bubble_sort")
def bubble_sort(request: SortRequest):
    arr = list(request.data)
    n = len(arr)
    steps = []
    
    # 초기 상태 저장
    steps.append(list(arr))
    
    # 버블 정렬 수행 및 단계별 기록
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # 두 원소 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append(list(arr))
                swapped = True
        if not swapped:
            break
            
    return {
        "sorted_data": arr,
        "steps": steps,
        "complexity": "O(n^2)",
        "status": "버블 정렬 완료"
    }

# Cloud Run 필수: 환경 변수 PORT를 읽어와서 서버 구동 (기본값 8080)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
