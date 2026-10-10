from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import json
import os


# ==========================================
# PATHS
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

FRONT_DIR = os.path.join(
    BASE_DIR,
    "Front"
)

PUBLIC_DIR = os.path.join(
    FRONT_DIR,
    "public"
)

CONTACTS_FILE = os.path.join(
    BASE_DIR,
    "contacts.json"
)


# ==========================================
# FLASK
# ==========================================

app = Flask(
    __name__,
    template_folder=FRONT_DIR
)

# =========================
# CSS
# =========================

@app.route("/style.css")
def style_css():
    return send_from_directory(
        os.path.join(BASE_DIR, "Front", "public"),
        "style.css"
    )
# ==========================================
# PUBLIC FILES
# ==========================================

@app.route("/public/<path:filename>")
def public_files(filename):

    return send_from_directory(
        PUBLIC_DIR,
        filename
    )


# ==========================================
# CONTACTS
# ==========================================

def load_contacts():

    try:

        with open(
            CONTACTS_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)

    except FileNotFoundError:

        return {
            "contacts": [],
            "numbers": []
        }

    except json.JSONDecodeError:

        return {
            "contacts": [],
            "numbers": []
        }


def save_contacts(data):

    with open(
        CONTACTS_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )


# ==========================================
# HOME
# ==========================================

@app.route("/")
def index():

    data = load_contacts()

    contacts = data.get(
        "contacts",
        []
    )

    numbers = data.get(
        "numbers",
        []
    )

    search = request.args.get(
        "search",
        ""
    ).strip()

    result = []

    for index, name in enumerate(contacts):

        if (
            search
            and search.lower() not in name.lower()
        ):
            continue

        if index < len(numbers):

            number = numbers[index]

        else:

            number = "بدون شماره"

        result.append({
            "index": index,
            "name": name,
            "number": number
        })

    return render_template(
        "index.html",
        contacts=result,
        search=search,
        message=request.args.get(
            "message"
        )
    )


# ==========================================
# ADD
# ==========================================

@app.route(
    "/add",
    methods=["POST"]
)
def add():

    name = request.form.get(
        "name",
        ""
    ).strip()

    number = request.form.get(
        "number",
        ""
    ).strip()

    data = load_contacts()

    contacts = data.get(
        "contacts",
        []
    )

    numbers = data.get(
        "numbers",
        []
    )


    if not name:

        return redirect(
            url_for(
                "index",
                message="نام را وارد کنید!"
            )
        )


    if name in contacts:

        return redirect(
            url_for(
                "index",
                message="این مخاطب قبلاً وجود دارد!"
            )
        )


    if (
        not number.isdigit()
        or len(number) != 11
    ):

        return redirect(
            url_for(
                "index",
                message="شماره باید 11 رقم باشد!"
            )
        )


    contacts.append(name)

    numbers.append(number)

    data["contacts"] = contacts

    data["numbers"] = numbers

    save_contacts(data)


    return redirect(
        url_for(
            "index",
            message="مخاطب با موفقیت اضافه شد!"
        )
    )


# ==========================================
# DELETE
# ==========================================

@app.route(
    "/delete/<int:index>",
    methods=["POST"]
)
def delete(index):

    data = load_contacts()

    contacts = data.get(
        "contacts",
        []
    )

    numbers = data.get(
        "numbers",
        []
    )


    if (
        index < 0
        or index >= len(contacts)
    ):

        return redirect(
            url_for(
                "index",
                message="مخاطب پیدا نشد!"
            )
        )


    deleted_name = contacts[index]

    contacts.pop(index)


    if index < len(numbers):

        numbers.pop(index)


    data["contacts"] = contacts

    data["numbers"] = numbers

    save_contacts(data)


    return redirect(
        url_for(
            "index",
            message=f"{deleted_name} حذف شد!"
        )
    )


# ==========================================
# RUN
# ==========================================

if __name__ == "__main__":

    print()
    print("================================")
    print(" Blade Contacts Manager")
    print("================================")
    print()
    print("Website:")
    print("http://127.0.0.1:5000")
    print()
    print("Public:")
    print("http://127.0.0.1:5000/public/")
    print()
    print("================================")
    print()

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )