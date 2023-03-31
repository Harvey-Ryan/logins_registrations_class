from flask import Flask,render_template,request,redirect,session
from users import User
app = Flask(__name__)
app.secret_key="supersecretpizza"

#users = [] #save to a list

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():

    if request.form['action'] == 'register':
        data={                                    ##############################
            'first_name': request.form['f_name'], # Collects data and sends to #
            'last_name':request.form['l_name'],   #       the DB via the       #
            'email':request.form['email'],        #    following save method   #
            'password':request.form['password'],  ##############################
        }

        id = User.save(data)
        print(f"THIS IS THE ID: {id}")
        session['user_id'] = id
        return redirect("/dash")
    else:
        this_user = User.get_one_by_email(request.form['email']) ######################
        if not this_user:                                        #        Login       #
            return redirect('/')                                 #        Logic       #
        if this_user.password == request.form['password']:       ######################
            session['user_id'] = this_user.id
            return redirect('/dash')
    return redirect("/")


@app.route("/dash")
def dash():
    users = User.get_all()
    return render_template("dash.html",users=users)

if __name__ == "__main__":
    app.run(debug=True)

