import os 
from flask import Flask, flash, request, jsonify

ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)

def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''@app.route("/files", methods=["GET"])
def files():
   return jsonify([{'message': 'ola'}])'''

@app.route("/files", methods=["POST"])
def upload():
   if request.files: 
      '''and request.files["file"]:'''

      uploadFile = request.files["file"]

      if not allowed_file(uploadFile.filename):
         return jsonify([{'Message': 'No permissions for you'}])
	
      return jsonify([{'content': uploadFile.read().decode("utf-8")}])
   return jsonify([{'Message': 'No permission'}])

if __name__ == '__main__':
   app.run(debug=True)