from locust import User , task , constant

class MyUser(User):
    weight = 2
    wait_time = constant(1)
    @task
    def launch(self):
        print("launching the URL")

    @task 
    def search(self):
        print("Searching")   

class MysecondUser(User):
    weight = 2
    wait_time = constant(1)
    @task
    def comment(self):
        print("Posting a comment")

    def view(self):
        print("Viewing")    
