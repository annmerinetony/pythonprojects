def admin_permission(func):
    def inner_fun(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("permission denied")
        else:
            return func(*args, **kwargs)

    return inner_fun


class User:
    def set_user(self, username, role):
        self.user_name = username
        self.role = role

    def print_details(self):
        print(self.user_name, self.role)


class AddCourse:
    @admin_permission
    def set_course(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print_details(self):
        print(self.course_name)


class AddBatch:
    @admin_permission
    def set_batch(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.batch_code = kwargs.get("batch_code")
        self.course = kwargs.get("course")

    def print_detail(self):
        print(self.batch_code, self.course)


user = User()
user.set_user("rahul", "admin")
course = AddCourse()
course.set_course(user=user, course_name="django")
batch = AddBatch()
batch.set_batch(user=user, batch_code="dfty7tdt6", course="django")

course.print_details()
batch.print_detail()
