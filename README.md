# Comp469_finalproject

An application of retro gym.
Attempt different baseline algorithms available on OpenAI.

## Getting Started

### Prerequisites

```
Anaconda
Tensorflow
Retro Gym
Gym
Baselines
Opencv
anyrl library
ROMS from this package https://store.steampowered.com/sub/102625/
in this I chose "Sonic The Hedgehog 2"
```

## Installing

### 1. Anaconda 3.6 for Linux

```
https://www.anaconda.com/download/#linux
```

### 2. Tensorflow

```
conda create --name gym-retro python=3.5
source activate gym-retro
pip install --ignore-installed --upgrade \ https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp35-cp35m-linux_x86_64.whl
```

### 3. Gym

```
pip install gym
```

### 4. Retro Gym

```
pip install gym-retro
```

### 5. Baselines

```
clone this where you feel store your projects

git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
```

### 6. Import ROMS
After purchase your game on Steam use the below command to import your rom

```
python -m retro.import.sega_classics
```

### 7. Opencv

```
pip install opencv-python
```
### 8. anyrl library

```
pip install anyrl 
```

### 9. Clone this repository

```
https://github.com/phunguyen1195/Comp469_finalproject.git
```
### 10. Run the Game:

take random action
```
python random_agent.py
```

always move right
```
python right_agent.py
```

JERK algorithm
```
python jerk_agent.py
```

Rainbow algorithm
```
python rainbow_agent.py
```

ppo2 algorithm
```
python ppo2_agent.py
```

## NOTES: 

This github uses game: Sonic The Hedgehog 2 with stages: CasinoNightZone.Act1 and AquaticRuinZone.Act1
please consult more from these sources if you wish to make changes:

```
https://github.com/openai/retro
https://github.com/openai/baselines
```

the latest update of baseline repository is buggy. I used the previous version of baseline github 
