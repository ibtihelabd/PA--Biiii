import os
# os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'  
# import json
# import numpy as np
from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS  # Add CORS support
# from groq import Groq
# from transformers import AutoTokenizer, AutoModel
# from faiss import read_index, write_index, IndexFlatL2
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes




@app.route("/")
def index():
    return render_template("index.html")   # Ton site principal

@app.route("/dash")
def dashbod():
    # URL du rapport Power BI que vous avez partagé
    #powerbi_embed_url = "https://app.powerbi.com/reportEmbed?reportId=a489d90c-4a78-4fdd-bedc-6995bab25f5d&autoAuth=true&ctid=604f1a96-cbe8-43f8-abbf-f8eaf5d85730"
    

    
    
    return render_template("Dashbord.html")

if __name__ == "__main__":
    app.run(debug=True)