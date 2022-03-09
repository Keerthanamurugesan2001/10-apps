lookup = {}
lookup = dict()
lookup1 = {'age': 42, 'loc': 'Italy'}
lookup2 = dict(age=42, loc='Italy')

lookup2['cat'] = 'funcodecamps'

print(lookup2)
print(lookup1)

if 'cat' in lookup2:
    print(lookup2['cat'])


class wizard:
    def __init__(self,name,level):
        self.level = level
        self.name = name

gandlof = wizard('kajk',23)
print(gandlof)
print(gandlof.__dict__)