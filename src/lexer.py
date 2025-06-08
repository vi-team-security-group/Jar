import re
<<<<<<< HEAD

# === Описание на токени ===
TOKEN_TYPES = [
    ("KEYWORD", r"\b(начало|край|дай|ако|иначе|върни)\b"),
    ("NUMBER", r"\b\d+(\.\d+)?\b"),
    ("STRING", r"\".*?\""),
    ("IDENTIFIER", r"\b[а-яА-Я_][а-яА-Я0-9_]*\b"),
    ("OPERATOR", r"[+\-*/=<>!]+"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("NEWLINE", r"\n"),
    ("WHITESPACE", r"[ \t]+"),
    ("UNKNOWN", r".")
]

# === Генериране на обща regex формула ===
TOKEN_REGEX = "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES)

# === Функция за токенизация с детайлна информация ===
def tokenize(code):
    tokens = []
    line_num = 1
    line_start = 0
    for match in re.finditer(TOKEN_REGEX, code):
        kind = match.lastgroup
        value = match.group()
        start = match.start()
        end = match.end()
        column = start - line_start
        if value == "\n":
            line_num += 1
            line_start = end
        elif kind not in ["WHITESPACE", "NEWLINE"]:
            tokens.append({
                "Тип": kind,
                "Стойност": value,
                "Ред": line_num,
                "Колона": column,
                "Позиция": (start, end)
            })
    return tokens

# === Примерен ЖАР код ===
if __name__ == "__main__":
    code = '''
начало
    дай "Здравей, свят!"
    върни 42
край
'''
    result = tokenize(code)
    for token in result:
        print(token)
=======
from typing import List

class Token:
    def __init__(self, type_: str, value: str):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)})"

def tokenize(code: str) -> List[Token]:
    token_specification = [
        ("KEYWORD", r"\b(начало|край|дай|ако|иначе|върни)\b"),
        ("NUMBER", r"\b\d+\b"),
        ("STRING", r'"[^"]*"'),
        ("IDENTIFIER", r"\b[а-яА-Я_][а-яА-Я0-9_]*\b"),
        ("OPERATOR", r"[+\-*/=<>!]+"),
        ("SKIP", r"[ \t\n]+"),
        ("MISMATCH", r".")
    ]
    tok_regex = "|".join(f"(?P<{name}>{pattern})" for name, pattern in token_specification)
    tokens = []
    for match in re.finditer(tok_regex, code):
        kind = match.lastgroup
        value = match.group()
        if kind == "SKIP":
            continue
        elif kind == "MISMATCH":
            raise RuntimeError(f"Непознат символ: {value}")
        else:
            tokens.append(Token(kind, value))
    return tokens
>>>>>>> c07e21a (Обновена първа фаза + тест)
