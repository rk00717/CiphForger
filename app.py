from flask import Flask, render_template, request
from engine import PassGenerator, CryptoTable

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        platform_name = str(request.form.get('platform_name', ""))
        username = str(request.form.get('username', ""))

        table_size = int(request.form.get('table_size', 0))
        length = int(request.form.get('length', 0))
        salt_1 = int(request.form.get('salt_1', 0))
        salt_2 = int(request.form.get('salt_2', 0))

        use_upper = 'upper' in request.form
        use_lower = 'lower' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form

        cryptoTable = CryptoTable(table_size)
        generator = PassGenerator(length, salt_1, salt_2)

        password = str("")
        if not(table_size == 0 or length == 0 or salt_1 == 0 or salt_2 == 0) :
            password = generator.generate_password(cryptoTable.table, platform_name, username)

        return render_template('index.html', password=password)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)