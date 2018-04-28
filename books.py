from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)
#app.debug = True

booksInfo = []

@app.route('/books/')
def index():
	return render_template('index.html', books = booksInfo)
	
@app.route('/add book', methods = ['POST', 'GET'])
def addBook():
	if request.method == 'POST':
		booksInfo.append({'title': request.form['title'], 'author': request.form['author'], 'publisher': request.form['publisher']}.copy())
		return redirect(url_for('index', books = booksInfo ))
	else:
		return render_template('add book.html')
	
''' Search book by name and display the result'''
@app.route('/books/<name>')
def getBookByName(name):
	return render_template('book.html', book_found = searchBook(name))

''' Returns matched book if found else message saying "No book found.." '''
def searchBook(name):
	for book in booksInfo:
		if book ['title'] == name:
			return book
	return "No book found.."

if __name__ == '__main__':
	#app.jinja_env.auto_reload = True
	#app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(debug = True)