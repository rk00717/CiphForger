class UserData:
    def __init__(self, platform, username):
        self.username = username
        self.platform = platform

    def set_password(self, password):
        self.password = password

class CryptoTable:
    symbols = (
        list("abcdefghijklmnopqrstuvwxyz") +
        list("ABCDEFGHIJKLMNOPQRSTUVWXYZ") +
        list("0123456789") +
        list("@#$%&*!")
    )

    def __init__(self, table_key):
        self.key = table_key

        self.columns = 8
        self.table = self.shuffle_list()

    def shuffle_list(self):
        shuffled_list = [(symbol, (ord(symbol) * self.key) % len(self.symbols)) for symbol in self.symbols]
        shuffled_list.sort(key=lambda x:x[1])
        shuffled_symbols = [symbol[0] for symbol in shuffled_list]
        return shuffled_symbols
        
    def display(self):
        col = self.columns
        display_table = [self.table[i:i + col] for i in range(0, len(self.symbols), col)]
        [print("| {0} |".format(" | ".join(row))) for row in display_table]

    def calculate_sum(self, content):
        return sum((ord(char) - ord("a") + 1) if char.islower() else (ord(char) - ord("A") + 1) for char in content)
    
class PassGenerator:
    def __init__(self, password_size, key_1, key_2):
        self.password_size = password_size
        self.key_1 = key_1
        self.key_2 = key_2

    def generate_password(self, table:list, platform:str, username:str, skip = 0):
        password = []
        platform_rotated = platform
        username_rotated = username

        for _ in range(self.password_size):
            platform_sum = ord(platform_rotated[0]) + skip
            username_sum = ord(username_rotated[0]) + skip
            
            row = username_sum % self.key_2
            col = platform_sum % self.key_1
            index = (row * self.key_1 + col) % len(table)

            password.append(table[index])
            platform_rotated = platform_rotated[1:] + platform_rotated[0]
            username_rotated = username_rotated[1:] + username_rotated[0]

        return ''.join(password)