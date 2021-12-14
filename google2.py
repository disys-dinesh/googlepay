import googlepay1
upiid=input("enter upiid")
emailid=input("enter the email id")
phone_number=input("enter phone number")
name=input("enter name ")
bankname=input("enter bankname")
account_number=input("enter account number")
ifsccode=input("enter ifsc code")
din=googlepay1.googlepay(upiid,emailid,phone_number,name,bankname,account_number,ifsccode)

class Phonepe(googlepay1.googlepay):
    
    def _init_(self,UPI_ID,Email_ID,Phone_number,Name,Bankname,Account_number,IFSCcode):
        super()._init_(UPI_ID,Email_ID,Phone_number,Name,Bankname,Account_number,IFSCcode)

    def open_Phonepe(self):
        print("Phone pay")
        
dk=Phonepe("123456","dinesh@gmail.com","9080706050","dinesh","indianbank","1234567890","IOB123456")

dk.open_phonepe()

dk.phone_number_verification()

dk.name_verification()

dk.bankname_verification()

dk.account_number_verification()

dk.ifsccode_verification()

y=input("set yoyr pin")

Ranjini.set_Pin(y)

i=input("enter the pin")

dk.Enter_your_Pin(i,i)



Googlepay=[{"name":"Ramesh","Googlepaynumber":"8838924821","Transactiontype":"regular"},
           {"name":"Suresh","Googlepaynumber":"8838924822","Transactiontype":"regular"},
           {"name":"vinesh","Googlepaynumber":"8838924823","Transactiontype":"regular"},
           {"name":"Naresh","Googlepaynumber":"8838924824","Transactiontype":"regular"},
           {"name":"Naveen","Googlepaynumber":"8838924825","Transactiontype":"regular"},
           {"name":"Raveen","Googlepaynumber":"8838924826","Transactiontype":"regular"},
           {"name":"Ravi","Googlepaynumber":"8838924827","Transactiontype":"regular"},
           {"name":"Subi","Googlepaynumber":"8838924828","Transactiontype":"regular"},
           {"name":"Bhuvi","Googlepaynumber":"8838924829","Transactiontype":"regular"},
           {"name":"Kavi","Googlepaynumber":"8838924820","Transactiontype":"regular"},
           {"name":"veera","Googlepaynumber":"8838924812","Transactiontype":"regular"},
           {"name":"Theran","Googlepaynumber":"8838924834","Transactiontype":"regular"},
           {"name":"Praveen","Googlepaynumber":"8838924845","Transactiontype":"regular"},
           {"name":"Vikram","Googlepaynumber":"8838924856","Transactiontype":"regular"},
           {"name":"Vicky","Googlepaynumber":"8838924867","Transactiontype":"regular"},
           {"name":"Zara","Googlepaynumber":"8838924878","Transactiontype":"regular"},
           {"name":"Nabi","Googlepaynumber":"8838924821","Transactiontype":"regular"},
           {"name":"Abdul","Googlepaynumber":"8838924822","Transactiontype":"regular"},
           {"name":"Khaliq","Googlepaynumber":"8838924823","Transactiontype":"regular"},
           {"name":"Kaali","Googlepaynumber":"8838924824","Transactiontype":"regular"},
           {"name":"Saminathan","Googlepaynumber":"8838924825","Transactiontype":"regular"},
           {"name":"Pushpanathan","Googlepaynumber":"8838924826","Transactiontype":"regular"},
           {"name":"Indhu","Googlepaynumber":"8838924827","Transactiontype":"regular"},
           {"name":"Mathi","Googlepaynumber":"8838924828","Transactiontype":"regular"},
           {"name":"Manoj","Googlepaynumber":"8838924829","Transactiontype":"regular"},
           {"name":"Mano","Googlepaynumber":"8838924820","Transactiontype":"regular"},
           {"name":"Manoranjini","Googlepaynumber":"8837724812","Transactiontype":"regular"},
           {"name":"Monu","Googlepaynumber":"8838004834","Transactiontype":"regular"},
           {"name":"Darshini","Googlepaynumber":"8833324845","Transactiontype":"regular"},
           {"name":"Darshan","Googlepaynumber":"8838924856","Transactiontype":"regular"},
           {"name":"Badhri","Googlepaynumber":"8838924867","Transactiontype":"regular"},
           {"name":"Justus","Googlepaynumber":"8838926678","Transactiontype":"regular"},
           {"name":"Paul","Googlepaynumber":"8838990821","Transactiontype":"regular"},
           {"name":"Bala","Googlepaynumber":"8838923422","Transactiontype":"regular"},
           {"name":"Swetha","Googlepaynumber":"8838804823","Transactiontype":"regular"},
           {"name":"Aswetha","Googlepaynumber":"89098924824","Transactiontype":"regular"},
           {"name":"Balamurugan","Googlepaynumber":"8888924825","Transactiontype":"regular"},
           {"name":"Murugan","Googlepaynumber":"8838824826","Transactiontype":"regular"},
           {"name":"Balu","Googlepaynumber":"8838977827","Transactiontype":"regular"},
           {"name":"Gopi","Googlepaynumber":"8838921128","Transactiontype":"regular"},
           {"name":"Gopal","Googlepaynumber":"8834424829","Transactiontype":"regular"},
           {"name":"Krishnan","Googlepaynumber":"8838955820","Transactiontype":"regular"},
           {"name":"Ram","Googlepaynumber":"8838924866","Transactiontype":"regular"},
           {"name":"Jaanu","Googlepaynumber":"8838924898","Transactiontype":"regular"},
           {"name":"Ramanujam","Googlepaynumber":"88389248277","Transactiontype":"regular"},
           {"name":"Ricky","Googlepaynumber":"8838924880","Transactiontype":"regular"},
           {"name":"Jhonty","Googlepaynumber":"8838924825","Transactiontype":"regular"},
           {"name":"Omar","Googlepaynumber":"8838924866","Transactiontype":"regular"},
           {"name":"Ameer","Googlepaynumber":"8838924800","Transactiontype":"regular"},
           {"name":"Abdur","Googlepaynumber":"8838924877","Transactiontype":"regular"},
           {"name":"Khalim","Googlepaynumber":"88389248278","Transactiontype":"regular"},
           {"name":"Kaaleshwari","Googlepaynumber":"8838924865","Transactiontype":"regular"},
           {"name":"Sam","Googlepaynumber":"8838924833","Transactiontype":"regular"},
           {"name":"Asha","Googlepaynumber":"8838924888","Transactiontype":"regular"},
           {"name":"Hindhu","Googlepaynumber":"8838924800","Transactiontype":"regular"},
           {"name":"Mathavan","Googlepaynumber":"8838924899","Transactiontype":"regular"},
           {"name":"Manuneedhi","Googlepaynumber":"8838924854","Transactiontype":"regular"},
           {"name":"Mannavan","Googlepaynumber":"8838924890","Transactiontype":"regular"},
           {"name":"Muthu","Googlepaynumber":"8838924878","Transactiontype":"regular"},
           {"name":"Karuppu","Googlepaynumber":"8838924856","Transactiontype":"regular"},
           {"name":"Viji","Googlepaynumber":"8838924845","Transactiontype":"regular"},
           {"name":"Lakshmi","Googlepaynumber":"8838924834","Transactiontype":"regular"},
           {"name":"Pooja","Googlepaynumber":"8838924823","Transactiontype":"regular"},
           {"name":"Rajan","Googlepaynumber":"8838924811","Transactiontype":"regular"}]

for i in googlepay:                                                                                                             
    for j,k in i.items():
        print(f"{j}:{k}")

            

            


        


            

        


