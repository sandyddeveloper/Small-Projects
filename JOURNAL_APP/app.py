from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_mysqldb import MySQL
import bcrypt

app = Flask(__name__)


app.secret_key = 'your_secret_key'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'journal_db'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", 
                        (username, email, hashed_password.decode('utf-8')))
            mysql.connection.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            flash('An error occurred. Email might already be registered.', 'danger')
        finally:
            cur.close()
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        cur = mysql.connection.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()

        if user and bcrypt.checkpw(password, user[2].encode('utf-8')):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Login successful!', 'success')
            return redirect(url_for('journal_entries'))
        else:
            flash('Invalid email or password.', 'danger')
    
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))


@app.route('/journal_entries')
def journal_entries():
    if 'user_id' not in session:
        flash('Please log in to view your journal.', 'info')
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, title, content, created_at FROM journal_entries WHERE user_id = %s", (session['user_id'],))
    entries = cur.fetchall()
    cur.close()

    return render_template('journal_entries.html', entries=entries)


@app.route('/new_entry', methods=['GET', 'POST'])
def new_entry():
    if 'user_id' not in session:
        flash('Please log in to create a journal entry.', 'info')
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO journal_entries (user_id, title, content) VALUES (%s, %s, %s)", 
                    (session['user_id'], title, content))
        mysql.connection.commit()
        cur.close()

        flash('Journal entry created successfully!', 'success')
        return redirect(url_for('journal_entries'))

    return render_template('new_entry.html')

@app.route('/edit_entry/<int:entry_id>', methods=['GET', 'POST'])
def edit_entry(entry_id):
    if 'user_id' not in session:
        flash('Please log in to edit a journal entry.', 'info')
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT id, title, content FROM journal_entries WHERE id = %s AND user_id = %s", 
                (entry_id, session['user_id']))
    entry = cur.fetchone()

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        cur.execute("UPDATE journal_entries SET title = %s, content = %s WHERE id = %s AND user_id = %s", 
                    (title, content, entry_id, session['user_id']))
        mysql.connection.commit()
        cur.close()

        flash('Journal entry updated successfully!', 'success')
        return redirect(url_for('journal_entries'))

    cur.close()
    return render_template('edit_entry.html', entry=entry)


@app.route('/delete_entry/<int:entry_id>')
def delete_entry(entry_id):
    if 'user_id' not in session:
        flash('Please log in to delete a journal entry.', 'info')
        return redirect(url_for('login'))

    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM journal_entries WHERE id = %s AND user_id = %s", (entry_id, session['user_id']))
    mysql.connection.commit()
    cur.close()

    flash('Journal entry deleted successfully!', 'success')
    return redirect(url_for('journal_entries'))

if __name__ == "__main__":
    app.run(debug=True)
