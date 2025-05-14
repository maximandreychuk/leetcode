class Database:
    def __init__(self):
        self.data = {}
        self.transactions = []

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return "NULL"

    def set(self, key, value):
        self.data[key] = value

    def unset(self, key):
        if key in self.data:
            del self.data[key]

    def counts(self, value):
        count = 0
        for k in self.data:
            if self.data[k] == value:
                count += 1
        return count

    def find(self, value):
        found = []
        for k in self.data:
            if self.data[k] == value:
                found.append(k)
        return found

    def begin(self):
        self.transactions.append(self.data.copy())

    def rollback(self):
        if self.transactions:
            self.data = self.transactions.pop()
        else:
            print("NO TRANSACTION")

    def commit(self):
        if self.transactions:
            self.transactions = []  # Clear transactions to commit
        else:
            pass  # Do nothing if no transaction is active


def main():
    db = Database()

    while True:
        try:
            command = input("> ").strip()
        except EOFError:
            break  # Handle EOF (Ctrl+D)

        parts = command.split()
        action = parts[0].upper()

        if action == "SET":
            if len(parts) == 3:
                key = parts[1]
                value = parts[2]
                db.set(key, value)
            else:
                print("Invalid SET command.")
        elif action == "GET":
            if len(parts) == 2:
                key = parts[1]
                print(db.get(key))
            else:
                print("Invalid GET command.")
        elif action == "UNSET":
            if len(parts) == 2:
                key = parts[1]
                db.unset(key)
            else:
                print("Invalid UNSET command.")
        elif action == "COUNTS":
            if len(parts) == 2:
                value = parts[1]
                print(db.counts(value))
            else:
                print("Invalid COUNTS command.")
        elif action == "FIND":
            if len(parts) == 2:
                value = parts[1]
                found = db.find(value)
                print(*found)  # Print all found keys separated by spaces
            else:
                print("Invalid FIND command.")
        elif action == "BEGIN":
            db.begin()
        elif action == "ROLLBACK":
            db.rollback()
        elif action == "COMMIT":
            db.commit()
        elif action == "END":
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()