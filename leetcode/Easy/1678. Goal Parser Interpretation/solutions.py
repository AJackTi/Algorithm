def interpret(self, command: str) -> str:
    d = {"()": "o", "(al)": "al"}

    for s in d:
        command = command.replace(s, d[s])
    
    return command