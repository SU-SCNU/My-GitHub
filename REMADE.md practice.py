def contains(bag, e) :
    return e in bag

def insert(bag, e) :
    bag.append(e)

def remove(bag, e) :
    bag.remove(e)

def count(bag):
    return len(bag)

myBag = [ ]
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '노트북')
insert(myBag, '빗')
insert(myBag, '손수건')
insert(myBag, '안경')
insert(myBag, '우산')
insert(myBag, '옷')
print('내 가방속의 물건:', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('내 가방속의 물건:', myBag)
print('내 가방속의 물건 유무:', contains(myBag, '휴대폰'))
print('내 가방속의 물건 유무:', contains(myBag, '커피'))
print('내 가방속의 물건 개수:', count(myBag))

def numOf(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e :
            count = count + 1
    return count

print('빗 의 개수', numOf(myBag, '빗'))
print('빗 의 개수', numOf(myBag, '빗'))