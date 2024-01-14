from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from datetime import timedelta
from controllers.auth_controller import auth_controller
from controllers.patient_controller import patient_controller
from controllers.visit_controller import visit_controller
import os

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = "$2a$12$zONiXJp/wt6qRIf5H5ZMi.llhUnI95i4iwpV/FQljiL7gYxqdWVTm"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# Patients
app.register_blueprint(patient_controller)

# Visits
app.register_blueprint(visit_controller)
jwt = JWTManager(app)

# Auth
app.register_blueprint(auth_controller)

# Handle Angular Routing
@app.route('/', defaults={'path': ''})
@app.route('/<string:path>')
@app.route('/<path:path>')
def static_proxy(path):
    if os.path.isfile('templates/' + path):
        return send_from_directory('templates', path)
    else:
        return send_from_directory("templates", "index.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)