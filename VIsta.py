from flask import Flask, render_template, request, redirect,url_for
from forms import *

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['SECRET_KEY'] = 'los cosos'    
app.static_folder = 'static'

@app.route('/',methods=["GET", "POST"])
def MenuMetodos():
    form = SelectorMetodos()
    if form.validate_on_submit():
        metodo = form.metodo.data
        print(metodo)
        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('Inicio.html'))
    return render_template('Inicio.html',form=form)

if __name__ == '__main__':
    app.run()
