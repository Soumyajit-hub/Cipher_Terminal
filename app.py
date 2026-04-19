from flask import Flask, render_template, request

app = Flask(__name__)

# YOUR ORIGINAL CIPHER LOGIC
def caesar_cipher(text, shift, mode):
    result = ""
    if mode == "decrypt":
        shift = -shift
    for char in text:
        if 'a' <= char <= 'z':
            start = ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        elif 'A' <= char <= 'Z':
            start = ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

# THE WEB ROUTE
@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    user_text = ""
    if request.method == "POST":
        # Get data from the HTML form
        user_text = request.form.get("message")
        shift_val = int(request.form.get("shift"))
        choice = request.form.get("mode")
        
        # Run the cipher
        output = caesar_cipher(user_text, shift_val, choice)
    
    return render_template("index.html", result=output, original=user_text)

if __name__ == "__main__":
    app.run()    