## Info About This Exam

### Car Number Shop Project

###

### **Model Structure**
`````
Number : ( id,number,price,status )
User : ( username,password,address,numbers:list[Number] )
Admin : ( pinCode )

`````

### Services of User

- **Login -> ( username, password )**
- **Register - ( username, password, address )**
- **Logout ->  click access for quit**
- **My Account** -> ( username )
- **Edit Profile** -> (username,password,address)
- **Search Number** -> ( number )
- **Buy Number -> ( number )**
- **Number List**
- **Filter Number -> ( price )**
- **My Number List** -> ( number )
- **Delete Account -> ( number )**


### Services of Admin

- **Login -> ( pinCode )**
- **Logout ->  click access for quit**
- **Add Number -> ( Number )**
- **Edit Number -> ( Number )**
- **Delete Number -> ( Number )**
- **Number List** -> **list[Number]**
- **Sold Numbers** -> **list[Number]**
- **Search Number** -> ( number )**
- **User List** -> **list[User]**


## Structure of Data Saver
`````
[
    {
        "login": "213",
        "manzil": "123",
        "parol": "123",
        "my_numbers": []
    },
    {
        "login": "GG",
        "manzil": "GG",
        "parol": "GG",
        "my_numbers": []
    }
]
`````
## **Note**
### - **PinCode** : 1234


# TASK DONE ✔️
