def get_credentials_users(path):
     with open(path, 'rb') as file:
        binary_file = file.read()

        decoded_file = binary_file.decode('utf-8')

        credentials = decoded_file.split('\n')

        return credentials