from model.user import User,TypeUser


class UserService:
    def __init__(self):
        self.userList=[]
        self.userList.append(User({"email":"jaruiz93977@umanizales.edu.co",
                                   "password":"123"},1,TypeUser("1","Administrador")))


    def get_users(self):
        list = []
        for user in self.userList:
            list.append(user.toUserDTO())
        return list

    def validate_email(self, email:str,admin:bool,cant_player:int):
        cont=0
        for user in self.userList:
            if user.email == email:
                return True
            if admin and user.type_user.code==1:
                return True
            if user.type_user.code==2:
                cont+=1
        if admin==False and cant_player==cont:
            return True
        return False

    def create_user(self, data):
        admin = False
        if data("type_user")("code")==1:
            admin = True
        if self.validate_email(data["email"],True,2):
            raise Exception("No cumple las condiciones para adicionar el ususario")


    def login(self, email, password):
        for user in self.userList:
            if email == user.email and password == user.password:
                return user
        return None
