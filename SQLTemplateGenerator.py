import random as rd;
dictionary = ['opine','airplane','melodic','jittery',
            'back','listen','rambunctious','memory',
            'humiliate','therapeutic','economic','sleep',
            'eight','hide','fireman','sleep','note',
            'airport','shirt','yarn','nerve','dedicate',
            'kill','actually','stem','bed','shrill',
            'zinc','psychedelic','found','pathetic',
            'start','caption','yield','structure'
            ]

def headGen():
    head = ''
    for i in range(8):
        
        head += rd.choice(dictionary)+' ';
    return head;
def bodyGen():
    body = ''
    for i in range(40):
        
        body += rd.choice(dictionary)+' ';
    return body;
def dateGen():
    year = '2022' # // add date here
    month = rd.choice([1,2,3,4,5,6]);
    day = rd.choice([i for i in range(1,30)])
    stringify = ('{}-{}-{}').format(year,month,day);
    return stringify
template = "INSERT INTO `articles` (`id`, `head`, `body`, `date`) VALUES "  #// modify query here!
for i in range(90):
    idnumber = 'NULL';
    head = headGen();
    body = bodyGen();
    date = dateGen();
    data = "({}, '{}', '{}', '{}')".format(idnumber,head,body,date);
    template += data+',';

template = template[:-1];
template += ';';
print(template);
 

    
