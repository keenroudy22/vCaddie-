from flask import Flask, render_template, request

app = Flask(__name__)

# Function to determine the appropriate club based on distance and lie
def recommend_club(distance, lie):
    if lie == "fairway":
        if distance > 200:
            return "Driver"
        elif 180 <= distance <= 200:
            return "3-Wood"
        elif 150 <= distance < 180:
            return "5-Iron"
        elif 120 <= distance < 150:
            return "7-Iron"
        elif 100 <= distance < 120:
            return "9-Iron"
        else:
            return "Pitching Wedge"
    elif lie == "rough":
        if distance > 200:
            return "3-Wood"
        elif 150 <= distance <= 200:
            return "5-Iron"
        elif 120 <= distance < 150:
            return "7-Iron"
        elif 100 <= distance < 120:
            return "8-Iron"
        else:
            return "Sand Wedge"
    elif lie == "sand":
        if distance > 100:
            return "7-Iron"
        else:
            return "Sand Wedge"
    else:
        return "Putter"

# Home route to display the form
@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Golf Club Recommender</title>
    </head>
    <body>
        <h1>Golf Club Recommender</h1>
        <form action="/recommend" method="POST">
            <label for="distance">Distance to the hole (yards):</label><br>
            <input type="number" id="distance" name="distance" required><br><br>

            <label for="lie">Lie of the ball:</label><br>
            <select id="lie" name="lie" required>
                <option value="fairway">Fairway</option>
                <option value="rough">Rough</option>
                <option value="sand">Sand</option>
                <option value="green">Green</option>
            </select><br><br>

            <input type="submit" value="Recommend Club">
        </form>
    </body>
    </html>
    '''

# Route to handle form submission and return the recommended club
@app.route('/recommend', methods=['POST'])
def recommend():
    distance = int(request.form['distance'])
    lie = request.form['lie']
    club = recommend_club(distance, lie)
    return f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Recommended Club</title>
    </head>
    <body>
        <h1>Your Recommended Club is: {club}</h1>
        <a href="/">Try Again</a>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True, port=5005)

