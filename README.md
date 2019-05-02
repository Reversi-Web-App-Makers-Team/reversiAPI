# reversiAPI==1.0.10

reversi api for playing reversi game.

# To install
hit the following command on your command line.
```
$ pip install git+https://github.com/reversiWebApp/reversiAPI.git -U
```

# Battle Modes
## human vs human
hit the following command on your command line.
```
$ git clone git@github.com:reversiWebApp/reversiAPI.git
$ cd reversiAPI/reversiAPI/
$ python human_vs_human_main.py
```
and game starts ono your shell.

## human vs agents
### Agents
#### random :
 - he choose stone putting position randomly.
#### dqn1, dqn2 :
 - he choose stone putting position where q value is maximized restricted to stone putable position. 
 - deeq q-learning is used to train these agents.
 - dqn2 is stronger than dqn1.
#### sl1, sl2 :
 - he choose stone putting position where probability of winning the game is maximized restricted to stone putable position.
 - CNN is used. The model has board information as input and predicts where the winner put the stone.
 - sl2 is stronger than sl1.

if you want to play with these agents, hit the following command on your command line.
```
$ git clone git@github.com:reversiWebApp/reversiAPI.git
$ cd reversiAPI/reversiAPI/
$ python human_vs_(agent's name you want to play with in the above).py
```
and game starts on your shell.
