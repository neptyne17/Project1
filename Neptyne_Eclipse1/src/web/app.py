from flask import Flask, render_template, request
from crud.USER_CRUD import USER_CRUD

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/login_submit", methods=['GET', 'POST'])
def login_submit():
    message = None
    login = None
    
    
    #--Data from DB----\
    dblogin = 'vasia'
    dbpasswd = '111'
    dblock = False

    
    if request.method == 'POST':
    
        flogin = request.form.get('login')
        fpasswd = request.form.get('passwd')
        
        if dblogin == flogin and dbpasswd == fpasswd:
            
            if dblock:
                message = "your are locked. Contact sysadmin."
                return render_template('login.html', login=login)
            else:
                message = 'Wrong login or password. Try again.'
                
        return render_template('login.html', message=message)
    
@app.route('/u_list')    
def u_list():
    
    title = 'U_list'
    u_crud = USER_CRUD()
    users = u_crud.select_all_obj()
    
    return render_template('u_list.html', users=users, title=title)


@app.route("/u_card")
def u_card():
    id_ = request.args.get('id')
    u_crud = USER_CRUD
    user = u_crud.select_one_by_id_obj(id_)
    return render_template('u_card.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)