from flask import Flask, render_template
import sys, os, time
app = Flask(__name__)

QUOTES = []

def onBoot(): #@TODO: Make this more static
	global QUOTES
	for q in os.listdir('./quotes/'):
		if not q.endswith('.txt'): continue
		with open('./quotes/'+q) as f:
			data = [i.strip() for i in f.readlines()]
		q = {'name':q[:-4].replace('_', ' ').title(), 'len':len(data), 'q':[i.split(' ', 1) for i in data]}
		QUOTES.append(q)

@app.route('/')
def root():
	return render_template('index.html', quotes=QUOTES)

@app.route('/<qid>')
def quote(qid):
	if not qid.isdigit(): return ""
	return render_template('quote.html', quote=QUOTES[int(qid)], qlen=len(QUOTES), n=int(qid))

onBoot()

if __name__ == "__main__":
    app.run()