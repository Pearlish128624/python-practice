# Class

Design data based on real world (or some concept)

For example :
```python
class Player():
  def __init__(self, name):
    self.name = name
    self.score = 0
  def getName(self):
    return self.name
  def getScore(self):
    return self.score
  def setScore(self, score):
    self.score = score

class Game:
  def __init__(self, player):
    self.live = 10
    self.player = player
  def isGameOver(self):
    return self.live <= 0
```

## Homework
You are handling a billing system.

Customer will send their orders to systems.

You should list their products together, and how much they should pay.

### Input :
- `produce.txt`: product list
- `rule.txt`: in some conditions, products will be on sales
- `record.txt`: logs from system

### Output :
Take Robin's billing:
```
Robin: BB
Robin: AADA
Robin: DEFC
```

```
For 1st bill, 2 purses will take 2 pens, and get 85% discount.

=> (350 + 350) * 0.85 = $595

For 2nd bill, 2 free pen, a fork, and a pen.

=> 150 + 10 = $160

For 3rd bill, a fork, a candy, get a $70 tooth brush, and a key chain

=> 150 + 50 + 70 + 100 = $370
```

```
=> Robin: 3A2B1C2D1E1F $1125
```