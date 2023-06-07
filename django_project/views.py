from django.http import HttpRequest, HttpResponse
import os, json

messages = json.loads(os.getenv("MESSAGES"))
message_count = int(os.getenv("MSG_COUNT"))


def home(request):
    return HttpResponse("""
  <!DOCTYPE html>
  <html lang="sv-se">
  <head>
  <title>TTG-chatten</title>
  </head>
  <body>
  <h1>TTG-chatten</h1>
  <div > <!-- remove when access granted -->
  <p>Du har inte åtkomst till chatten</p>
  <h2>Logga in</h2>
  <div>
  <input type="password" id="token" placeholder="token"/>
  <button onclick="tryLogin()">Logga in</button>
  </div>
  </div>
  <div id="messages">
    <p>Chatten skulle vara här om du hade loggat in</p>
  </div>

  <script>
  function tryLogin(){
    localStorage.setItem("token", document.getElementById("token"))
  } 
  </script>

  <script>
    while(1==1){
      setTimeout(function(){
      if(fetch("ttg-chat"))
      }, 1350)
    }
  </script>
  </body>
  </html>
  """)


def get_count(request):
    
    return HttpResponse(json.dumps({"message_count": message_count}))


def reload(request):
  
  auth = request.GET.get("auth")
  print(type(auth), type(str(os.getenv("ALL_TOKENS"))))
  if " " + auth + " " in str(os.getenv("ALL_TOKENS")):
    return HttpResponse(
        json.dumps({
            "message_count": message_count,
            "messages": messages
        }))
  else:
    return HttpResponse("Access denied")

def create_message(request):
  return HttpResponse("Not yet implemented")
    