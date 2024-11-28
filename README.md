## 사용법
인풋 데이터의 타입에 따라 코드가 다르게 구성되어 있음.

1. cam - 노트북의 실시간 캠을 이용해 디텍션 진행 후 fire가 감지되면 출력화면에 바운딩 박스 표시
2. video - 영상을 인풋으로 집어 넣으면 fire 감지 후 바운딩 박스를 그려 영상 반환
3. img - 이미지를 인풋으로 집어 넣으면 fire 감지 후 바운딩 박스를 그려 이미지 반환

## 실행 안될 경우 설치해야하는 라이브러리

git clone https://github.com/ultralytics/yolov5.git  
cd yolov5  
pip install -r requirements.txt  
