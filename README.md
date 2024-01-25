# RL agent for Skiing

# Setup

```
conda create -n RL python=3.8.5;
conda activate RL

pip install gymnasium
pip install "gymnasium[atari]"
pip install gym
pip install pygame
pip install torch
pip install scikit-image
pip install tensorboard
pip install tqdm

ale-import-roms roms/ # Instalacja gry Skiing

python skiing_play.py # Gra dla czlowieka

python test.py Skiing dqn-atari-master/Skiing.pt
python ./test.py Skiing ./Trained_Agents/Skiing_1_old.pt
python ./test.py Skiing ./Trained_Agents/Skiing_6_dont_stop_v3.pt
```

# Trening DQN

```
conda activate RL

python ./train.py Skiing ./Skiing_numer_nazwa_testu.pt --replay_memory_size 20000 --replay_start_size 3000 --checkpoint --minibatch_size 64
```
