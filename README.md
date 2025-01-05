## Yolov5를 이용한 화재 감지 모델
GDG sprint challenge

## 모델 선정 이유
실시간으로 웹캠을 통해 전달 받은 데이터를 빠른 시간 내에 연산하기 위해 모델의 크기가 작은 Yolov5 선정

## 사용법
인풋 데이터의 타입에 따라 코드가 다르게 구성되어 있음.

1. cam - 노트북의 실시간 캠을 이용해 디텍션 진행 후 fire가 감지되면 출력화면에 바운딩 박스 표시
2. video - 영상을 인풋으로 집어 넣으면 fire 감지 후 바운딩 박스를 그려 영상 반환
3. img - 이미지를 인풋으로 집어 넣으면 fire 감지 후 바운딩 박스를 그려 이미지 반환

## 화재 감지시 신호 전달하는 방법
코드 내부에 if 문으로 선언된 부분중 주석으로 화제 감지라고 작성한 부분 존재  
해당 조건문 내부에 함수등을 추가하여 신호 전달 가능  

## 실행 안될 경우 설치해야하는 라이브러리

git clone https://github.com/ultralytics/yolov5.git  
cd yolov5  
pip install -r requirements.txt  

## 결과
![test](https://github.com/user-attachments/assets/ce276c8f-23cd-4388-a297-79ed81596dfd)
