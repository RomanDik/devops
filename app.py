from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Lab #1</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 40px; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
            }
            h1 { color: #ffd700; }
            .status { 
                background: rgba(0,255,0,0.2); 
                padding: 10px; 
                border-radius: 5px; 
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>DevOps Laboratory Work #1</h1>
            <p><strong>Student:</strong> dik</p>
            <p><strong>GitHub Webhooks Auto-Deployment</strong></p>
            
            <div class="status">
                    <strong>Application successfully deployed via GitHub Webhook!</strong>
            </div>
            
            <p>This page is automatically updated when you push to GitHub repository. Try 2</p>
            <p>Webhook URL: http://webhook.dik.course.prafdin.ru</p>
            <p>App URL: http://app.dik.course.prafdin.ru</p>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)