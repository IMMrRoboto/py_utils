
# coding: utf-8

# In[1]:
import pickle
import networkx as nx
import CRUD_Graph as crud

from flask import Flask, request, render_template, flash
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DEBUG = True

app = Flask(__name__)


teams = []
okrs = []
members = []
key_results = []

def update_nodes():
    global teams, okrs, members, key_results
    G = crud.load_graph()

    ND = G.nodes(data=True)
    teams = []
    okrs = []
    members = []
    key_results = []

    for (n, d) in ND:
        if d['type'] == "Team" or d['type'] == "Root":
            teams.append(G.nodes()[n])
        if d['type'] == "OKR":
            okrs.append(G.nodes()[n])
        if d['type'] == "Key_Result":
            key_results.append(G.nodes()[n])
        if d['type'] == "Member":
            members.append(G.nodes()[n])

class TeamForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    parent = TextField('parent:', validators=[validators.required()])
    relationship = TextField('relationship:', validators=[validators.required()])
    description = TextField('description:')
    pulse = TextField('pulse:')
    confluence = TextField('confluence:')
    github = TextField('Name:')

class OKRForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    parent = TextField('Name:', validators=[validators.required()])
    relationship = TextField('Name:', validators=[validators.required()])



@app.route("/")
def landing():
    update_nodes()

    return render_template("index.html",
                            heading="Update the graph",
                            teams=teams,
                            okrs=okrs,
                            key_results=key_results,
                            members=members
    )

@app.route("/teams", methods=['GET', 'POST'])
def teams_route():
    update_nodes()
    form = TeamForm(request.form)
    # print(teams)
    # print form.errors
    if request.method == 'POST':
        name=request.form['name']
        parent=request.form['parent']
        relationship=request.form['relationship']
        description=request.form['description']
        pulse=request.form['pulse']
        confluence=request.form['confluence']
        github=request.form['github']

        if name != '' and parent != '' and relationship != '':
            crud.add_team(name, parent, relationship, description, pulse, confluence, github)

    return render_template("team_index.html",
                            heading="Update the graph",
                            teams=teams,
                            form=form
    )

@app.route("/OKRForm", methods=['GET', 'POST'])
def _route():
    update_nodes()

    form = TeamForm(request.form)

    # print form.errors
    if request.method == 'POST':
        name=request.form['name']
        # password=request.form['password']
        # email=request.form['email']
        print(name)

    return render_template("index.html",
                            heading="Update the graph",
                            teams=teams,
                            okrs=okrs,
                            key_results=key_results,
                            members=members,
                            form=form
    )

if __name__ == "__main__":
    app.run(port=8989, debug=True)
