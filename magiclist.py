from dataclasses import dataclass
class MagicList(list):
    def __init__(self, cls_type=None):
        self.type = cls_type
    def __getitem__(self, i,v=None):
      
      l = super(MagicList, self)
      if i==l.__len__() and self.type is not None:
        l.append(self.type(v))
      return super(MagicList, self).__getitem__(i)
      
    def __setitem__(self, i, v):
      
      l = super(MagicList, self)
      if i==l.__len__() :

          l.append(v)
      # elif (i ==-1 or i==0 ) and l.__len__()==0:
            # l.append(v)
      else:
          l.__setitem__(i,v)



@dataclass
class Person:
  age :  int 





def test_sanity():

    
  x = MagicList()
  x[0]=1
  assert x[0]==1
  x[1]=7
  assert x[1]==7
  del x[1]
  assert len(x) ==1
  x[1] = 2

  assert x[1]==2
test_sanity()
def test_types():
  
  x = MagicList(Person)
  x[0]=Person(22)
  print(x)
  x[1].age =6
  print(x)
  del x
  
  x = MagicList(Person)
  
  x[0].age=333
  x[]
  print(x)
test_types()