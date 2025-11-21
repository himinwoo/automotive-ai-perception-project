# train_example.ipynb 실행 가이드

이 가이드는 `train_example.ipynb` 노트북을 실행하기 위한 전체 프로세스를 설명합니다.

## 🚀 빠른 시작

실제 데이터가 있는 경우:

```bash
# 1. 환경 설정
./setup.sh

# 2. 노트북 실행
source venv/bin/activate  # Linux/Mac
jupyter notebook train_example.ipynb
```

실제 데이터가 없는 경우 (테스트용):

```bash
# 1. 환경 설정
./setup.sh

# 2. 샘플 데이터 생성
python create_sample_data.py

# 3. 환경 검증
python test_notebook.py

# 4. 빠른 테스트 (선택사항)
python quick_test.py

# 5. 노트북 실행
source venv/bin/activate  # Linux/Mac
jupyter notebook train_example.ipynb
```

## 📋 사전 요구사항

### 필수 소프트웨어
- Python 3.8 - 3.12
- pip (Python 패키지 관리자)
- Git (이미 설치됨)

### 권장 사항
- 최소 8GB RAM
- GPU가 있으면 더 빠른 훈련 가능 (선택사항)
- 충분한 디스크 공간 (데이터 파일용)

## 📦 설치 상세 가이드

### 1단계: 저장소 확인

```bash
cd /path/to/automotive-ai-perception-project
ls -la
```

다음 파일들이 있어야 합니다:
- train_example.ipynb
- requirements.txt
- setup.sh
- ref/f1score.py

### 2단계: 가상환경 생성

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3단계: 패키지 설치

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

설치되는 주요 패키지:
- numpy: 수치 계산
- tensorflow: 딥러닝 프레임워크
- jupyter: 노트북 환경
- notebook: Jupyter 노트북 인터페이스

### 4단계: 데이터 준비

#### 옵션 A: 실제 데이터 사용

`ref/` 디렉토리에 다음 파일들을 배치:
- X_train.npz (훈련 이미지)
- y_train.npz (훈련 라벨)
- X_test.npz (테스트 이미지)

#### 옵션 B: 샘플 데이터 생성 (테스트용)

```bash
python create_sample_data.py
```

⚠️ **경고**: 샘플 데이터는 실제 차선 검출 데이터가 아닙니다. 노트북 실행 테스트용으로만 사용하세요.

## 🧪 검증 및 테스트

### 환경 검증

노트북 실행 전에 모든 것이 올바르게 설정되었는지 확인:

```bash
python test_notebook.py
```

예상 출력:
```
============================================================
Testing train_example.ipynb Prerequisites
============================================================
Testing imports...
✓ All imports successful

Testing data loading...
✓ Data loading successful

Testing model creation...
✓ Model creation successful

Testing prediction shape...
✓ Prediction shape test successful

Testing submission directory...
✓ Submission directory exists

============================================================
Test Results: 5/5 passed
============================================================
```

### 빠른 실행 테스트

전체 훈련을 시작하기 전에 2 에포크로 빠른 테스트:

```bash
python quick_test.py
```

이 테스트는 다음을 확인합니다:
- 데이터 로딩
- 모델 생성
- 훈련 프로세스
- 예측 생성
- 결과 저장

## 📓 노트북 실행

### 방법 1: Jupyter Notebook UI

```bash
jupyter notebook
```

브라우저가 열리면:
1. `train_example.ipynb` 클릭
2. 각 셀을 순서대로 실행 (Shift+Enter)
3. 또는 상단 메뉴에서 "Cell > Run All" 선택

### 방법 2: 커맨드 라인 실행

```bash
jupyter nbconvert --to notebook --execute train_example.ipynb --output train_example_executed.ipynb
```

## 📊 노트북 내용 설명

### 셀 구조

1. **Import 셀**: 필요한 라이브러리 임포트
2. **Data Loading 셀**: 데이터 파일 로드
3. **Model Definition 셀**: CNN 모델 정의
4. **Training 셀**: 모델 훈련 (20 에포크)
5. **Prediction 셀**: 테스트 데이터 예측
6. **Submission 셀**: 결과 저장

### 모델 아키텍처

```
Input (128x256x3)
    ↓
Encoder (Conv + MaxPool) x3
    ↓
Bottleneck (64 filters)
    ↓
Decoder (UpSample + Conv) x3
    ↓
Output (128x256x1)
```

### 훈련 파라미터

- **Epochs**: 20
- **Batch Size**: 16
- **Optimizer**: Adam (lr=0.001)
- **Loss**: Binary Crossentropy
- **Metric**: F1 Score
- **Validation Split**: 0.2

## 💾 결과 저장

노트북 실행 후 `submission/` 디렉토리에 결과 파일이 생성됩니다:

```
submission/
└── submission1.npz    # 예측 결과
```

결과 파일은 다음 형태를 가집니다:
- Shape: (1248, 128, 256, 1)
- Type: float32
- Range: [0, 1] (sigmoid 출력)

## 🔧 문제 해결

### 일반적인 문제

#### 1. TensorFlow 설치 실패

**증상**: `ERROR: Could not find a version that satisfies the requirement tensorflow==2.15.0`

**해결책**: 
- Python 버전 확인: `python --version`
- Python 3.12인 경우 TensorFlow 2.16+ 필요
- `requirements.txt`는 이미 호환 가능한 버전 사용

#### 2. 데이터 파일 없음

**증상**: `FileNotFoundError: [Errno 2] No such file or directory: 'ref/X_train.npz'`

**해결책**:
```bash
# 샘플 데이터 생성
python create_sample_data.py

# 또는 실제 데이터를 ref/ 디렉토리에 복사
```

#### 3. 메모리 부족

**증상**: `ResourceExhaustedError` 또는 시스템이 느려짐

**해결책**:
- 배치 크기 감소: 노트북에서 `batch_size=16`을 `batch_size=8` 또는 `batch_size=4`로 변경
- 훈련 데이터 크기 축소 (샘플 데이터의 경우)

#### 4. Jupyter 실행 안 됨

**증상**: `jupyter: command not found`

**해결책**:
```bash
# 가상환경이 활성화되었는지 확인
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Jupyter 재설치
pip install --upgrade jupyter notebook
```

#### 5. GPU를 찾을 수 없음

**증상**: `Could not find cuda drivers on your machine, GPU will not be used.`

**해결책**: 이것은 경고일 뿐입니다. CPU로도 훈련 가능합니다. GPU를 사용하려면:
- CUDA 드라이버 설치
- tensorflow-gpu 설치 고려

### 디버깅 팁

1. **단계별 실행**: 노트북 셀을 하나씩 실행하여 어디서 문제가 발생하는지 확인
2. **로그 확인**: TensorFlow 경고 메시지를 주의 깊게 읽기
3. **버전 확인**: 
   ```bash
   python -c "import numpy; print(f'numpy: {numpy.__version__}')"
   python -c "import tensorflow; print(f'tensorflow: {tensorflow.__version__}')"
   ```

## 📈 성능 예상

### 훈련 시간 (샘플 데이터 100개 샘플 기준)

- **CPU**: 에포크당 ~2-3초
- **GPU**: 에포크당 ~0.5-1초
- **총 훈련 시간 (20 에포크)**: CPU에서 약 1-2분

### 실제 데이터 기준 (전체 데이터셋)

- 훈련 시간은 데이터 크기에 따라 다름
- F1 Score는 초기에 낮고 점차 증가
- 최종 F1 Score: 0.5-0.7 범위 예상

## 🎯 다음 단계

노트북 실행 후:

1. **결과 분석**: 
   - 훈련 히스토리 확인
   - Validation loss vs Training loss 비교
   - F1 Score 추이 확인

2. **모델 개선**:
   - 하이퍼파라미터 튜닝 (learning rate, batch size)
   - 모델 아키텍처 수정
   - 데이터 증강 추가

3. **제출**:
   - submission/ 디렉토리의 .npz 파일 제출
   - 노트북 파일도 함께 제출

## 📚 추가 자료

- [TensorFlow 공식 문서](https://www.tensorflow.org/)
- [Jupyter Notebook 가이드](https://jupyter-notebook.readthedocs.io/)
- [NumPy 문서](https://numpy.org/doc/)

## 🆘 도움 받기

문제가 계속되면:

1. `test_notebook.py` 실행 결과 공유
2. 에러 메시지 전체 복사
3. Python 버전 및 OS 정보 제공
4. Issue 생성 또는 문의

## ✅ 체크리스트

노트북 실행 전 확인:

- [ ] Python 3.8-3.12 설치됨
- [ ] 가상환경 생성 및 활성화됨
- [ ] requirements.txt 패키지 설치됨
- [ ] 데이터 파일이 ref/ 디렉토리에 있음
- [ ] test_notebook.py 통과
- [ ] submission/ 디렉토리 존재
- [ ] 충분한 디스크 공간 확보

모든 체크가 완료되면 노트북을 실행할 준비가 되었습니다! 🎉
