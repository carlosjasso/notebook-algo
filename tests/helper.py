from datetime import datetime

def print_ruled(message: str, new_line: bool = True) -> None:
    ruller = "-" * int((70 - len(message)) / 2)
    br = "\n" if new_line else ""
    print(f"{br}{ruller} {message} {ruller}")

def print_took(start: datetime):
    diff = int((datetime.now() - start).total_seconds() * 1000)
    print(f"\ttook: {diff} ms")
