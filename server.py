from flask import Flask, request, render_template, redirect, url_for
from weather import get_current_weather
from waitress import serve

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")

@app.route("/weather", methods=["GET","POST"])
def get_weather():
    if request.method == "POST":
        city = request.form.get("city")
        return redirect(url_for('get_weather', city=city))
    else:
        city = request.args.get("city")

    #check for empty string or string with only spaces
    if not city or not city.strip():
        city = "Jaipur"
   

    weather_data = get_current_weather(city)

    #City is not found by the API
    if not weather_data['cod'] == 200:
        return render_template("city-not-found.html")

    return render_template ("weather.html", 
                           title=weather_data["name"], 
                           status= weather_data["weather"][0]["description"].capitalize(),
                           temp=f"{weather_data['main']['temp']:.1f}",
                           feels_like=f"{weather_data['main']['feels_like']:.1f}"
                            ) 

      

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)