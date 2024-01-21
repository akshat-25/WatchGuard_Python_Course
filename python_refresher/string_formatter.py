name = "Bob"
greeting = f"Hello, {name}"

print(greeting)
print(f"Hello {name}")

name = "Rolf"

print(greeting)

print(f"Hello {name}")

with_name = greeting.format(name)

long_phrase = "Hello, {}. Today is {}."

formatted = long_phrase.format("Akshat","Friday")
print(formatted)
