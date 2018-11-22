import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
runoobdb = myclient["runoobdb"]

dblist = myclient.list_database_names()
# dblist = myclient.database_names()
if "runoobdb" in dblist:
    print("数据库已存在！")
else:
    print("数据库不存在")
c_user = runoobdb["user"]
user_gezz = c_user.find_one({"name":"gezz"})
if user_gezz == None:
    print("gezz不在数据库")
    user_gezz = {"name":"gezz","age":20}
    user_gezz = c_user.insert_one(user_gezz)

    if (user_gezz != None):
        print(user_gezz.inserted_id)
else:
    print("gezz在数据库:age:" + str(user_gezz.get("_id")) )