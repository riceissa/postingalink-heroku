import os
from flask import Flask, render_template
app = Flask(__name__)

def title_recursion(num_str):
    base_title = "Posting a link instead of formulating an argument"
    try:
        n = int(num_str)
        if n == 0:
            return base_title
        else:
            return "Posting a link instead of " + title_recursion(n - 1).lower()
    except ValueError:
        return base_title

def content_recursion(num_str):
    base_content = """This page is called posting a link instead
        of formulating an argument, so when somebody posts
        a link instead of formulating an argument you can
        post a link to posting a link instead of formulating
        an argument instead of formulating an argument."""
    try:
        n = int(num_str)
        if n == 0:
            return base_content
        else:
            this_title = title_recursion(n).lower()
            previous_title = title_recursion(n - 1).lower()
            return "This page is called " + this_title + ", so when somebody posts " + previous_title + " instead of formulating an argument you can post a link to " + this_title + " instead of formulating an argument."
    except ValueError:
        return base_content

#@app.route('/')
#def index():
    #""" Displays the index page accessible at '/'
    #"""
    #return render_template('template.html')

@app.route("/<num_str>/")
def postingalink(num_str):
    try:
        title = title_recursion(num_str)
        body = content_recursion(num_str)
    except RuntimeError:
        title = "O, no!"
        body = "Now, that *is* a bit too many!!"
    return render_template("template.html", title=title, body=body)

if __name__ == "__main__":
    #app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
