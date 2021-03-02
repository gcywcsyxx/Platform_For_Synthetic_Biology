from .router import router

def init_app(app):
    app.register_blueprint(router)
    