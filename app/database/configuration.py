dataBaseName= None; #"gestorbd"
userName= None #"root"
userPassword= None #""
connectionPort=None; #3306
server="localhost"

#creando la conexion
dataBaseConnection=f"mysql+mysqlconnector://
{userName}:{userPassword}@{server}:
{connectionPort}/{dataBaseName}"

print(dataBaseConnection)





