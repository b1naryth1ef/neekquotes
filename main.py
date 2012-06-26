from flask import Flask, render_template
import sys, os, time
app = Flask(__name__)

QUOTES = []

for q in os.listdir('./quotes/'):
	if not q.endswith('.txt'): continue
	with open('./quotes/'+q) as f:
		data = [i.strip() for i in f.readlines()]
	q = {'name':q[:-4].replace('_', ' ').title(), 'len':len(data), 'q':[]}
	for line in data:
		q['q'].append(line.split(' ', 1))
	QUOTES.append(q)

@app.route('/')
def root():
	return render_template('index.html', quotes=QUOTES)

@app.route('/quote/<qid>')
def quote(qid):
	return render_template('quotes.html', quote=QUOTES[int(qid)], qlen=len(QUOTES), n=int(qid))

if __name__ == "__main__":
    app.run(debug=True)