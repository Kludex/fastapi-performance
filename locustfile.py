from locust import HttpUser, task


class Page(HttpUser):
    @task
    def index(self):
        self.client.get("/")
