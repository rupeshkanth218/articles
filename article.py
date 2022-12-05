from flask import Flask,render_template

app=Flask(__name__)




@app.route("/")
def home():
    posts=[{'title':"Worldcup 2023",'Content':"The FIFA worldcup started this week in Doha, Qatar. First match was played between Qatar and Ecuador ","image":'img1.png'},
        {'title':"New Robot made","Content": "A brand New robot which is indistinguishable from human is no available to buy.","image":'img2.jpeg'},
        {'title':"A cafe where robot serves!!","Content":"A brand new Cafe in Dubai is open for service. A robot take order and serves delicious coffee.","image":'img3.jpeg'},
        {'title':"Python 3.11","Content":" Python 3.11 released.Experts say it is very fast compared to previous version.","image":'img4.png'}
    ]
    return render_template("home.html",posts=posts)


@app.route("/aboutme")
def about():
    return render_template("about.html")


app.run(debug=True)