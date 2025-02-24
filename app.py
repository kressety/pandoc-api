from flask import Flask, request, send_file, jsonify
import pypandoc
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/app/uploads'
app.config['OUTPUT_FOLDER'] = '/app/outputs'

# 确保上传和输出文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

def get_content_type(output_format):
    content_types = {
        'pdf': 'application/pdf',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'html': 'text/html',
        'html4': 'text/html',
        'html5': 'text/html',
        'markdown': 'text/markdown',
        'markdown_github': 'text/markdown',
        'markdown_mmd': 'text/markdown',
        'markdown_phpextra': 'text/markdown',
        'markdown_strict': 'text/markdown',
        'gfm': 'text/markdown',
        'commonmark': 'text/markdown',
        'commonmark_x': 'text/markdown',
        'djot': 'text/markdown',
        'latex': 'application/x-latex',
        'texinfo': 'application/x-texinfo',
        'beamer': 'application/x-latex',
        'bibtex': 'application/x-bibtex',
        'biblatex': 'application/x-bibtex',
        'csljson': 'application/json',
        'json': 'application/json',
        'odt': 'application/vnd.oasis.opendocument.text',
        'opendocument': 'application/vnd.oasis.opendocument.text',
        'rtf': 'application/rtf',
        'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'epub': 'application/epub+zip',
        'epub2': 'application/epub+zip',
        'epub3': 'application/epub+zip',
        'fb2': 'application/xml',
        'docbook': 'application/docbook+xml',
        'docbook4': 'application/docbook+xml',
        'docbook5': 'application/docbook+xml',
        'jats': 'application/xml',
        'jats_archiving': 'application/xml',
        'jats_articleauthoring': 'application/xml',
        'jats_publishing': 'application/xml',
        'tei': 'application/xml',
        'ipynb': 'application/json',
        'rst': 'text/x-rst',
        'asciidoc': 'text/asciidoc',
        'asciidoc_legacy': 'text/asciidoc',
        'asciidoctor': 'text/asciidoc',
        'mediawiki': 'text/x-wiki',
        'dokuwiki': 'text/x-wiki',
        'xwiki': 'text/x-wiki',
        'zimwiki': 'text/x-wiki',
        'org': 'text/x-org',
        'textile': 'text/x-textile',
        'typst': 'text/plain',
        'plain': 'text/plain',
        'ansi': 'text/plain',
        'man': 'application/x-troff-man',
        'ms': 'application/x-troff-ms',
        'chunkedhtml': 'text/html',
        'icml': 'application/xml',
        'jira': 'text/plain',
        'muse': 'text/plain',
        'native': 'application/json',
        'opml': 'text/x-opml',
        'revealjs': 'text/html',
        's5': 'text/html',
        'slideous': 'text/html',
        'slidy': 'text/html',
        'dzslides': 'text/html',
    }
    return content_types.get(output_format, 'application/octet-stream')

@app.route('/convert', methods=['POST'])
def convert():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file:
        to_format = request.args.get('to', None)
        if not to_format:
            return "Output format not specified", 400
        filename = file.filename
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(input_path)
        try:
            output_filename = f"output.{to_format}"
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
            pypandoc.convert_file(input_path, to_format, outputfile=output_path)
            content_type = get_content_type(to_format)
            return send_file(output_path, mimetype=content_type)
        except Exception as e:
            return f"Conversion failed: {str(e)}", 500
    return "Invalid request", 400

@app.route('/formats', methods=['GET'])
def list_formats():
    try:
        input_formats, output_formats = pypandoc.get_pandoc_formats()
        format_combinations = {fmt: output_formats for fmt in input_formats}
        return jsonify(format_combinations)
    except Exception as e:
        return f"Failed to retrieve formats: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))