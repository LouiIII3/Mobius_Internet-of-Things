1. Python-Mobius-Resource-Creation.py 설명
    - import 문: 필요한 라이브러리를 가져온다.
    - requests는 HTTP 요청을 보내기 위해 사용된다.
    - shortuuid는 고유한 식별자를 생성하기 위해 사용된다.
    - json은 JSON 데이터를 처리하기 위해 사용된다.
    
    +추가    
    - data 변수: 생성할 자원의 정보를 담고 있는 딕셔너리
    - requests.request() 함수: POST 메서드를 사용하여 Mobius 서버로 요청
    - try 블록: HTTP 요청을 보내고 응답을 처리
    - Content-Type: 요청 본문의 데이터 형식을 지정

2. ae_create.py 설명
    - serverIP 변수: Mobius 서버의 IP 주소를 할당
    - ae 변수: 새로운 자원 엔티티의 이름을 할당
    - data: 딕셔너리를 생성

3. cnt_create.py 설명
    - 변수 설정: ae는 "lamp_ae", cnt는 "COMMAND", lbl은 "findRoom1"로 설정
    - if __name__ == "__main__": 블록 안에서는 요청에 필요한 헤더를 설정
    - try 블록 : requests.request() 함수를 사용하여 POST 요청
    - 응답 출력 : print(response.text)

4. lamp.py 설명
    - send_onem2m_data(data) 함수: 데이터를 웹 서버로 전송하는 역할
    - url_send 변수: 요청을 보낼 URL이 저장 
    - read_onem2m_data() 함수: 반복적으로 호출 하여 1초마다 데이터를 읽어옴
    
