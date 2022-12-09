import numpy as np
visit={}
for i in range(ord('a'),ord('z')+1):
    visit[chr(i)]=False
del visit['j']

def key_matrix(key):
    k = ''
    key = key.lower().replace('j','i')
    for i in key:
        if i not in k:
            k+=i
            visit[i]=True
    matrix=[]
    for i in k:
        matrix.append(i)
    

    for i,j in visit.items():
        if j ==False:
            matrix.append(i)
    matrix = np.array(matrix).reshape((5,5))
    print(matrix)
    return matrix

def process_plain(p):
    groups=[]
    i=0
    while(i<len(p)):
        if(p[i]!=p[i+1]):
            groups.append(p[i]+p[i+1])
            i+=2
        else:
            groups.append(p[i]+'x')
            i+=1
    print(groups)
    return groups

process_plain("communist")

def find_index(ch,matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if ch == matrix[i][j]:
                return i,j
    
    return -1,-1


def encrypt(group,key_matrix): #经过处理后的双字母对
    res=[]
    for g in group:
        ix,iy = find_index(g[0],key_matrix)
        jx,jy = find_index(g[1],key_matrix)
        if ix == jx: #同行
            c1 = key_matrix[ix][(iy+1)%5]
            c2 = key_matrix[jx][(jy+1)%5]
            res.append(c1+c2)
        elif iy == jy: #同列
            c1 = key_matrix[(ix+1)%5][iy]
            c2 = key_matrix[(jx+1)%5][jy]
            res.append(c1+c2)
        else:
            c1 = key_matrix[ix][jy]
            c2 = key_matrix[jx][iy]
            res.append(c1+c2)
    
    return res

def decrypt(group,key_matrix):
    res=[]
    for g in group:
        ix,iy = find_index(g[0],key_matrix)
        jx,jy = find_index(g[1],key_matrix)
        if ix == jx: #同行
            c1 = key_matrix[ix][(iy-1+5)%5]
            c2 = key_matrix[jx][(jy-1+5)%5]
            res.append(c1+c2)
        elif iy == jy: #同列
            c1 = key_matrix[(ix-1+5)%5][iy]
            c2 = key_matrix[(jx-1+5)%5][jy]
            res.append(c1+c2)
        else:
            c1 = key_matrix[ix][jy]
            c2 = key_matrix[jx][iy]
            res.append(c1+c2)
    
    return res


plain = "hello"
key = "world"
processed=process_plain(plain)
key= key_matrix(key)
enc = encrypt(processed,key)
print(enc)
dec = decrypt(enc,key)
print(dec)