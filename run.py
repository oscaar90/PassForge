from flask import Flask
from app import create_app
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

app = create_app(
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)

if __name__ == '__main__':
    app.run(debug=True)
