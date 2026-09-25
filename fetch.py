from importlib import import_module


get_gmail_service = import_module("gmail_auth").get_gmail_service


service = get_gmail_service()


results = service.users().messages().list(
    userId="me",
    maxResults=10
).execute()


messages = results.get(
    "messages",
    []
)


for message in messages:

    print(
        "Message ID:",
        message["id"]
    )