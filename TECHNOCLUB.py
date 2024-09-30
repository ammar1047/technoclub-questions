data_table = [
    {"No": 1, "Nama": "Haikal", "Kelas": "IF21B"},
    {"No": 2, "Nama": "Mr. Santai", "Kelas": "IF21B"},
    {"No": 3, "Nama": "Kisah", "Kelas": "IF22C"},
    {"No": 4, "Nama": "Ajag", "Kelas": "IF23B"}
]


for i in range(100):
    print("Saya Teknik Informatika (for loop)")

# Using a while loop
count = 0
while count < 100:
    print("Saya Teknik Informatika (while loop)")
    count += 1

x, y, z = True, False, True

and_result = x and y  # False

or_result = x or y  # True

not_result = not z  # False

print("AND result:", and_result)
print("OR result:", or_result)
print("NOT result:", not_result)

a, b = 5, 10

gt_result = a > b  # False

le_result = a <= b  # True

eq_result = a == b  # False

print("Greater than result:", gt_result)
print("Less than or equal result:", le_result)
print("Equal result:", eq_result)

mod_result = 1 % 2  # 1
print("1 % 2 result:", mod_result)


def greeting(name):
    return f"Hello, {name}!"

def simple_greeting():
    return "Hello, World!"

print(greeting("Haikal"))
print(simple_greeting())