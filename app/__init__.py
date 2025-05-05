from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Initialize Excel connection for real-time updates
    init_excel_connector()
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app
