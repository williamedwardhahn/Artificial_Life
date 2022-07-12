from microdot import Microdot, send_file
app = Microdot()


html1 ="""
<html>

    <body >
            <h1>Microdot Form Example</h1>

            <form method="POST" action="">
                
                    <p>
                        <input type="radio" name="var1" value="1">
                        <input type="radio" name="var1" value="2">
                        <input type="radio" name="var1" value="3">
                        <br>
                        <input type="submit" name="read" value="Read">
                    </p>
                
                
            </form>
        </div>
    </body>
</html>
"""



@app.route('/', methods=['GET', 'POST'])
def index(request):

	if request.method == 'POST':
		print(request.form['var1'])

	return html1, 200, {'Content-Type': 'text/html'}



app.run(debug=True)
