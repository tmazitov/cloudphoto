import io


class Config:
    def __init__(self):
        self.variables = {}

    def __str__(self):
        max_len = max([len(key) for key in self.variables.keys()])
        return "".join(
            [f"{ k } {' ' * (max_len - len(k))} : { self.variables[k]}\n" for k in self.variables.keys()]
        )

    def parse(self, string: str):
        if "=" not in string:
            return (None, None)
        if string[len(string) - 1] == "=":
            return (None, None)

        parts = string.split("=")
        key = parts[0]
        value = parts[1]

        return key, value

    def get(self, key: str):
        return self.variables[key]

    def add(self, key: str, value: str):
        self.variables[key] = value

    def includes(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def read(self, config_file: io.TextIOWrapper):
        lines = config_file.readlines()
        for line in lines:
            if line is None:
                continue
            
            line = line.replace("\n", "")  
            key, value = self.parse(line)

            if key == None or value == None:
                continue

            self.add(key, value)
