from flask import Flask, request, jsonify, abort, render_template
import uuid

app = Flask(__name__)

# In-memory storage for secrets
secrets_store = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    secret = request.form.get('secret') 
   
    if not secret:
        return render_template('index.html', error='No secret provided')

    if len(secret) > 500:
        return render_template('index.html', error='Secret is too long')
    
    if len(secret) <= 1:
        return render_template('index.html', error='Secret is too short')

    if not secret.isalnum():
        return render_template('index.html', error='Secret contains invalid characters')
    
    secret_id = str(uuid.uuid4())
    secrets_store[secret_id] = {'secret': secret, 'used': False}
    
    return render_template('index.html', link=f'/read/{secret_id}')

@app.route('/read/<secret_id>', methods=['GET'])
def read(secret_id):
    secret_data = secrets_store.get(secret_id)
    
    if not secret_data:
        return jsonify({'error': 'Secret not found'}), 404
    
    if secret_data['used']:
        return jsonify({'error': 'This link has already been used once'}), 400
    
    secret_data['used'] = True
    
    return render_template('index.html', secret=secret_data['secret'])

if __name__ == '__main__':
    app.run(debug=True)