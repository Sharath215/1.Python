class BasicFunctions():
    
    
    
    def SubFields():
        List = ["Machine Learning", "Neural Networks", "VisionRobotics", "Speech Processing", "Natural Language Processing" ]
        print("Sub-fields in AI are:\n")
        for i in List:
            print(i)
            

    
    def OddEven(a):
        if(a%2==0):
            res = "is Even Number"
        else:
            res = "is Odd Number"
        return res
    

    def Eligible(A,G):
        if(G == "Male" and A < 21):
            res = "NOT Eligible"

        elif(G == "Male" and A >= 21):
            res = "Eligible"

        elif(G == "Female" and A >= 18):
            res = "Eligible"

        elif(G == "Female" and A < 18):
            res = "NOT Eligible"

        else:
            res = "invalid Values"

        return res
    
    def Percentage():
        S1 = int(input("Subject1: "))
        S2 = int(input("Subject2: "))
        S3 = int(input("Subject3: "))
        S4 = int(input("Subject4: "))
        S5 = int(input("Subject5: "))
        total = S1+S2+S3+S4+S5
        P = (total/500)*100
        print("Total: ",total,"\nPercentage : ",P)
        
    def triangle():
        H = int(input("Height : "))
        B = int(input("Breadth : "))
        print("area Formula : (Height*Breadth)/2")
        A = (H*B)/2
        print("Area of Triangle : ", A )
        H1 = int(input("Height1 : "))
        H2 = int(input("Height2 : "))
        B2 = int(input("Breadth : "))
        print("Perimeter Formula : Height1+Height2+Breadth")
        P= H1+H2+B2
        print("Perimeter of Triangle : ",P)

    
    
   
    
            
            
