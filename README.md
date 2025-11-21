# Automotive AI Perception Project - Lane Detection

This project implements a lane detection system using TensorFlow for automotive AI perception.

## 프로젝트 개요

차량의 전방 카메라 이미지로부터 차선을 검출하는 인공지능 모델을 학습하고 평가하는 프로젝트입니다.

## 요구사항

- Python 3.11.9 (또는 호환 버전)
- numpy 1.26.4
- tensorflow 2.15.0
- jupyter notebook

## 설치 방법

### 1. Python 환경 준비

Python 3.11.9 설치를 권장합니다. pyenv를 사용하는 경우:

```bash
pyenv install 3.11.9
pyenv local 3.11.9
```

### 2. 가상환경 생성 (권장)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 또는
venv\Scripts\activate  # Windows
```

### 3. 필요한 패키지 설치

```bash
pip install -r requirements.txt
```

## 데이터 준비

다음 데이터 파일들이 `ref/` 디렉토리에 필요합니다:
- `X_train.npz`: 훈련용 이미지 데이터
- `y_train.npz`: 훈련용 라벨 데이터 (차선 이진 맵)
- `X_test.npz`: 테스트용 이미지 데이터

데이터 파일들을 `ref/` 디렉토리에 배치하세요.

## 실행 방법

### Jupyter Notebook 실행

```bash
jupyter notebook
```

브라우저가 자동으로 열리면 `train_example.ipynb` 파일을 선택하여 실행합니다.

### 커맨드 라인에서 실행 (선택사항)

```bash
jupyter nbconvert --to notebook --execute train_example.ipynb
```

## 제출물 생성

노트북 실행 후 `submission/` 디렉토리에 다음 형식으로 결과 파일이 생성됩니다:
- `submission1.npz`
- `submission2.npz` (추가 실행시)
- ...

## 프로젝트 구조

```
.
├── train_example.ipynb   # 메인 훈련 노트북
├── ref/
│   ├── f1score.py        # F1 Score 계산 함수
│   ├── X_train.npz       # 훈련 데이터 (필요)
│   ├── y_train.npz       # 훈련 라벨 (필요)
│   └── X_test.npz        # 테스트 데이터 (필요)
├── submission/           # 제출 파일 저장 디렉토리
├── requirements.txt      # Python 패키지 의존성
└── README.md            # 본 파일
```

## 모델 설명

이 프로젝트는 CNN 기반의 U-Net 스타일 네트워크를 사용합니다:
- 인코더: Conv2D + MaxPooling2D 레이어
- 디코더: UpSampling2D + Conv2D 레이어
- 출력: 차선 이진 맵 (128x256x1)

## 평가 지표

- **F1 Score**: Precision과 Recall의 조화 평균

## 주의사항

1. X_test를 추론할 때 shuffle 하지 마세요
2. 출력 shape는 반드시 (1248, 128, 256, 1)이어야 합니다
3. 제출 파일명은 submission1.npz, submission2.npz 형식으로 관리하세요

## 문제 해결

### TensorFlow 설치 오류
- Python 버전이 TensorFlow 2.15.0과 호환되는지 확인하세요
- GPU 버전이 필요한 경우 `tensorflow-gpu==2.15.0` 사용

### 메모리 부족 오류
- 배치 크기를 줄이세요 (현재 16)
- GPU 메모리 증가 설정이 활성화되어 있는지 확인하세요

### 데이터 파일 없음
- ref/ 디렉토리에 .npz 파일들이 있는지 확인하세요
- 파일 경로가 올바른지 확인하세요
