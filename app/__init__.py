import os
from dotenv import load_dotenv
from flask import Flask
from .api import api_blueprint
from .cli import register_cli
from .dashapp import create_dash_application


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config['EMBEDDING_PROVIDER'] = os.environ.get('EMBEDDING_PROVIDER')
    app.config['LLM_PROVIDER'] = os.environ.get('LLM_PROVIDER')
    app.config['LLM_MODEL'] = os.environ.get('LLM_MODEL')
    app.config['ANTHROPIC_API_KEY'] = os.environ.get('ANTHROPIC_API_KEY')
    app.config['VOYAGE_API_KEY'] = os.environ.get('VOYAGE_API_KEY')
    app.config['OPENAI_API_KEY'] = os.environ.get('OPENAI_API_KEY')
    app.config['ACTIVELOOP_TOKEN'] = os.environ.get('ACTIVELOOP_TOKEN')
    app.config['ACTIVELOOP_USERNAME'] = os.environ.get('ACTIVELOOP_USERNAME')
    app.config['REPO_URL'] = os.environ.get('REPO_URL')
    app.config['VECTORDB_NAME'] = os.environ.get('VECTORDB_NAME')
    app.register_blueprint(api_blueprint)
    register_cli(app)
    create_dash_application(app)
    return app
