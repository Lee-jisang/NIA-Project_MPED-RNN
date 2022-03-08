# MPED-RNN


# 딥러닝 모델을 이용한 졸음 감지 서비스
**딥러닝 모델을 이용한 졸음 감지 서비스와 함께 눈 건강 보호, 일정 관리 등의 부가 서비스를 제공하는 프로젝트**

## 1. 개발 환경 및 사용 라이브러리
- **OS** : Window 10
- **Language** : Python 3.8, HTML5, JavaScript, CSS
- **Framework** : Django
- **DBMS** : MySQL
- **Library** : Python Channels, Web Socket, OpenCV, imutils, dlib

## 2. 구성도
![<서비스구성도>](/00_img/서비스구성도.png)   
## 3. 주요기능   
- 졸음감지 및 알림 기능
- 눈동자 깜빡임 횟수 측정
- 졸음 통계 제공

## 4. 결과물
**4.1 얼굴인식**   
![<얼굴인식>](/00_img/1.png)   

**4.2 졸음감지경고**   
![<졸음감지경고1>](/00_img/2.png)![<졸음감지경고2>](/00_img/3.png)   

**4.3 눈 깜빡임 경고**   
![<눈깜빡임경고>](/00_img/4.png)   

**4.4 투두리스트(ToDo-List)**   
![<투두리스트>](/00_img/6.png)   

**4.5 통계제시**   
![<통계제시>](/00_img/5.png)   

**4.6 각종 게시판**   
![<자유게시판>](/00_img/7.png)![<Q&A>](/00_img/8.png)![<랭킹게시판>](/00_img/10.png)  

**4.7 졸음 방지 및 눈 건강 보호 해결책**   
![<해결책>](/00_img/9.png)   
 

## 5. 구성원 및 역할분담

|**이름**|**담당업무**|
|---|---|
|최영환|풀스택, 프로젝트 총괄 / 팀장|
|이지상|프론트엔드 / 프론트엔드장|
|정영도|프론트엔드|
|이현수|풀스택 / 백엔드장|
|오수지|백엔드|




# Environment Setup

First please create an appropriate environment using conda: 

> conda env create -f environment.yml

> conda activate tbad

# Folder Configuration

### E2ON  

> Pre-processed E2ON dataset(csv, npy)
> JSON files of Original E2ON dataset

# Test Pre-Trained Models

To evaluate pre-trained models run the evaluate.py script.
Some examples:

#### Test E2ON data set.

> python evaluate.py --gpu_ids 0 --gpu_memory 0.2 combined_model ./E2ON_all/pretrained/mp_Grobust_Lrobust_Orobust_concatdown/training_2021_09_22_19_35_12 ./E2ON_all/testing/trajectories/01 ./E2ON_test/testing/frame_level_masks/01 --video_resolution 1920x1080 --overlapping_trajectories

# Train Models from Scratch

To train a model from scratch you should look up the model's configuration options using the option --help on the training.py script. Here is one example:

#### Train MPED-RNN on the E2ON data set.

> python train.py --gpu_ids 0 --gpu_memory 0.1 combined_model ./E2ON_all/training/trajectories/01
> --video_resolution 1920x1080 --message_passing --reconstruct_original_data --multiple_outputs --multiple_outputs_before_concatenation --input_length 12
>  --rec_length 12 --pred_length 6 --reconstruct_reverse --cell gru --global_hidden 8 --local_hidden 16 --output_activation linear 
>  --optimiser adam --learning_rate 0.001 --loss mse --epochs 5 --batch_size 256 --global_normalisation robust --local_normalisation robust 
>  --out_normalisation robust
