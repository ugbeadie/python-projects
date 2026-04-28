# import base64
# from io import BytesIO

# from flask import Flask, render_template_string, request
# import qrcode

# app = Flask(__name__)

# PAGE_TEMPLATE = """
# <!doctype html>
# <html lang="en">
# <head>
#     <meta charset="utf-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1">
#     <title>QR Code Generator</title>
#     <style>
#         :root {
#             color-scheme: light;
#             --bg: #f7f2ea;
#             --card: #fffdf9;
#             --ink: #1f2933;
#             --muted: #52606d;
#             --accent: #c2410c;
#             --accent-dark: #9a3412;
#             --line: #ead9c8;
#         }

#         * {
#             box-sizing: border-box;
#         }

#         body {
#             margin: 0;
#             min-height: 100vh;
#             font-family: "Segoe UI", sans-serif;
#             color: var(--ink);
#             background:
#                 radial-gradient(circle at top left, #ffe7c2 0, transparent 30%),
#                 linear-gradient(135deg, #f8f1e7, #f3ebe2 55%, #efe4d8);
#             display: grid;
#             place-items: center;
#             padding: 24px;
#         }

#         .card {
#             width: min(720px, 100%);
#             background: rgba(255, 253, 249, 0.92);
#             backdrop-filter: blur(10px);
#             border: 1px solid rgba(234, 217, 200, 0.9);
#             border-radius: 24px;
#             padding: 28px;
#             box-shadow: 0 24px 60px rgba(84, 56, 20, 0.12);
#         }

#         h1 {
#             margin: 0 0 10px;
#             font-size: clamp(2rem, 4vw, 3rem);
#         }

#         p {
#             margin: 0 0 20px;
#             color: var(--muted);
#             line-height: 1.5;
#         }

#         form {
#             display: grid;
#             gap: 14px;
#         }

#         textarea {
#             width: 100%;
#             min-height: 110px;
#             resize: vertical;
#             border: 1px solid var(--line);
#             border-radius: 16px;
#             padding: 16px;
#             font: inherit;
#             background: #fff;
#         }

#         button {
#             width: fit-content;
#             border: 0;
#             border-radius: 999px;
#             padding: 12px 20px;
#             font: inherit;
#             font-weight: 700;
#             color: white;
#             background: linear-gradient(135deg, var(--accent), var(--accent-dark));
#             cursor: pointer;
#         }

#         .message {
#             margin-top: 16px;
#             padding: 12px 14px;
#             border-radius: 14px;
#             background: #fff1e8;
#             color: var(--accent-dark);
#         }

#         .preview {
#             margin-top: 24px;
#             padding: 22px;
#             border: 1px solid var(--line);
#             border-radius: 20px;
#             background: white;
#             display: grid;
#             justify-items: center;
#             gap: 14px;
#         }

#         .preview img {
#             width: min(280px, 100%);
#             height: auto;
#             border-radius: 16px;
#         }

#         .preview code {
#             max-width: 100%;
#             overflow-wrap: anywhere;
#             padding: 8px 10px;
#             border-radius: 10px;
#             background: #f7f2ea;
#         }
#     </style>
# </head>
# <body>
#     <main class="card">
#         <h1>QR Code Generator</h1>
#         <p>Paste a link or any text below. Submit the form and the QR code appears instantly in the browser.</p>

#         <form method="post">
#             <textarea name="data" placeholder="https://example.com">{{ data }}</textarea>
#             <button type="submit">Generate QR Code</button>
#         </form>

#         {% if message %}
#         <div class="message">{{ message }}</div>
#         {% endif %}

#         {% if qr_code %}
#         <section class="preview">
#             <img src="data:image/png;base64,{{ qr_code }}" alt="Generated QR code">
#             <code>{{ data }}</code>
#         </section>
#         {% endif %}
#     </main>
# </body>
# </html>
# """


# def build_qr_code(data: str) -> str:
#     qr = qrcode.QRCode(box_size=10, border=4)
#     qr.add_data(data)
#     qr.make(fit=True)

#     image = qr.make_image(fill_color="black", back_color="white")
#     image_buffer = BytesIO()
#     image.save(image_buffer, format="PNG")
#     return base64.b64encode(image_buffer.getvalue()).decode("ascii")


# @app.route("/", methods=["GET", "POST"])
# def index() -> str:
#     data = ""
#     qr_code = ""
#     message = ""

#     if request.method == "POST":
#         data = request.form.get("data", "").strip()
#         if data:
#             qr_code = build_qr_code(data)
#         else:
#             message = "Paste a link or text before generating a QR code."

#     return render_template_string(PAGE_TEMPLATE, data=data, qr_code=qr_code, message=message)


# if __name__ == "__main__":
#     app.run(debug=True)

age = 30
height = 1.75
z = 3 + 4j

def area_triangle():
    base = float(input("enter base: "))
    height = float(input("enter height: "))
    print(f"area of triangle is {0.5 * base * height}")

def perimeter_triangle():
    a = float(input("enter side a: "))
    b = float(input("enter side b: "))
    c = float(input("enter side c: "))
    print(f"perimeter of triangle is {a + b + c}")

# # perimeter_triangle()
# word1 = "python"
# word2 = "dragon"

# print(len(word1))  # 6
# print(len(word2))  # 6

# # falsy comparison (both lengths equal → False condition)
# print(len(word1) != len(word2))  # False

# print("jargon" in "I hope this course is not full of jargon.")

# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
# gr, fr, bg, sw, *scandic, es = countries
# print(gr) 
# print(fr)
# print(bg)
# print(sw)
# print(scandic)
# print(es)

# fruits = ['banana', 'orange', 'mango', 'lemon']

# fruit = input("Enter a fruit: ")

# if fruit in fruits:
#     print("That fruit already exist in the list")
# else:
#     fruits.append(fruit)
#     print(fruits)

# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python','Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# # 1. Check if 'skills' exists and print middle skill
# if 'skills' in person:
#     skills = person['skills']
#     middle_index = len(skills) // 2
#     print("Middle skill:", skills[middle_index])


# person = {
#     'first_name': 'Asabeneh',
#     'last_name': 'Yetayeh',
#     'age': 250,
#     'country': 'Finland',
#     'is_married': True,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }
# for skill in person.get('skills', []):
#     print(skill)

# from datetime import datetime

# name = input("Give me your name: ")
# age = int(input("Give me your name: "))

# current_year = datetime.now().year
# year_100 = current_year + (100 - age)

# print(f"{name}, you will turn 100 years old in {year_100}.")
  
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# num = int(input("Enter a number: "))

# new_list = []

# for item in a:
#     if item < num:
#         new_list.append(item)

# print(new_list)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# num = int(input("Enter a number: "))
# print([item for item in a if item < num])

# def arbitrary_named_args(**args):
#     print("I received an arbitrary number of arguments, totaling", len(args))
#     print("They are provided as a dictionary in my function:", type(args))
#     print("Let's print them:")
#     for k, v in args.items():
#         print(" * key:", k, "value:", v)

# def addToNumbers(a,b):
#     sum = a+b
#     print (sum)
#     return sum

# addToNumbers(2,3)

# try:
#     f=open("names.txt")
#     print(f.read())
# except FileNotFoundError:
#     print("The file 'names.txt' does not exist.")
# finally:
#     f.close()

# f = open("names.txt", "a")
# f.write("\nUgbe")
# f.close()

# f = open("names.txt")
# print(f.read())
# f.close()

# f = open("names.txt", "w")
# f.write("")
# f.close()

with open(r"C:\Users\DELL\Desktop\groceries.txt", "a") as f:
    f.write("\nbanana")