from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import tempfile
import io
import pythoncom
import win32com.client
from tqdm import tqdm
import time  
import colorama

colorama.init()
app = Flask(__name__)
CORS(app)

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.docx'):
        return jsonify({'error': 'Only .docx files are supported'}), 400

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.docx') as temp_docx:
            file.save(temp_docx.name)
            docx_path = temp_docx.name
        
        print("\033[92mStarting conversion...\033[0m")
        progress = tqdm(
            total=3,
            desc="\033[92mConversion Progress\033[0m",
            ncols=70,
            bar_format="{l_bar}\033[92m{bar}\033[0m {n_fmt}/{total_fmt}"
        )
         
        progress.set_postfix(step="Loading")
        progress.update(1)

        pdf_path = docx_path.replace('.docx', '.pdf')
        
        pythoncom.CoInitialize()
        word = win32com.client.Dispatch("Word.Application")
        word.Visible = False

        doc = word.Documents.Open(docx_path)
        
        progress.set_postfix(step="Converting")
        doc.SaveAs(pdf_path, FileFormat=17) 
        doc.Close()
        word.Quit()

        progress.set_postfix(step="Saving")
        progress.update(1)
        
        progress.set_postfix(step="Done")
        progress.update(1)

        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()

        os.unlink(docx_path)
        os.unlink(pdf_path)

        return send_file(
            io.BytesIO(pdf_data),
            mimetype='application/pdf',
            as_attachment=True,
            download_name=file.filename.replace('.docx', '.pdf')
        )

    except Exception as e:
        return jsonify({'error': f'Conversion failed: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
