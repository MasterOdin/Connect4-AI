Connect4-AI
===========
[![Build Status](https://travis-ci.org/MasterOdin/Connect4-AI.svg?branch=master)](https://travis-ci.org/MasterOdin/Connect4-AI) [![Coverage Status](https://coveralls.io/repos/MasterOdin/Connect4-AI/badge.png?branch=master)](https://coveralls.io/r/MasterOdin/Connect4-AI?branch=master)


Connect 4 Game written in Python including an AI player 2 implementing a number of strategies

The AI will implement the following strategies:
1. Pick a random column and place a piece there if not full
2. Minimax algorith with alpha-beta pruning with some number of move lookead (default 5)

Other than the Very Easy strategy, the bot will implement a minmax algorithm with alpha-beta pruning to determine an
optimal move
