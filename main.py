from App import create_app
App = create_app()
if __name__ == '__main__':
    App.run(host = '0.0.0.0', port=5000, debug=True)