from flask import Flask, request
import rsa_module as rsa

app = Flask(__name__)

@app.route('/encrypt')
def encrypt_route():
    plaintext = request.args.get('plaintext')
    public_key = request.args.get('public_key')
    return rsa.main_encrypt(plaintext, eval(public_key))

@app.route('/decrypt')
def decrypt_route():
    ciphertext = request.args.get('ciphertext')
    private_key = request.args.get('private_key')
    return rsa.main_decrypt(ciphertext, eval(private_key))

@app.route('/generate_keys')
def generate_keys():
    return rsa.generate_keys()
#host='0.0.0.0', port=80, debug=True
app.run()
