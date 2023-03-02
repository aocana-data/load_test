import time
from locust import HttpUser , task , between

class UserStart(HttpUser):
    wait_time = between(1,5)

    @task
    def load_local(self):
        self.client.get("http://127.0.0.1:5000")
