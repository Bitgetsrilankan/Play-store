from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def generate_image():
    query = request.args.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query parameter is required'}), 400

    url = 'https://www.blackbox.ai/api/image-generator'

    headers = {
        'authority': 'www.blackbox.ai',
        'accept': '*/*',
        'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        'cookie': 'sessionId=3033c7d1-cff1-434c-99e1-2230eb4082df; intercom-id-jlmqxicb=bb00e518-0266-4b82-943a-e06982f73b3b; intercom-device-id-jlmqxicb=3911161f-8755-4a5a-a4dc-2f4071616805; render_session_affinity=ca92ab20-174f-48b8-866a-e5d117b10b1a; __Host-authjs.csrf-token=26a49f56587df7a792d4f759ecfe8bfc183d192ae2e3be05f1e8a6ef3447c59e%7Cfe2393b25dfa9d3b0ab1bb3d4031421c964af4783968b1e3c67a31553e5da889; __Secure-authjs.callback-url=https%3A%2F%2Fwww.blackbox.ai',
        'origin': 'https://www.blackbox.ai',
        'pragma': 'no-cache',
        'referer': 'https://www.blackbox.ai/agent/create/new',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'
    }

    data = {
        'query': query,
        'agentMode': True
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        image_url = result.get('markdown', '').split('![](')[-1].strip(')')
        
        # Create the response dictionary with Owner included
        response_dict = {
            'image_url': image_url,
            'Owner': '@PikaApis'
        }

        # Use jsonify directly to return the proper JSON response
        return jsonify(response_dict)
    else:
        error_response = {
            'error': 'Failed to fetch data'
        }
        return jsonify(error_response), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
