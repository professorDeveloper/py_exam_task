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
{
    "users": [
        {
            "username": "username",
            "password": "password",
            "address": "address",
            "numbers": [
                {
                    "id": 1,
                    "number": 12345678,
                    "price": 10000,
                    "isSold": true
                }
            ]
        }
    ],
    "numbers": [
        {
            "id": 1,
            "number": 12345678,
            "price": 10000,
            "isSold": true
        }
    ],
    "admins": [
        {
            "pinCode": 1234
        }
    ]
}

`````
## **Note**
### - **PinCode** : 1234