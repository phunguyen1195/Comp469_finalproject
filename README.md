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
ROMS from this package https://store.steampowered.com/sub/102625/
in this I chose "Sonic The Hedgehog 2"
```

### Installing

## 1. Anaconda 3.6 for Linux

```
https://www.anaconda.com/download/#linux
```

## 2. Tensorflow

```
conda create --name gym-retro python=3.5
source activate gym-retro
pip install --ignore-installed --upgrade \ https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.8.0-cp35-cp35m-linux_x86_64.whl
```

## 3. Gym

```
pip install gym
```

## 4. Retro Gym

```
pip install gym-retro
```

## 5. Baselines

```
clone this where you feel store your projects

git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
```

## 6. Import ROMS
After purchase your game on Steam use the below command to import your rom

```
python -m retro.import.sega_classics
```

## 7. Opencv

```
pip install opencv-python
```
## 7. anyrl library

```
pip install anyrl 
```

## 8. Clone this repository

```
pip install anyrl 
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system
