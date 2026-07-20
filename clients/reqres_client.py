# clients/reqres_client.py
class ReqResClient:
    def __init__(self, request_context):
        self.request = request_context

    def get_user(self, user_id):
        return self.request.get(f"users/{user_id}")

    def create_user(self, name, job):
        return self.request.post("users/", data={"name": name, "job": job})

    def login(self, email, password):
        return self.request.post("login/", data={"email": email, "password": password})