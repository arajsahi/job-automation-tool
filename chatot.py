import anthropic
from dotenv import load_dotenv
load_dotenv()

from flask import Flask,request,jsonify,render_template_string
import os

app = Flask(__name__)
client =anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Araj Chatbot</title>
<style>
  body { font-family: Arial, sans-serif; background: #f0f2f5; margin: 0; padding: 0; }
  .container { max-width: 700px; margin: 40px auto; background: white; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; }
  .header { background: #075e54; color: white; padding: 20px; text-align: center; }
  .header h1 { margin: 0; font-size: 22px; }
  #chat { height: 450px; overflow-y: scroll; padding: 20px; display: flex; flex-direction: column; gap: 12px; }
  .user-msg { background: #dcf8c6; padding: 10px 14px; border-radius: 18px 18px 4px 18px; align-self: flex-end; max-width: 70%; }
  .bot-msg { background: #f1f0f0; padding: 10px 14px; border-radius: 18px 18px 18px 4px; align-self: flex-start; max-width: 70%; }
  .input-area { display: flex; padding: 16px; gap: 10px; border-top: 1px solid #eee; }
  input { flex: 1; padding: 12px; border: 1px solid #ddd; border-radius: 24px; outline: none; font-size: 14px; }
  button { background: #075e54; color: white; border: none; padding: 12px 24px; border-radius: 24px; cursor: pointer; font-size: 14px; }
  button:hover { background: #128c7e; }
</style>
</head>
<body>
<div class="container">
  <div class="header"><h1>🤖 Araj Chatbot</h1></div>
  <div id="chat"></div>
  <div class="input-area">
    <input id="msg" type="text" placeholder="Type a message...">
    <button onclick="sendMessage()">Send</button>
  </div>
</div>
<script>
function sendMessage() {
    const msg = document.getElementById('msg').value;
    if (!msg) return;
    const chat = document.getElementById('chat');
    chat.innerHTML += '<div class="user-msg">' + msg + '</div>';
    chat.innerHTML += '<div class="bot-msg">Typing...</div>';
    chat.scrollTop = chat.scrollHeight;
    fetch('/chat', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({message: msg})})
    .then(r => r.json())
    .then(data => {
        const msgs = chat.querySelectorAll('.bot-msg');
        msgs[msgs.length-1].textContent = data.reply;
        chat.scrollTop = chat.scrollHeight;
    });
    document.getElementById('msg').value = '';
}
document.getElementById('msg').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') sendMessage();
});
</script>
</body>
</html>
"""





@app.route('/')
def home():
    return render_template_string(HTML)


@app.route('/chat',methods=["POST"])

def chat():
    user_message = request.json['message']
    message = client.messages.create(

        model="claude-sonnet-4-6",
        max_tokens=500,
        messages=[{"role": "user", "content": user_message}]
    )

    reply = message.content[0].text
    return jsonify({"reply":reply})

if __name__ == '__main__':
    app.run(debug=True)