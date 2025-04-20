import random
import collections
boxes = [ "green" , "orange", "purple", "golden", "nothing"]
equipment = collections.Counter(random.choices(boxes, [ 75, 20, 4,  1,  40 ], k = 5))
g = equipment["green"] * 1000
o = equipment["orange"] * 4000
p = equipment["purple"] * 9000
gn = equipment["golden"] * 16000
n = equipment["nothing"] * 0
gold = g + o + p + gn + n

print(gold)

print(equipment)
  
      
