from flask import Flask

def create_app():
    app = Flask(__name__)

    # Configuración de la app (si tienes configuraciones adicionales)
    app.config['SECRET_KEY'] = 'tu_clave_secreta'

    # Registra tus rutas aquí (ejemplo):
    from .routes import main
    app.register_blueprint(main)

    return app
