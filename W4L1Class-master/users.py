from mysqlconnection import connectToMySQL


class User:

    db="facegram"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.password=data['password']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query="SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        print(results)
        users =[]
        for row in results:
            users.append(cls(row)) #feeds into the constructor on line 8.
        return users

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO users(first_name,last_name,email,password) 
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s);
        """ # """ allows you to break up the line of code into multiple lines.
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def get_one_by_email(cls,email):
        data={
            'email':email
        }
        query="""
        SELECT * FROM users WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])