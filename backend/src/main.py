from flask import Flask, render_template
from restapi.account_app import account_bp
from flask_cors import CORS

from restapi.project_app import project_bp
from restapi.story_app import story_bp
from restapi.sprint_app import sprint_bp
from restapi.task_app import task_bp
from restapi.task_status_app import task_status_bp
from restapi.project_group_app import project_group_bp
from restapi.authority_app import authority_bp
from restapi.page_app import page_bp
from restapi.project2_app import project2_bp
from restapi.story2_app import story2_bp
from restapi.sprint2_app import sprint2_bp
from restapi.task2_app import task2_bp
from restapi.task_status2_app import task_status2_bp
from restapi.project_group2_app import project_group2_bp
from restapi.authority2_app import authority2_bp
from restapi.page2_app import page2_bp
from restapi.project3_app import project3_bp

from session import session_pool

app = Flask(__name__, static_folder='../../frontend/dist/static',
            template_folder='../../frontend')
app.register_blueprint(account_bp)
app.register_blueprint(project_bp)
app.register_blueprint(story_bp)
app.register_blueprint(sprint_bp)
app.register_blueprint(task_bp)
app.register_blueprint(task_status_bp)
app.register_blueprint(project_group_bp)
app.register_blueprint(authority_bp)
app.register_blueprint(page_bp)
app.register_blueprint(project2_bp)
app.register_blueprint(story2_bp)
app.register_blueprint(sprint2_bp)
app.register_blueprint(task2_bp)
app.register_blueprint(task_status2_bp)
app.register_blueprint(project_group2_bp)
app.register_blueprint(authority2_bp)
app.register_blueprint(page2_bp)
app.register_blueprint(project3_bp)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
