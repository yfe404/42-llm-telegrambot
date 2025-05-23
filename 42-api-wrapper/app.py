from flask import Flask, jsonify
from intra import ic
from config import campus_id

app = Flask(__name__)
ic.progress_bar = False  # No progress bar in server mode


@app.route("/user/<userid>", methods=["GET"])
def get_user_infos(userid):
    payload = {
            "id": userid
    }
    try:
        response = ic.get(f"users", params=payload)
        return jsonify(response.text)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

    

@app.route("/connected", methods=["GET"])
def get_connected_users():
    payload = {
        "filter[campus_id]": campus_id,
        "filter[active]": "true"
    }

    try:
        response = ic.pages_threaded("locations", params=payload)
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

