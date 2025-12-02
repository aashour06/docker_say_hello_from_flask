from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name', 'Ashour')
        return f"<h1>Hello {name}</h1><a href='/'>Back</a>"
    return """
        <h1>Simple Flask Form</h1>
        <form method="POST">
            <label>Your name:</label>
            <input type="text" name="name" />
            <button type="submit">Send</button>
        </form>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
