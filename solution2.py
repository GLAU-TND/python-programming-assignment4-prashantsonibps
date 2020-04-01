p=eval(input())
def new(q):
  try:
    for k in q:
      if type(q[k])==type({}):
        for i in q[k]:
          q[k+i]=q[k][i]
        q.pop(k)
        new(q)
    else:
      print(q)
  except RuntimeError:
    pass
new(p)