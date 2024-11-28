import torch
import cv2

# YOLOv5 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5s_best.pt')

# 비디오 파일 열기
cap = cv2.VideoCapture('input.mp4')  # 비디오 파일 경로

# 비디오 출력 파일 설정 (같은 해상도로 저장)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 출력 비디오 코덱 설정
out = cv2.VideoWriter('output.mp4', fourcc, 30.0, (int(cap.get(3)), int(cap.get(4))))  # 새 비디오 파일

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # BGR -> RGB 변환 (YOLOv5 모델은 RGB 이미지를 사용)
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # YOLOv5 모델로 추론
    results = model(img_rgb)  # 현재 프레임에 대한 추론

    # 탐지된 객체 확인
    detections = results.pandas().xyxy[0]  # 탐지된 결과를 Pandas DataFrame으로 반환

    # 'fire' 클래스 감지 여부 확인
    for index, row in detections.iterrows():
        if row['name'] == 'fire':
            # 'fire' 클래스가 감지된 경우, 바운딩 박스를 그립니다.
            x1, y1, x2, y2 = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  # 바운딩 박스 그리기
            cv2.putText(frame, 'Fire Detected', (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # 결과를 새로운 비디오 파일로 저장
    out.write(frame)

    # ESC 키를 눌러서 비디오 실행 중지 가능
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일 종료 후 자원 해제
cap.release()
out.release()  # 비디오 쓰기 객체 해제
cv2.destroyAllWindows()
