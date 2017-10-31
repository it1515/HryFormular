"""
Logic for dashboard related routes
"""
from flask import Blueprint, render_template,redirect,url_for,flash
from .forms import LogUserForm, secti,masoform,TestForm,HryForm,VyvojarForm
from ..data.database import db
from ..data.models import LogUser,Emaily,Hry,Vyvojari
blueprint = Blueprint('public', __name__)

@blueprint.route('/', methods=['GET'])
def index():
    return render_template('public/index.tmpl')

@blueprint.route('/loguserinput',methods=['GET', 'POST'])
def InsertLogUser():
    form = LogUserForm()
    if form.validate_on_submit():
        LogUser.create(**form.data)
    return render_template("public/LogUser.tmpl", form=form)

@blueprint.route('/loguserlist',methods=['GET'])
def ListuserLog():
    pole = db.session.query(LogUser).all()
    return render_template("public/listuser.tmpl",data = pole)

@blueprint.route('/secti', methods=['GET','POST'])
def scitani():
    form = secti()
    if form.validate_on_submit():
        return render_template('public/vystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/secti.tmpl', form=form)

@blueprint.route('/maso', methods=['GET','POST'])
def masof():
    form = masoform()
    if form.validate_on_submit():
        return render_template('public/masovystup.tmpl',hod1=form.hodnota1.data,hod2=form.hodnota2.data,suma=form.hodnota1.data+form.hodnota2.data)
    return render_template('public/maso.tmpl', form=form)

@blueprint.route('/testForm', methods=['GET','POST'])
def Formular():
    form = TestForm()
    if form.validate_on_submit():
        Emaily.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/testForm.tmpl', form=form)

@blueprint.route('/testList', methods=['GET'])
def FormularList():
    pole = db.session.query(Emaily).all()
    return render_template('public/testList.tmpl', pole=pole)

@blueprint.route('/smazEmail/<id>', methods=['GET'])
def FormularDel(id):
    iddel = db.session.query(Emaily).filter_by(id=id).first()
    Emaily.delete(iddel)
    return redirect(url_for('public.FormularList'))

@blueprint.route('/hry', methods=['GET','POST'])
def FormularHry():
    form = HryForm()
    if form.validate_on_submit():
        Hry.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/hryForm.tmpl', form=form)

@blueprint.route('/hryList', methods=['GET'])
def FormularHryList():
    pole = db.session.query(Hry).all()
    return render_template('public/hryList.tmpl', pole=pole)

@blueprint.route('/smazHru/<id>', methods=['GET'])
def FormularHryDel(id):
    hra = db.session.query(Hry).filter_by(id=id).first()
    Hry.delete(hra)
    return redirect(url_for('public.FormularHryList'))

@blueprint.route('/upravHru/<id>', methods=['GET','POST'])
def FormularHryEdit(id):
    hra = db.session.query(Hry).filter_by(id=id).first()
    form=HryForm(obj=hra)
    if form.validate_on_submit():
        Hry.delete(hra)
        Hry.create(**form.data)
        return redirect(url_for('public.FormularHryList'))
    return render_template("public/hryForm.tmpl", action="Edit", form=form)

@blueprint.route('/vyvojari', methods=['GET','POST'])
def FormularVyvojari():
    form = VyvojarForm()
    if form.validate_on_submit():
        Vyvojari.create(**form.data)
        flash("Ulozeno",category="INFO")
    return render_template('public/vyvojarForm.tmpl', form=form)

@blueprint.route('/vyvojariList', methods=['GET'])
def FormularVyvojariList():
    pole = db.session.query(Vyvojari).all()
    return render_template('public/vyvojariList.tmpl', pole=pole)

@blueprint.route('/smazVyvojare/<id>', methods=['GET'])
def FormularVyvojariDel(id):
    vyvojar = db.session.query(Vyvojari).filter_by(id=id).first()
    Hry.delete(vyvojar)
    return redirect(url_for('public.FormularVyvojariList'))

@blueprint.route('/upravVyvojare/<id>', methods=['GET','POST'])
def FormularVyvojariEdit(id):
    vyvojar = db.session.query(Vyvojari).filter_by(id=id).first()
    form=VyvojarForm(obj=vyvojar)
    if form.validate_on_submit():
        Vyvojari.delete(vyvojar)
        Vyvojari.create(**form.data)
        return redirect(url_for('public.FormularVyvojariList'))
    return render_template("public/vyvojarForm.tmpl", action="Edit", form=form)