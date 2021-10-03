PC_1 = [57,49,41,33,25,17,9,1,
        58,50,42,34,26,18,10,2, 
        59,51,43,35,27,19,11,3,
        60,52,44,36,63,55,47,39,
        31,23,15,7,62,54,46,38,
        30,22,14,6,61,53,45,37,
        29,21,13,5,28,20,12,4]

PC_2= [14,17,11,24,1,5,
       3,28,15,6,21,10,
       23,19,12,4,26,8,
       16,7,27,20,13,2,
       41,52,31,37,47,55,
       30,40,51,45,33,48,
       44,49,39,56,34,53,
       46,42,50,36,29,32]

IP = [58,50,42,34,26,18,10,2,
      60,52,44,36,28,20,12,4,
      62,54,46,38,30,22,14,6,
      64,56,48,40,32,24,16,8,
      57,49,41,33,25,17,9,1,
      59,51,43,35,27,19,11,3,
      61,53,45,37,29,21,13,5,
      63,55,47,39,31,23,15,7]

E = [32,1,2,3,4,5,
     4,5,6,7,8,9,
     8,9,10,11,12,13,
     12,13,14,15,16,17,
     16,17,18,19,20,21,
     20,21,22,23,24,25,
     24,25,26,27,28,29,
     28,29,30,31,32,1]

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

PI_1 = [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

shifts=[1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2,  2,   2,   2,   1]

S = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

def string_to_binary(text : str) : 
    result=[]
    for i in text:
        binarry=str(bin(ord(i)).replace("0b",""))
        if len(binarry)<8:
            n=8-len(binarry)
            binarry=(n*"0")+binarry
        result.extend(binarry)
        result=list(map(int,result))
    return result

def binary_to_string(binary : list):
    result=[]
    for i in range(7,64,8):
        asci=0
        temp=binary[i-7:i+1]
        temp=temp[::-1]
        for j in range(0,8):
            asci+=(2**j)*temp[j]
        char=chr(asci)
        result.append(char)
    return "".join(result)

def shift(li : list , n : int ):
    for j in range(n):
        temp=li[0]
        for i in range(0,len(li)-1):
            li[i]=li[i+1]
        li[len(li)-1]=temp
    return li

class DES :
    def __init__(self , text=None , key = None , password = None):
        self.text=text
        self.key=key
        self.password=password


    def list_halfer(self , li : list):
        lenth=len(li)
        result1=li[0:lenth//2]
        result2=li[lenth//2:lenth]
        return result1 , result2

    def list_combination(self , li : list,combinationer : list ):
        result=[]
        for i in combinationer:
            result.append(li[i-1])
        return result

    def list_uncombination(self , li : list,combinationer : list ):
        result=[]
        for i in combinationer:
            result.append(li[i-1])
        return result

    def S_box(self,li):
        result=[]
        for i in range(8):
            fd =""
            fd=str(li[i][0])+str(li[i][5])  # first end
            middle=list(map(str , li[i][1:5]))
            middle="".join(middle)
            fd=int(fd , base=2)
            middle=int(middle , base=2)
            temp=bin(S[i][fd][middle]).replace("0b","")
            if len(temp)<4:
                temp=((4-len(temp))*"0")+temp
            temp=list(map(int,temp))
            result.extend(temp)
        return result
            


    def f(self , Rn_1,Kn):
        Rn_1=self.list_combination(Rn_1,E)
        R_x_K=[]
        for i in range(len(Kn)):
            R_x_K.append(Rn_1[i] ^ Kn[i])
        B=[]
        for i in range(6,49,6):
            B.append(R_x_K[i-6:i])
        result=self.S_box(B)
        result=self.list_combination(result,P)
        return result
        
        

    def encrypt(self , text , key):
        self.text=text
        self.key=key

        if len(text)!=8 or len(key)!=8 :
            raise "key and text must be only 8 character"

        M=string_to_binary(self.text)

        L,R=self.list_halfer(M)

        K=[]

        K.append(string_to_binary(self.key))

        Kplus=self.list_combination(K[0] , PC_1)

        C=[]
        D=[]
        C_temp , D_temp =self.list_halfer(Kplus)
        C.append(C_temp)
        D.append(D_temp)

        for i in shifts:
            C_temp=shift(C_temp,i)
            C.append(C_temp)
            D_temp=shift(D_temp,i)
            D.append(D_temp)


        for i in range(1,17):
            CD=C[i]+D[i]
            K.append(self.list_combination(CD,PC_2))
        L=[]
        R=[]
        M=self.list_combination(M,IP)
        L_temp , R_temp=self.list_halfer(M)
        L.append(L_temp)
        R.append(R_temp)

        for i in range(1,17):
            L.append(R[i-1])
            f_result=self.f(R[i-1],K[i])
            result=[]

            for j in range(len(f_result)):
                result.append(L[i-1][j] ^ f_result[j])
            R.append(result)

        
        password=R[16]+L[16]
        password=self.list_combination(password,PI_1)
        password=hex(int(''.join(list(map(str,password))),2)).replace("0x","")
        return password

    def decrypt(self ,password : str , key : str):
        self.password=list(map(int , bin(int(password , 16))[2:]))
        if len(self.password) <64:
            self.password=list(map(int,((64-len(self.password))*'0')))+self.password
        self.key=key

        if len(self.key)!=8 or len(self.password)!=64:
            raise "key and password must be 64 bit"
        K=[]
        K.append(string_to_binary(self.key))



        Kplus=self.list_combination(K[0] , PC_1)

        C=[]
        D=[]
        C_temp , D_temp =self.list_halfer(Kplus)
        C.append(C_temp)
        D.append(D_temp)

        for i in shifts:
            C_temp=shift(C_temp,i)
            C.append(C_temp)
            D_temp=shift(D_temp,i)
            D.append(D_temp)


        for i in range(1,17):
            CD=C[i]+D[i]
            K.append(self.list_combination(CD,PC_2))

        RL=64*[0]

        for i in range(64):
            RL[PI_1[i]-1]=self.password[i]


        R=[]
        L=[]

        R.append(RL[0:32])
        L.append(RL[32:64])

        for i in range(16,0,-1):
            R.append(L[16-i])
            f_result=self.f(R[16-i+1],K[i])
            temp=[]
            for j in range(len(f_result)):
                temp.append(R[16-i][j] ^ f_result[j])
            L.append(temp)

        

        LR=L[16]+R[16]
        result=64*[0]
        for i in range(64):
            result[IP[i]-1]=LR[i]

        return binary_to_string(result)




    






    


        





