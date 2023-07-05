from flask import Flask
from src.middleware.authentication import auth_middleware
from src.middleware.errorHandler import error_handler
from src.routes.userRoutes import user_routes
from src.routes.contactRoutes import contact_routes
from src.routes.activityRoutes import activity_routes

app = Flask(__name__)

# Middleware
app.wsgi_app = auth_middleware(app.wsgi_app)
app.register_error_handler(Exception, error_handler)

# Routes
app.register_blueprint(user_routes)
app.register_blueprint(contact_routes)
app.register_blueprint(activity_routes)

if __name__ == "__main__":
    app.run(debug=True)