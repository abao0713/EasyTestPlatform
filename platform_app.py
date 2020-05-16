from interface_platform import create_app
from interface_platform.models.table import InterfaceModel,InterfaceCase
app = create_app(config_name='development')


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6851)
