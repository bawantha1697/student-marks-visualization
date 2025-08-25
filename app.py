from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    chart_url = None
    if request.method == "POST":
        students = request.form.getlist("student")
        maths = list(map(int, request.form.getlist("maths")))
        science = list(map(int, request.form.getlist("science")))
        english = list(map(int, request.form.getlist("english")))

        df = pd.DataFrame({
            "Student": students,
            "Maths": maths,
            "Science": science,
            "English": english
        })

        # Example: generate bar chart
        plt.figure()
        plt.bar(df["Student"], df["Maths"])
        plt.title("Maths Marks of Students")

        # Convert plot to image
        img = io.BytesIO()
        plt.savefig(img, format="png")
        img.seek(0)
        chart_url = base64.b64encode(img.getvalue()).decode()

    return render_template("index.html", chart_url=chart_url)

if __name__ == "__main__":
    app.run(debug=True)
