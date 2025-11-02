from flask import Flask, request, jsonify
from underthesea import word_tokenize

# Khởi tạo Flask app
app = Flask(__name__)

# Các từ ngữ cần kiểm duyệt
BAD_WORDS = ["bạo lực", "khiêu dâm", "đánh đập"]

# Hàm kiểm tra nội dung có chứa từ xấu không
def contains_bad_words(text):
    text = text.lower()
    for word in BAD_WORDS:
        if word in text:
            return True
    return False

# Tạo API kiểm tra nội dung
@app.route('/detect', methods=['POST'])
def detect():
    content = request.json.get('text', '')
    is_bad = contains_bad_words(content)
    return jsonify({'is_bad': is_bad})

# Lắng nghe cổng 5000
if __name__ == '__main__':
    app.run(port=5000)