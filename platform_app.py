from interface_platform import create_app

if __name__ == '__main__':
    app = create_app("develop")
    app.run(host='0.0.0.0',port=8081,debug=True)
