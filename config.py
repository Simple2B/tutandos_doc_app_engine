import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(object):
    """Base configuration."""

    APP_NAME = "GCP Peritax Auditing"
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.environ.get(
        "SECRET_KEY", "Ensure you set a secret key, this is important!"
    )

    GCP_PROJECT_ID = os.environ.get("GCP_PROJECT_ID") or "Provide GCP project ID"
    GCP_LOCATION = os.environ.get("GCP_LOCATION") or "Provide GCP location ID"
    GCP_TARGET_URL = os.environ.get("GCP_TARGET_URL") or "Provide Target URL"
    GOOGLE_APPLICATION_CREDENTIALS = "peritax-auditing-6d669fbb995d.cred.json"

    @staticmethod
    def configure(app):
        # Implement this method to do further configuration on your app.
        pass


class DevelopmentConfig(BaseConfig):
    """Development configuration."""

    DEBUG = True
    GCP_QUEUE_NAME = "DEV-DOC-GEN-QUEUE"


class TestingConfig(BaseConfig):
    """Testing configuration."""

    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    GCP_QUEUE_NAME = "TEST-DOC-GEN-QUEUE"


class ProductionConfig(BaseConfig):
    """Production configuration."""

    GCP_QUEUE_NAME = "PROD_DOC_GEN_QUEUE"
    WTF_CSRF_ENABLED = True


config = dict(
    development=DevelopmentConfig, testing=TestingConfig, production=ProductionConfig
)
