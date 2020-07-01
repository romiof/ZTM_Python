from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)
print(f"{__name__} eu estou aqui")

# Tipagem direta, automatica

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_file(data):
    # Escrevendo em um CSV o contudo do POST que foi armazenado no DICT
    with open('database.txt', mode='a') as database:
        email   = data['email']
        subject = data['subject']
        message = data['message']
        file    = database.write(f"\n{email};{subject};{message}")

def write_csv(data):
    # Escrevendo em um CSV o contudo do POST que foi armazenado no DICT, usando o método de CSV default
    with open('database.csv',  mode='a', newline='') as database2:
        email      = data['email']
        subject    = data['subject']
        message    = data['message']
        csv_writer = csv.writer(database2, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow( [email, subject, message] )


# Subdiretorios manuais

@app.route('/')
@app.route('/index.html')
def root():
    # return 'Hello, World!, My Friend'
    return render_template('index.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# # Testes Avulsos

# @app.route('/pets/')
# def pets():
#     return 'Hello, My Pet!'

# @app.route('/cat/')
# def cat():
#     return 'Get out of here 🎃!'

# @app.route('/bear/')
# def bear():
#     return render_template('index.html')

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico', mimetype='image/vnd.microsoft.icon')

# The Request Object

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            # print(data)
            write_file(data)
            write_csv(data)
            return redirect('/thanks.html')
        except:
            return 'did not save to our database'
    else:
        return 'Something went wrong... try again'

