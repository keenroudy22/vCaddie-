from flask import Flask, render_template, request

app = Flask(__name__)


def recommend_club(distance, lie, driver_distance):
    percentage = distance / driver_distance * 100
    if lie == "fairway":
        if percentage > 100:
            return "Driver"
        if 83 <= percentage <= 100:
            return "3-Wood"
        if 75 <= percentage < 83:
            return "5-Hybrid"
        if 70 <= percentage <= 75:
            return "5-Iron"
        if 66 <= percentage < 70:
            return "6-Iron"
        if 60 <= percentage < 66:
            return "7-Iron"
        if 57 <= percentage < 60:
            return "8-Iron"
        if 54 <= percentage < 57:
            return "9-Iron"
        if 42 <= percentage < 54:
            return "Pitching Wedge"
        if 38 <= percentage < 42:
            return "Approach Wedge · 52°"
        if 32 <= percentage < 38:
            return "Sand Wedge · 56°"
        return "Lob Wedge · 60°"
    if lie == "rough":
        if percentage > 75:
            return "3-Wood"
        if 57 <= percentage <= 75:
            return "5-Iron"
        if 45 <= percentage < 57:
            return "7-Iron"
        if 38 <= percentage < 45:
            return "8-Iron"
        return "Sand Wedge"
    if lie == "sand":
        return "7-Iron" if percentage > 38 else "Sand Wedge"
    return "Putter"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():
    try:
        driver_distance = int(request.form["driver_distance"])
        distance = int(request.form["distance"])
        lie = request.form["lie"]
        if driver_distance <= 0 or distance < 0:
            raise ValueError
    except (KeyError, TypeError, ValueError):
        return render_template(
            "index.html",
            error="Enter a positive driver distance and a valid distance to the pin.",
        ), 400

    club = recommend_club(distance, lie, driver_distance)
    return render_template(
        "result.html",
        club=club,
        distance=distance,
        lie=lie.title(),
    )


if __name__ == "__main__":
    app.run(debug=True, port=5005)

