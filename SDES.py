# generate key
def P10(string):
    res=string[2]+string[4]+string[1]+string[6]+string[3]+string[9]+string[0]+string[8]+string[7]+string[5]
    return res

def LS_N(string,n):
    res=string
    for i in range(n):
        temp = res[0]
        res = res[1:]
        res+=temp
    return res

def P8(s):
    res = s[5]+s[2]+s[6]+s[3]+s[7]+s[4]+s[9]+s[8]
    return res

def generate_key(key):
    p10 = P10(key)
    Left_LS_1 = LS_N(p10[:5],1)
    Right_LS_1 = LS_N(p10[5:],1)
    K1 = P8(Left_LS_1+Right_LS_1)
    #print(K1)
    
    Left_LS_2 = LS_N(Left_LS_1,2)
    Right_LS_2 = LS_N(Right_LS_1,2)
    K2 = P8(Left_LS_2+Right_LS_2)
    #print(K2)
    return K1,K2

def IP(p):
    return p[1]+p[5]+p[2]+p[0]+p[3]+p[7]+p[4]+p[6]
def IP_Inverse(p):
    return p[3]+p[0]+p[2]+p[4]+p[6]+p[1]+p[7]+p[5]

def EP(n):
    return n[3]+n[0]+n[1]+n[2]+n[1]+n[2]+n[3]+n[0]

def XOR(a,b):
    res=''
    for i in range(len(a)):
        res+=str(int(a[i])^int(b[i]))
    return res

def S0(s):
    matrix=[
        [1,0,3,2],
        [3,2,1,0],
        [0,2,1,3],
        [3,1,3,2]
    ]
    i = int(s[0])*2+int(s[3])
    j = int(s[1])*2+int(s[2])
    res = bin(matrix[i][j])[2:]
    res = (2-len(res))*'0'+str(res)
    return res

def S1(s):
    matrix=[
        [0,1,2,3],
        [2,0,1,3],
        [3,0,1,0],
        [2,1,0,3]
    ]
    i = int(s[0])*2+int(s[3])
    j = int(s[1])*2+int(s[2])
    res = bin(matrix[i][j])[2:]
    res = (2-len(res))*'0'+str(res)
    return res

def SW(s):
    return s[4:]+s[0:4]

def P4(s):
    return s[1]+s[3]+s[2]+s[0]
def encrypt(plain,K1,K2):
    ip_res = IP(plain)
    ##########################
    left = ip_res[0:4]
    right = ip_res[4:]
    
    EP_res = EP(right)
    K1_res = XOR(EP_res,K1)
    
    S0_res = S0(K1_res[0:4])
    S1_res = S1(K1_res[4:])
    
    P4_res = P4(S0_res+S1_res)
    
    XOR_res = XOR(left,P4_res)
    
    ##########################
    left = right
    right = XOR_res
    
    EP_res = EP(right)
    K2_res = XOR(EP_res,K2)
    
    S0_res = S0(K2_res[0:4])
    S1_res = S1(K2_res[4:])
    
    P4_res = P4(S0_res+S1_res)
    
    XOR_res = XOR(left,P4_res)
    
    ##########################
    ip_reverse = IP_Inverse(XOR_res)
    return ip_reverse

def decrypt(cipher,K1,K2):
    ip_res = IP(cipher)

    ##########################
    left = ip_res[0:4]
    right = ip_res[4:]
    
    EP_res = EP(right)

    K1_res = XOR(EP_res,K2)

    S0_res = S0(K1_res[0:4])
    S1_res = S1(K1_res[4:])

    P4_res = P4(S0_res+S1_res)
    XOR_res = XOR(left,P4_res)

    
    ##########################
    left = right
    right = XOR_res

    EP_res = EP(right)
    K2_res = XOR(EP_res,K1)

    S0_res = S0(K2_res[0:4])
    S1_res = S1(K2_res[4:])

    P4_res = P4(S0_res+S1_res)  
    XOR_res = XOR(left,P4_res)
    ##########################
    ip_reverse = IP_Inverse(XOR_res+right)
    return ip_reverse

#使用课堂上讲的例题来验证
K1,K2 = generate_key('0111111101')
res = decrypt('10100010',K1,K2)
print(res)