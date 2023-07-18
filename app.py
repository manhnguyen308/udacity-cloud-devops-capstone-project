from flask import Flask
app = Flask(__name__)

@app.route('/')
def page():
    html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>My Capstone Project</title>
        </head>
        <body>
            <h1>Hello, welcome to my capstone project!</h1>
        </body>
        </html>
        '''
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True) # specify port=80