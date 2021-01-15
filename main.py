import random
drawer = [
    'Katelyn','Matt W','Tasha','Alex','Nick','Mariah','Matt S', 'Zack', 'Lindsy', 'Tessa','Ben', 'Joe']
black_list = {
    'Katelyn': ['Matt W', 'Katelyn', 'Matt S'],
    'Matt W': ['Matt W', 'Katelyn', 'Joe'],
    'Tasha': ['Tasha', 'Alex', 'Nick'],
    'Alex': ['Tasha', 'Alex', 'Katelyn'],
    'Matt S': ['Matt S', 'Mariah','Tasha'],
    'Mariah': ['Matt S', 'Mariah', 'Matt W'],
    'Nick': ['Nick', 'Tessa'],
    'Zack': ['Zack', 'Lindsy', 'Ben'],
    'Lindsy': ['Lindsy', 'Zack', 'Alex'],
    'Tessa': ['Tessa', 'Mariah'],
    'Ben': ['Ben', 'Zack'],
    'Joe': ['Joe', 'Lindsy'],
}

def the_drawing()-> list: 
    drawn = []
    not_picked = ['Katelyn','Matt W','Tasha','Alex','Nick','Mariah','Matt S', 'Zack', 'Lindsy', 'Tessa','Ben', 'Joe']
    counter: int = 0
    for key in drawer:
        rand: int = random.randint(0,len(not_picked)-1)
        drawn_name = not_picked[rand]
        not_allowed = black_list[key]
        if drawn_name in not_allowed:
            if len(not_picked)<=1:
                the_drawing()
            while counter < 50:
                rand = random.randint(0,len(not_picked)-1)
                drawn_name = not_picked[rand]
                not_allowed = black_list[key]
                if key in not_allowed: 
                    counter+=1 
                else:
                    drawn.append(drawn_name)
                    not_picked.remove(drawn_name)
                    break
        else:
            drawn.append(drawn_name)
            not_picked.remove(drawn_name)
    return drawn

drawn = the_drawing()
while len(drawn)<= 11:
    drawn = the_drawing()   

print('\n')
print('Gifter ..........  Reciever') 
#print('\n')
for i in range(len(drawn)):
    print(f'{drawer[i]} ..........  {drawn[i]}')
print('\n')




