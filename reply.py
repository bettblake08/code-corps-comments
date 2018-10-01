# Reply.py

from datetime import datetime


class Reply(object):
    """docstring for Reply"""

    def __init__(self, data={}):
        self.data = data
        self.reply = data.get('comment_id')
        self.message = data.get('message')
        self.author = data.get('author')
        self.role = data.get('role')
        self.timestamp = datetime.utcnow()
        self.comments = [
            {'author': 'dennis', 'message': 'Message to edit', 'timestamp': self.timestamp, 'comment_id': 1, 'user_id': 1}]
        self.userDetails = [
            {'user_id': 1, 'author': 'dennis', 'role': 1, 'status': True}]

    def get_by_id(self, comment_id):
        for comment in self.comments:
            if comment_id == comment['comment_id']:
                return comment

    def get_user(self):
        for user in self.userDetails:
            if user['status'] == True:
                return user

    def postReply(self, comment_id):
        comment_to_reply = self.get_by_id(comment_id)
        if not comment_to_reply:
            print("Invalid comment id")
        else:
            message = raw_input("Enter reply message: ")
            time = self.timestamp
            user = self.get_user()
            author = user['author']
            reply_message = {'Reply': message,
                             'Time': time, 'Author': author, 'Comment id': comment_id}
            rep = self.comments.append(reply_message)
            print(self.comments)

    def edit(self, comment_id):
        comment_to_edit = self.get_by_id(comment_id)
        if not comment_to_edit:
            print("Invalid comment id")
        else:
            user = self.get_user()
            if user == False:
                print("Not loggedIn")
            elif (user['author'] == 'dennis') and (user['role'] == 1):
                message == raw_input("Enter edit message: ")
                if not message:
                    print("Message can't be blank")
                comment_to_edit['Message'] = message
            elif (user['author'] == 'moderator') and (user['role'] == 2):
                message == raw_input("Enter reply")
                comment_to_edit['Message'] = message
                if not message:
                    print("Message can't be blank")
                comment_to_edit['message'] = message
            elif user['role'] == 3:
                message == raw_input("Enter reply: ")
                if not message:
                    print("Message can't be blank")
                comment['message'] = message
            else:
                print("User Anauthorized")

    def delete(self, comment_id):
        comment_to_delete = self.get_by_id(comment_id)
        if not comment_to_delete:
            print("Invalid comment id")
        else:
            if self.get_user == False:
                print("Not loggedIn")
            if self.get_user['role'] == 1:
                print("Anauthorized access")
            elif self.get_user['role'] == 2 or 3:
                self.comments.pop(comment_to_delete)

rep = Reply()
rep.postReply(1)
