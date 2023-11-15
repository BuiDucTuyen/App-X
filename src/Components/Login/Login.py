from flask import Flask, request, redirect, session, url_for
from requests_oauthlib import OAuth1Session
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

consumer_key = 'L0zGioiAyiByOVJhbut9RprSg'  
consumer_secret = 'TNhrFkclBv7MknhoIFgmQj5e4ZwlQugqaq7Y1rRWobqfTdI0g5'  

@app.route('/')
def home():
    return 'Trang chủ - Đăng nhập bằng Twitter <a href="/twitter_login">Đăng nhập</a>'

@app.route('/twitter_login')
def twitter_login():
    twitter = OAuth1Session(consumer_key, client_secret=consumer_secret)
    request_token_url = 'https://api.twitter.com/oauth/request_token'
    response = twitter.fetch_request_token(request_token_url)

    request_token = response.get('oauth_token')
    request_token_secret = response.get('oauth_token_secret')

    session['request_token'] = request_token
    session['request_token_secret'] = request_token_secret

    authenticate_url = f'https://api.twitter.com/oauth/authenticate?oauth_token={request_token}'
    return redirect(authenticate_url)

@app.route('/twitter_callback')
def twitter_callback():
    oauth_token = request.args.get('oauth_token')
    oauth_verifier = request.args.get('oauth_verifier')

    request_token = session['request_token']
    request_token_secret = session['request_token_secret']

    twitter = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=request_token,
        resource_owner_secret=request_token_secret,
        verifier=oauth_verifier
    )

    access_token_url = 'https://api.twitter.com/oauth/access_token'
    access_token_response = twitter.fetch_access_token(access_token_url)

    access_token = access_token_response.get('oauth_token')
    access_token_secret = access_token_response.get('oauth_token_secret')

    user_info_url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    user_info_response = twitter.get(user_info_url)
    user_data = user_info_response.json()

    return f'Đăng nhập bằng Twitter thành công!<br>{user_data["name"]}'

if __name__ == '__main__':
    app.run(debug=True)


