from locust import HttpUser, between, task

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task(4)
    def get_home(self):
        self.client.get("/home")

    @task(1)
    def get_dashboard(self):
        self.client.get("/dashboard")



