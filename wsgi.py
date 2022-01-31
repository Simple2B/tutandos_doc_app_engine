#!/.venv/bin/python

from dotenv import load_dotenv
from app import create_app

load_dotenv()

app = create_app()


# flask cli context setup
@app.shell_context_processor
def get_context():
    """Objects exposed here will be automatically available from the shell."""
    return dict(app=app)


if __name__ == "__main__":
    app.run()
