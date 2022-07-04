from Blog_Application.models import users, posts

session={}

def signin_required(fun):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fun(*args,**kwargs)
        else:
            print("u must login")
    return wrapper        
# username = "anu"
# password = "Password@123"
# user = [user for user in users if user["username"] == username and user["password"] == password]
# print(user)
def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user


class SignInView:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password = kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print("success")

        else:
            print("invalid")

class PostView():
    @signin_required
    def get(self,*args,**kwargs):
        return posts
    @signin_required
    def post(self,*args,**kwargs):
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        posts.append(kwargs)
        print(posts)

class MyPostListView:
    @signin_required
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        print(userId)
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post

class PostDetailsView:
    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post
    @signin_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        post=self.get_object(post_id)
        return post
    @signin_required
    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post removed")
            print(len(posts))

    @signin_required
    def put(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=kwargs.get("data")
        instance=self.get_object(post_id)
        if instance:
            post_obj=instance[0]
            post_obj.update(data)
            return post_obj

class LikeView:
    @signin_required
    def get(self,*args,**kwargs):
        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userid=session["user"]["id"]
            post["liked_by"].append(userid)
            print(post)
log=SignInView()
log.post(username="richard",password="Password@123")
like=LikeView()
like.get(postid=6)
# print(session)
# data=PostView()
# print(data.get())
# data.post(postId=9,title='HELLO THERE',CONTENT="bhgfudf",liked_by=[])
myposts=MyPostListView()
print(myposts.get())
post_detail=PostDetailsView()
post_detail.delete(post_id=6)
print(post_detail.get(post_id=2))
data={"title":"hi everyone","content":"vgujjkj"}
post_detail=PostDetailsView()
print(post_detail.put(post_id=5,data=data))