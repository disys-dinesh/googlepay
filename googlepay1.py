class googlepay:                                                                                   
    
    def _init_(self,UPI_ID,Email_ID,Phone_number,Name,Bankname,Account_number,IFSCcode):
        self.upiid=UPI_ID
        self.emailid=Email_ID
        self.mobile=Phone_number
        self.name=Name
        self.bankname=Bankname
        self.account_number=Account_number
        self.ifsccode=IFSCcode
        
    def upiid_verification(self):
        if type(self.upiid) == str:                              
            if len(self.upiid) <= 6:                                                                              
                print("upiid verified successfully")
            else:
                raise ValueError("the upiid should not exceed 6 values")
        else:
            raise TypeError("invalid upiid")
        
    def emailid_verification(self):
        if type(self.emailid) == str:                                                                               
            if len(self.emailid) <= 30:                                                                              
                print("emailid verified successfully")
            else:
                raise ValueError("the emailid should not exceed 30 values")
        else:
            raise TypeError("invalid emailid")

        
    def mobile_verification(self):
        if (len(self.mobile)==10):
            if type(self.mobile) == str:                                                                            
                print("phonenumber verified successfully")
            else:
                raise TypeError("phonenumber should contain only integers ")
        else:
            raise ValueError("phone number should not exceed or deceed 10")
        
        
    def name_verification(self):
        if type(self.name) == str:
            if len(self.name) <= 20:                                                                                
                print("name verified successfully")
            else:
                raise ValueError("The name should not edxceed 20 letters")
        else:
            raise TypeError("The name should be in letters only")



    def bankname_verification(self):
        if type(self.bankname) == str:
            if len(self.bankname) <= 15:                                                                                
                print("bankname verified successfully")
            else:
                raise ValueError("account number should not exceed 15 letters")
        else:
            raise TypeError("account number should be in numbers only")


    def ifsccode_verification(self):
        if type(self.ifsccode) == str:                                                                               
            if len(self.ifsccode) <= 16:                                                                              
                print("ifsccode verified successfully")
            else:
                raise ValueError(" ifsccode should not exceed 16 values")
        else:
            raise TypeError("invalid ifsccode")    

  

    def set_Pin(self,number):
        self.pin=number
        if (len(self.pin)==4 or len(self.pin) ==6):
            print("your pin is successfully created")
        else:
            raise ValueError("Invalid pin_number")
        

    def Enter_your_Pin(self,match,pin):
        self.match=match
        self.pin=pin
        if self.match==self.pin:
            print("DONE")
        else:
            raise ValueError("pin not matched")
