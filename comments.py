from datetime import datetime

class Comment:
    normal = 1
    moderator = 2
    admin = 3

    def __init__(self, data={}):
        self.data = data
        self.id = data.get('id')
        self.author_id = data.get('author_id')
        self.message = data.get('message')
        self.timestamp = datetime.utcnow()
        self.parent_id = data.get('parent_id')
        self.list = []
        self.user = {'username':'nesh', 'password':'thestate', 'role':1, 'status':'loggedin'}


    def authenticated(self):
        if self.user['status'] == 'loggedin':
            return True
        return False
        
    def save(self):
        if self.authenticated:
            self.list.append(self.data)
            print(self.list)
        else:
            print('please login')

    def get_by_id(self, id):
        for i in self.list:
            if i['id'] == id:
                return i

    def get_list(self):
        return self.list

    def edit(self, data, id):
        
        if self.user['role'] == 1:
            comment_to_edit = self.get_by_id(id)
            
            if comment_to_edit:
                if self.user['role'] == 2:
                    print('moderator cannot edit comment')
                elif (self.user['role']  or self.user['role'] ) and self.authenticated:
                    comment_to_edit.update(self.data) 
                    print(comment_to_edit)
                elif self.authenticated() == False:
                    print ({"message":"please signin"})
            else:
                print ("no item with id")
        elif self.user['role'] :
            comment_to_edit = self.get_by_id(id)
            if comment_to_edit:
                if (self.user['role'] and self.user['role'] ):
                    comment_to_edit.update(self.data) 
                    print(comment_to_edit)
                elif self.user['role']:
                    print("you cannot edit this comment")
                elif self.authenticated() == False:
                    print ({"message":"please signin"})
            else:
                print ("no item with id")

        elif self.user['role'] == 3:
            comment_to_edit = self.get_by_id(id)
            if comment_to_edit:
                if (self.user['role'] == 1 and self.user['role']  == 2):
                    print('moderator and normal user cannot edit comment')
                elif self.user['role']  == 3:
                    comment_to_edit.update(self.data) 
                    print(comment_to_edit)
                elif self.authenticated() == False:
                    print ({"message":"please signin"})
            else:
                print ("no item with id")
            
    def delete(self,id):
        comment_to_delete = self.get_by_id(id)
        if comment_to_delete:
            if self.user['role']  == 1:
                print('normal user cannot delete')
            elif self.user['role']  == 3 or self.user['role']  == 2 and self.authenticated:
                deleted_list = list(filter(lambda x:x['id'] != id, self.list))
                print (deleted_list)
            elif self.authenticated == False:
                print ("please signin")
        print("no item with id")

timestamp = datetime.utcnow()
data = {'id':1, 'author_id':1, 'message':'This is a commnet', 'timestamp':timestamp}
data_edited = {'id':1, 'author_id':1, 'message':'I already had a comment', 'timestamp':timestamp}

comment = Comment(data)
comment.save()



comment2 = comment.edit(data_edited,1)
comment3 = comment.delete(1)


print(comment3)
        

        
        


        


