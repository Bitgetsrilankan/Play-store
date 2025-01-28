from google_play_scraper import search, app
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def play_store_search():
    query = request.args.get('query', '')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    try:
        # Fetch search results
        results = search(query, num=10)

        # Format the data as per the required structure
        formatted_results = []
        for app_info in results:
            formatted_results.append({
                "title": app_info.get("title"),
                "appId": app_info.get("appId"),
                "url": f"https://play.google.com/work/apps/details?id={app_info.get('appId')}",
                "icon": app_info.get("icon"),
                "developer": app_info.get("developer"),
                "developerId": app_info.get("developerId"),
                "price": app_info.get("price"),
                "free": app_info.get("free"),
                "summary": app_info.get("description"),
                "scoreText": app_info.get("scoreText"),
                "score": app_info.get("score")
            })

        return jsonify(formatted_results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/app/<app_id>', methods=['GET'])
def get_app_details(app_id):
    try:
        # Fetch detailed data for the app using the appId
        app_details = app(app_id)

        # Format the data as per the required structure
        detailed_info = {
            "title": app_details.get("title"),
            "appId": app_details.get("appId"),
            "url": f"https://play.google.com/work/apps/details?id={app_details.get('appId')}",
            "icon": app_details.get("icon"),
            "developer": app_details.get("developer"),
            "developerId": app_details.get("developerId"),
            "price": app_details.get("price"),
            "free": app_details.get("free"),
            "summary": app_details.get("description"),
            "scoreText": app_details.get("scoreText"),
            "score": app_details.get("score"),
            "contentRating": app_details.get("contentRating"),
            "reviews": app_details.get("reviews"),
            "url": app_details.get("url"),
            "screenshots": app_details.get("screenshots")
        }

        return jsonify(detailed_info)

    except Exception as e:
        return jsonify({"error": f"Failed to fetch details for {app_id}: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
