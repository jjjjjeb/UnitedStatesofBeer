import json
import simplejson as json
from sqlalchemy import func, create_engine
from flask import (
    Flask, 
    request, 
    render_template, 
    url_for,
    jsonify)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from collections import defaultdict
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Create a connection to our postgress database
engine = create_engine('postgresql+psycopg2://postgres:jbjf8488@localhost/beer_db')

# Use the automap base method to reflect our database into a new one
Base = automap_base()
Base.prepare(engine, reflect=True)
Base.classes.keys()

# Set our tables as local variables
Beer = Base.classes.beer_table
Review = Base.classes.reviews_table
Visitors = Base.classes.visitor_log

#Create a session so we can query the database
session = Session(engine)

# Flask Setup
###################################################
app = Flask(__name__)

# DB Setup
###################################################

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/allbeers')
def allreviews():
    data = session.query(Review.state_id, func.count(Review.state_id))\
        .group_by(Review.state_id).order_by(Review.state_id.asc()).all()

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i][1]

    return render_template('heatmap.html', data=json.dumps(doc))


@app.route('/ipa')
def get_ipa():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%IPA%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id
    """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template("heatmap.html", data=json.dumps(doc))


@app.route('/stout')
def get_stout():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%Stout%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id
    """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template('heatmap.html', data=json.dumps(doc))


@app.route('/porter')
def get_porter():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%Porter%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id
    """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template('heatmap.html', data=json.dumps(doc))

@app.route('/sour')
def get_sour():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%Lambic%'
    OR beer_table.beer_style LIKE '%Gueuze%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id

    """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template('heatmap.html', data=json.dumps(doc))

@app.route('/ale')
def get_ale():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%Ale%'
    OR beer_table.beer_style LIKE '%Barleywine%'
    OR beer_table.beer_style LIKE '%Quadrupel%'
    OR beer_table.beer_style LIKE '%Dubbel%'
    OR beer_table.beer_style LIKE '%Saison%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id

        """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template('heatmap.html', data=json.dumps(doc))

@app.route('/wheatbeer')
def get_wheat():
    data = session.execute("""SELECT reviews_table.state_id, COUNT(reviews_table.state_id)
    FROM reviews_table
    JOIN beer_table ON reviews_table.beer_id = beer_table.beer_id
    WHERE beer_table.beer_style LIKE '%Hefeweizen%'
    OR beer_table.beer_style LIKE '%Weisse%'
    OR beer_table.beer_style LIKE '%Witbier%'
    GROUP BY reviews_table.state_id
    ORDER BY reviews_table.state_id

    """)
    test = {}
    for i in range(0, 51):
        test.update({i: 0})

    for i in data:
        test.update({i[0]: i[1]})

    data = list(test.values())

    with open('../data/states.json') as f:
        doc = json.load(f)

    features = doc['features']
    for i in range(len(features)):
        features[i]['properties']['count'] = data[i]

    return render_template('heatmap.html', data=json.dumps(doc))


@app.route('/breweries')
def brew():
    return render_template('breweries.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        name = request.form["visitorName"]
        style = request.form["beerStyle"]
        lat = request.form["Lat"]
        lon = request.form["Lon"]

        visit = Visitors(name=name, style=style, lat=lat, long=lon)
        session.add(visit)
        session.commit()
        return redirect("/visitormap", code=302)

    return render_template("form.html")

@app.route("/visitormap")
def visit():
    results = session.query(Visitors.name, Visitors.style, Visitors.lat, Visitors.long).all()

    print(results)

    hover_text = [[result[0], result[1]] for result in results]
    lat = [result[2] for result in results]
    lon = [result[3] for result in results]

    visitor_data = [{
        "type": "scattergeo",
        "locationmode": "USA-states",
        "name": "Visitor Logs",
        "lat": lat,
        "lon": lon,
        "text": hover_text,
        "hoverinfo": "text",
        "marker": {
            "size": 15,
            "color": "rgb(140,45,28)",
            "opacity": 0.75,
            "symbol": "circle",
            "line": {
                "color": "rgb(214, 171, 11)",
                "width": 1
            },
        }
    }]
    return render_template("visitor_map.html", data = visitor_data)

if __name__ == '__main__':
    app.run()
