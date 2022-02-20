from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Lidosta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    saisinajums = db.Column(db.String(3), nullable=False)
    adrese = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return 'Task %r' % self.id

class Rezervacija(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nolidostas = db.Column(db.String(200), nullable=False)
  uzlidostas = db.Column(db.String(200), nullable=False)
  datumsno = db.Column(db.String(200), nullable=False)

  def __repr__(self):
        return 'Rezervacija %r' % self.id

class Lidmasina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    modelis = db.Column(db.String(200), nullable=False)
    razosanas_gads = db.Column(db.String(3), nullable=False)
    vietu_skaits = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

def __repr__(self):
        return 'Lidmasina %r' % self.id

@app.route('/panel_samoleti.html', methods=['POST', 'GET'])
def lidmasina():
    if request.method == 'POST':
      new_lidmasina = Lidmasina(content=request.form['content'],modelis=request.form['modelis'], razosanas_gads=request.form['razosanas_gads'], vietu_skaits=request.form['vietu_skaits'])
      try:
        db.session.add(new_lidmasina)
        db.session.commit()
        return redirect('/panel_samoleti.html')
      except:
        return 0;
    else:
      tasks = Lidmasina.query.order_by(Lidmasina.date_created).all()
      return render_template('panel_samoleti.html', tasks=tasks,)

@app.route('/delete_airplane/<int:id>')
def delete_plane(id):
    task_to_delete = Lidmasina.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/templates/panel_samoleti')
    except:
        return 0;

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/secondlpp.html')
def secondlpp():
    return render_template("secondlpp.html")

@app.route('/login.html')
def login():
    return render_template("login.html")

@app.route('/register.html')
def register():
    return render_template("register.html")

@app.route('/reservation.html')
def reservation():
    return render_template("reservation.html")

@app.route('/airports.html')
def airports():
    return render_template("footerPages/airports.html")

@app.route('/aboutUs.html')
def aboutUs():
    return render_template("footerPages/aboutUs.html")

@app.route('/advertisingOffer.html')
def advertisingOffer():
    return render_template("footerPages/advertisingOffer.html")

@app.route('/cities.html')
def cities():
    return render_template("footerPages/cities.html")

@app.route('/confidentiality.html')
def confidentiality():
    return render_template("footerPages/confidentiality.html")

@app.route('/countries.html')
def countries():
    return render_template("footerPages/countries.html")

@app.route('/onWeekend.html')
def onWeekend():
    return render_template("footerPages/onWeekend.html")

@app.route('/reference.html')
def reference():
    return render_template("footerPages/reference.html")

@app.route('/settings.html')
def settings():
    return render_template("footerPages/settings.html")

@app.route('/panel.html')
def panel():
    return render_template("panel.html")

@app.route('/latvia.html')
def latvia():
    return render_template("countries/latvia.html")

@app.route('/netherlands.html')
def netherlands():
    return render_template("countries/netherlands.html")

@app.route('/norway.html')
def norway():
    return render_template("countries/norway.html")

@app.route('/romania.html')
def romania():
    return render_template("countries/romania.html")

@app.route('/russia.html')
def russia():
    return render_template("countries/russia.html")

@app.route('/spain.html')
def spain():
    return render_template("countries/spain.html")

@app.route('/usa.html')
def usa():
    return render_template("countries/usa.html")

@app.route('/panel_reisi.html')
def panel_reisi():
    return render_template("panel_reisi.html")

app.run(host='0.0.0.0', port=8080)