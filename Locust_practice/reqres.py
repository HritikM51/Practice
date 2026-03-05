from locust import HttpUser , task , constant

class MyUser(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    @task   
    def get_users(self):
        res = self.client.get("/collections/todos/records")
        print(res.status_code)

    @task
    def create_user(self):
        res = self.client.post("collections/todos/records", data={"title": "ship the ui", "completed": "False"})
        print(res.status_code)
  