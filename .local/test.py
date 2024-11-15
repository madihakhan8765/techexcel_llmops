import urllib.request
import json
import os
import ssl

def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True) # this line is needed if you use self-signed certificate in your scoring service.

# Request data goes here
# The example below assumes JSON formatting which may be updated
# depending on the format your endpoint expects.
# More information can be found here:
# https://docs.microsoft.com/azure/machine-learning/how-to-deploy-advanced-entry-script
data = {
  "question": "How can I request a refill for my prescription at Lamna Healthcare?",
  "chat_history": []
}

body = str.encode(json.dumps(data))

url = 'https://rag-7557-endpoint.eastus2.inference.ml.azure.com/score'
# Replace this with the primary/secondary key, AMLToken, or Microsoft Entra ID token for the endpoint
api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCIsImtpZCI6IjNQYUs0RWZ5Qk5RdTNDdGpZc2EzWW1oUTVFMCJ9.eyJhdWQiOiJodHRwczovL21sLmF6dXJlLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzE2YjNjMDEzLWQzMDAtNDY4ZC1hYzY0LTdlZGEwODIwYjZkMy8iLCJpYXQiOjE3MzE2OTY4MDQsIm5iZiI6MTczMTY5NjgwNCwiZXhwIjoxNzMxNzAyMzIzLCJhY3IiOiIxIiwiYWlvIjoiQWFRQVcvOFlBQUFBS3o1blZZbU9hNGJQcS9LTHY1ZmJUWHk1OTYrRjArTlFqR1lpaWZhNGFmY3k5eUh0eXJ2UDZyVThvckFLVHVMOUdSdUlCd2ZIN2RvQXhxaDdWSXV3WnZMcnFWVFdEWWRlVmk2N1VoNHFjYUVML1VieVJ4SndzMmNsaUZvR2Q2akVjclJlbXFpMjJqNUM4MG9SNmZyUTZZUHZma1BTeXFKeEsyVzZ6ZDAxNjFSVEE5SVFscWZqTDFOYVRRY1dpUUNFVUNvOWZySjhwYXJxaXhFL25EendDdz09IiwiYWx0c2VjaWQiOiI1OjoxMDAzMjAwMEJGNjY4OUNBIiwiYW1yIjpbInJzYSIsIm1mYSJdLCJhcHBpZCI6ImNiMmZmODYzLTdmMzAtNGNlZC1hYjg5LWEwMDE5NGJjZjZkOSIsImFwcGlkYWNyIjoiMCIsImRldmljZWlkIjoiYjA4NGFjMDktMmI3OC00MWRlLWJkMjktOTRlNzRjODVjMzkxIiwiZW1haWwiOiJNYWRpaGEuS2hhbkBtaWNyb3NvZnQuY29tIiwiZmFtaWx5X25hbWUiOiJLaGFuIiwiZ2l2ZW5fbmFtZSI6Ik1hZGloYSIsImdyb3VwcyI6WyJiMTMwNDAyMi0wOGU2LTQ0N2QtYjA5NC0xNTM3MDU5N2M2YjYiLCIwOTUzMWE3Mi0yYzNlLTRlMDYtYmUxZS0yNTk2YmQwOGRjZGQiLCJkMzRjNGViZS00OTg0LTQ5MDMtYTY0ZC04YzIwMjgzZDUxNmIiLCJlMzA5NmRmNy1iNjVjLTRlMzItYWIxYS03YTM1ZGM2ODRmMGEiXSwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNzJmOTg4YmYtODZmMS00MWFmLTkxYWItMmQ3Y2QwMTFkYjQ3LyIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjI0LjIxNC4xNTkuMTYyIiwibmFtZSI6Ik1hZGloYSBLaGFuIiwib2lkIjoiYzM1YzM4NTktYzA3NC00YjBmLTg5YjctYTc5NjFkYmE2ZmI2IiwicHVpZCI6IjEwMDMyMDAyNTRGMUQxOTIiLCJyaCI6IjEuQVVZQUU4Q3pGZ0RUalVhc1pIN2FDQ0MyMDE5dnBoamYyeGRNbmRjV05IRXFuTDd4QUxsR0FBLiIsInNjcCI6InVzZXJfaW1wZXJzb25hdGlvbiIsInN1YiI6Ikt4S01xSURNVnZWVE5kUWxTdnVqZ2R1ZzNTRWFrLVExSmEwMVQzLVpIVEEiLCJ0aWQiOiIxNmIzYzAxMy1kMzAwLTQ2OGQtYWM2NC03ZWRhMDgyMGI2ZDMiLCJ1bmlxdWVfbmFtZSI6Ik1hZGloYS5LaGFuQG1pY3Jvc29mdC5jb20iLCJ1dGkiOiJfbjlzSk5aV2xFSzJzRFJxTG1OR0FBIiwidmVyIjoiMS4wIiwieG1zX2lkcmVsIjoiMSAxMCJ9.EU9Tlbws4hSuHH1vC_QMhIKSigXje6Hso3aIBJnMqfIvjFmVrZFMm6MdvXEsyzXaIFBhWKp5yIw46Odpnhhxtx9gPM5JQLNNlljTv9LQjCG8_0HbnkWD7uSkcE52AsVW2KizrsG05J_VLdfeFVpbJ6RceEBo9twOZynlFTTDsyVi0EcTs9wp7wEOcDfmwll3xCi1RK630Ltf8VgjXrcWPKa0P4t604letv-NBac9oK--1zAuSCm_ffEGotUhr221KgnW7atK99jOhgpQ1mkn320TL3jWhvOnpmJ4KZ_ORzgV2qGnWJzBPgBCy5qzmnX6JeiOtXw67Aevd29VMiAkYw'
if not api_key:
    raise Exception("A key should be provided to invoke the endpoint")


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(error.read().decode("utf8", 'ignore'))