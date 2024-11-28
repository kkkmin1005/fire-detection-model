import torch

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s_best.pt')

# 이미지 추론
results = model('test.png')  # 감지할 이미지 경로

# 결과 출력
results.show()  # 감지 결과를 화면에 표시

# 탐지된 객체 확인
detections = results.pandas().xyxy[0] 

# fire 클래스 감지 여부 확인
if 'fire' in detections['name'].values: 
    print("화재가 감지되었습니다!")
else:
    print("화재가 감지되지 않았습니다.")