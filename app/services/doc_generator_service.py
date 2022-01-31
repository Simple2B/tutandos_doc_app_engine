import json
from google.cloud import tasks_v2
from google import auth as g_auth
from google import oauth2 as g_oauth2
from typing import Union
from uuid import uuid4
import os
from flask_jwt_extended import current_user


class DocGenerator:
    def configure(self, conf: Union[object, str]):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = conf.GOOGLE_APPLICATION_CREDENTIALS
        self.task_client = tasks_v2.CloudTasksClient()

        self.task_parent = self.task_client.queue_path(
            conf.GCP_PROJECT_ID,
            conf.GCP_LOCATION,
            conf.GCP_QUEUE_NAME,
        )

        self.task_prototype = {
            "http_request": {
                "http_method": tasks_v2.HttpMethod.POST,
                "url": conf.GCP_TARGET_URL,
                "headers": {"Content-type": "application/json"},
            }
        }

    def generate_doc(self, data: dict):
        uuid = str(uuid4())
        data["uuid"] = uuid
        data["user"] = current_user.uid
        self.task_prototype["http_request"]["body"] = json.dumps(data).encode()

        auth_req = g_auth.transport.requests.Request()
        jwt_token = g_oauth2.id_token.fetch_id_token(
            auth_req,
            self.task_prototype["http_request"]["url"],
        )

        self.task_prototype["http_request"]["headers"]["Authorization"] = f"bearer {jwt_token}"

        request = {
            "parent": self.task_parent,
            "task": self.task_prototype,
        }

        self.task_client.create_task(request=request)
        return uuid
