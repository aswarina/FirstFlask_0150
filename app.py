
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        nama = request.form.get("nama", "").strip()

        if nama:
            hasil = f"Halo, {nama}! Data berhasil dikirim."
        else:
            hasil = "Silakan masukkan nama terlebih dahulu."

    return render_template("index.html", hasil=hasil)


@app.route("/about")
def about():
    return "About us"


@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"


@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"


if __name__ == "__main__":
    app.run(debug=True)
