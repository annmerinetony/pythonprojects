from blog.models import users, posts


def authenticate(**kwargs):
    username = kwargs.get("username")
    email = kwargs.get("email")
    user_data = [user for user in users if user["username"] == username and user["email"] == email]
    return user_data


# def authenticate(username,email):
#     user_data=[user for user in users if user["username"]==username and user["email"]==email]
#     return user_data

# user=authenticate("django","django@gmail.com")

session = {}   #user:Bret


def login_required(fn):
    def wrapper(*args, **kwrags):
        if "user" in session:
            return fn(*args, **kwrags)
        else:
            print("you must login")

    return wrapper

@login_required
def loged_user():
    username= session.get("user")
    user_id=[user["id"] for user in users if user["name"] == username][0]
    return user_id


class SignInView:
    def post(self, *args, **kwargs):
        username = kwargs.get("username")
        email = kwargs.get("email")
        user = authenticate(username=username, email=email)

        if user:
            print("login success")
            session["user"]=username
        else:
            print("invalid credentials")




@login_required
def logout(*args, **kwargs):
    session.pop("user")


sign = SignInView()
sign.post(username="django", email="django@gmail.com")
# print(session)




class PostListView:
    @login_required
    def get(self, *args, **kwargs):
        return posts

# pl=PostListView()
# all_posts=pl.get()
# for p in all_posts:
#     print(p)
# pl=PostListView()
# try:
#     all_posts=pl.get()
# except Exception as e:
#     print(e)

class MyPostsView:
    @login_required
    def get(self, *args, **kwargs):
        # username = session.get("user")
        # user_id = [user["id"] for user in users if user["name"] == username][0]
        userId=loged_user()
        qs=[post for post in posts if post["userId"]==userId]
        return qs
# lg = SignInView()
# lg.post(username="django", email="django@gmail.com")
# po = MyPostsView()
# print(po.get())


class PostCreateView():
    @login_required
    def post(self,*args,**kwargs):
        userId=loged_user()
        title=kwargs.get("title")
        body=kwargs.get("body")
        data={
            "userId":userId,
            "title":title,
            "body":body
        }
        posts.append(data)
        print("post created successfully")

class PostDetailsView():
    @login_required
    def get(self,*args,**kwargs):
        post_id=kwargs.get('post_id')
        qs=[p for p in posts if p.get("id")==post_id]
        return qs
    def put(self,id=None,*args,**kwargs):

        post= [p for p in posts if p.get("id") == id][0]
        title=kwargs.get("title")
        body=kwargs.get("body")
        post["title"]=title
        post["body"] = body
        print(post)



usr=SignInView()
usr.post(username="django",email="django@gmail.com")
pst=PostCreateView()
pst.post(title="mypost",body="this is my new post")
mp=MyPostsView()
print(mp.get())



detail=PostDetailsView()
print(detail.get(post_id=5))

up=PostDetailsView()
print(up.get(post_id=10))
up.put(id=10,title="hi all",body="rdyghfryujkmlm")
print(up)