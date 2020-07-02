from logger import logger

print("here we go")


@logger
def polish(s):
  pol = []
  assert "-, +, /, *" not in s, "No signs -, +, /, *"
  pol.append(s)
  for sign, number1, number2 in pol:
    if sign == "+":
      print(int(number1)+int(number2))
    elif sign == "-":
      print(int(number1) - int(number2))
    elif sign == "*":
      print(int(number1) * int(number2))
    elif sign == "/":
    # try:
      print(int(number1) / int(number2))
    # except (Exception) as e:
    #   print(f"errors {e}")

try:
  polish(input().split())
except (Exception) as e:
  print(f"errors {e}")