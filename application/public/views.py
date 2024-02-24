import os
import json
import uuid
from datetime import datetime
from datetime import time

#   importing basic flask module
from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from flask import abort
from flask import jsonify
from flask import make_response
from flask import current_app
from flask import send_file
import pandas as pd


public = Blueprint('public', __name__)

@public.route('/')
def index():
    return render_template('public/index.html')

@public.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return render_template('public/index.html', message='No file part')

    file = request.files['file']

    if file.filename == '':
        return render_template('public/index.html', message='No selected file')

    if file:
        # Read the uploaded file and process the data
        data = file.read().decode('utf-8').splitlines()
        processed_data = process_data(data)

        # Create an Excel file
        excel_data = pd.DataFrame(processed_data)
        filename = f'{uuid.uuid4().hex}.xlsx'
        excel_path = os.path.join(current_app.root_path, 'static/result/', filename)
        excel_data.to_excel(excel_path, index=False, header=False)

        # Pass both processed data and Excel file path to the result template
        return render_template('public/result.html', data=processed_data, excel_path=filename)

    
@public.route('/download/<string:file_name>', methods=['GET', 'POST'])
def download(file_name):
    excel_path = os.path.join(current_app.root_path, 'static/result', file_name)
    return send_file(excel_path, as_attachment=True)


def process_data(data):
    processed_data = []

    for i in range(0, len(data), 8):
        # Check if there are enough lines left in data
        if i + 8 <= len(data):
            voter_info = {}
            
            # Extract the serial number (ক্রোমিক নং)
            serial_number = data[i].strip()
            print('serial --> ', serial_number)
            voter_info['ক্রোমিক নং'] = serial_number

            for j in range(1, 8):  # Start from 1 to skip the serial number line
                line = data[i + j]
                if ':' in line:
                    key, value = line.split(':', 1)
                    voter_info[key.strip()] = value.strip()
                else:
                    # Handle the case when ":" is not present in the line
                    print(f"Warning: ':' not found in line {i + j + 1}: {line}")

            processed_data.append(voter_info)
        else:
            # Handle the case when there are not enough lines
            print(f"Error: Not enough lines to process starting from index {i}")

    return processed_data
