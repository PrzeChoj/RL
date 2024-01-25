# RL

```
conda create -n RL2 python=3.8.5; # 3.8.16 na dgx-3
conda activate RL2
pip install gymnasium
pip install "gymnasium[atari]"
pip install gym
pip install pygame
pip install torch
pip install scikit-image
pip install tensorboard

pip install tqdm

pip install notebook

ale-import-roms roms/

python skiing_play.py

python dqn-atari-master/test.py Skiing dqn-atari-master/Skiing.pt
```

# Run DQN

### Train
```
pyenv activate RL

python3 ./dqn-atari-master/train.py Skiing ./dqn-atari-master/Skiing.pt --replay_memory_size 20000 --replay_start_size 3000 --checkpoint --minibatch_size 64
python3 ./dqn-atari-master/train.py Skiing ./dqn-atari-master/Skiing_Adam_.pt --replay_memory_size 2000 --replay_start_size 300 --checkpoint --minibatch_size 64
python3 ./dqn-atari-master/train.py Skiing ./dqn-atari-master/Skiing_Adam_eden.pt --replay_memory_size 20000 --replay_start_size 3000 --checkpoint --minibatch_size 64
python3 ./dqn-atari-master/train.py Skiing ./dqn-atari-master/Skiing_Adam_eden2.pt --replay_memory_size 20000 --replay_start_size 3000 --checkpoint --minibatch_size 64
```

### Test
```
python3 ./dqn-atari-master/test.py Skiing ./dqn-atari-master/Skiing.pt
python3 ./dqn-atari-master/test.py Skiing ./dqn-atari-master/Skiing_Adam.pt
python3 ./dqn-atari-master/test.py Skiing ./dqn-atari-master/Skiing_Adam_eden2.pt
```
