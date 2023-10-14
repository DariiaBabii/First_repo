import base64


def encode_data_to_base64(data):
    base64_messages = []

    for user_info in data:
        user_info_bytes = user_info.encode("utf-8")
        base64_user_info = base64.b64encode(user_info_bytes)
        base64_message = base64_user_info.decode("utf-8")
        base64_messages.append(base64_message)

    return base64_messages  # SGVsbG8gd29ybGQh
    
        
        
        
    