// ==========================================
// [필수] 구글 클라우드 런 배포 후 발급받은 URL로 변경하세요!
// 예: https://bubble-sort-xxxxxx.a.run.app/bubble_sort
// ==========================================
const CLOUD_RUN_URL = 'https://YOUR_CLOUD_RUN_URL/bubble_sort'; 

/**
 * 웹 앱 접속 시 Index.html을 렌더링하여 화면에 보여줍니다.
 */
function doGet(e) {
  return HtmlService.createHtmlOutputFromFile('Index')
    .setTitle('버블 정렬 시각화')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * 클라이언트(HTML)로부터 배열을 받아 Cloud Run 서버에 전송합니다.
 * @param {Array<number>} inputArray 사용자가 입력한 숫자 배열
 */
function requestSortToServer(inputArray) {
  // HTTP POST 요청을 위한 설정
  const options = {
    'method' : 'post',
    'contentType': 'application/json',
    // 파이썬 서버의 SortRequest 모델 형식에 맞게 JSON 생성
    'payload' : JSON.stringify({ data: inputArray }),
    'muteHttpExceptions': true
  };

  try {
    // Cloud Run 서버로 요청 전송
    const response = UrlFetchApp.fetch(CLOUD_RUN_URL, options);
    const responseCode = response.getResponseCode();
    const responseText = response.getContentText();
    
    // 정상 통신 시 JSON 결과 반환
    if(responseCode === 200) {
      return JSON.parse(responseText);
    } else {
      throw new Error(`[${responseCode}] 서버 에러: ${responseText}`);
    }
  } catch(error) {
    throw new Error('서버 통신 실패: ' + error.message);
  }
}
