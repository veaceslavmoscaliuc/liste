# Python DATA STRUCTURES
days = [ "MO" , "TU" , "WD" , "TH" , "FR" , "SA" , "SU" ]
temps = [10.0 ,  9.0 ,  8.0 ,  0.0 , -5.0 , -10.0 , 0.0 ]
#         0       1      2      3      4       5     6
i = 0


## HW1: rewrite this code with WHILE
while i < len(temps,) and i < len(days):  
        for i in range(7):
            if temps [i] <= 0:
                sing = "*"
            else:
                sing = " "
            print( sing, days[i], temps[i] )
            i=i+1