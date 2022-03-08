# NIA-Project_MPED-RNN
**스켈레톤 정보를 활용한 공공 보안용 CCTV의 이상행동 학습용 데이터 적합성 검증 연구**

## 1. 테스트 환경 및 사용 라이브러리
- **OS** : Window 10
- **Language** : Python, JSON
- **Framework** : Visual Studio Code

## 2. 테스트 결과
**4.1 얼굴인식**   
![<얼굴인식>](/00_img/1.png)   
 

## 5. 구성원 및 협력기관

**구성원**
이지상, 김경수, 이세림

**협력기관**

동국대학교, 




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
