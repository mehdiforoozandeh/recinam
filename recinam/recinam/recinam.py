def file_to_sequence(name , Format):
        data = open(name + Format ,'rb')
        key = {}
        while True:
            z = ''.join(format(ord(x),'b') for x in data.read(1))
            if z == '':
                break
            if len(z) != 8:
                while len(z) < 8 :
                    z = '0'+z
            for i in range(0,8,2):
                if z[i:i+2] in key:
                    key[z[i:i+2]] += 1
                else:
                    key[z[i:i+2]] = 1
        nuc=['G','C','A','T']
        a=sorted(key, key=key.get, reverse=True)
        for w,i in zip(a,range(4)):
                key[w]=nuc[i]
        keyfile= open('key.nky','w')
        for k,v in key.items():
            keyfile.write(v+':'+k+'\n')
        keyfile.close()
        dataf = open(name+'.nuc','w')
        data = open(name+Format ,'rb')
        while True:
            y = ''.join(format(ord(x),'b') for x in data.read(1))
            if y == '':
                break
            if len(y) != 8:
                while len(y) < 8 :
                    y = '0'+y
            for i in range(0,8,2) :
                dataf.write(key[y[i:i+2]])
        dataf.close()

def sequence_to_file(name, Format):
    dataf = open(name + '(2nd)' + Format, 'wb')
    data = open(name + '.nuc', 'r')
    key = {}
    keyopen = open('key.nky', 'r')
    l = keyopen.readlines()
    for line in l:
        n = line[0]
        b = line[2:4]
        key[n] = b
    binary = ''
    while True:
        q = data.read(64)
        if q == '':
            break
        else:
            for x in q:
                binary += key[x]
            st = (binary[i:i + 8] for i in range(0, len(binary), 8))
            dataf.write(''.join(chr(int(x, 2)) for x in st))
            binary = ''
    data.close()
    dataf.close()