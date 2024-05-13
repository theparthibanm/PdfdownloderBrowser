from flask import Flask, request, render_template, make_response
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    text = request.form['text']
    pdf.multi_cell(0, 10, txt=text)
    response = make_response(pdf.output(dest='S').encode('latin1'))
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'attachment; filename=download.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)
