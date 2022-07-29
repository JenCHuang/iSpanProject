from flask import Flask, render_template, request, url_for
from flask_moment import Moment
from datetime import datetime
from pathlib import Path
import uuid

# practice start
from recognition.load_model import recog_digit
# practice end

app = Flask(__name__)
moment = Moment(app)

# practice start
UPLOAD_FOLDER = Path(__file__).resolve().parent/'static/uploaded'
# practice end

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header",
                           current_time=datetime.utcnow())

# practice start
@app.route('/file', methods=['GET', 'POST'])
def get_file():
    if request.method == "GET":
        return render_template('file(practice).html', page_header="upload file")
    elif request.method == "POST":
        file = request.files['fileinfo'] 
        if file:
            filename = file.filename
            # filename = str(uuid.uuid4())+"_"+file.filename
            file.save(UPLOAD_FOLDER/filename)
            result = recog_digit(filename)
            
        return render_template('recog_result(practice).html', page_header="result", result=result, img=filename)
# practice end


if __name__ == "__main__":
    app.run(debug=True)



