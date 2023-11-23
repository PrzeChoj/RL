# RL

```
conda create -n RL2 python=3.8.5;
conda activate RL2
pip install gymnasium
pip install "gymnasium[atari]"
pip install pygame

pip install tqdm
```

# Run DQN

### Train
```
python3 ./dqn-atari-master/train.py Skiing ./dqn-atari-master/Skiing.pt --replay_memory_size 20000 --replay_start_size 3000 --checkpoint --minibatch_size 64
```

### Test
```
python3 ./dqn-atari-master/test.py Skiing ./dqn-atari-master/Skiing.pt
```
