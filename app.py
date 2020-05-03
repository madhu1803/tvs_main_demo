from flask import Flask, render_template, request, redirect, flash
from datetime import datetime
import forms
import mysql.connector
from mysql.connector.errors import ProgrammingError
import json
from datetime import date

app = Flask(__name__)
import copy

mydb = mysql.connector.connect(host="localhost", database="main_test", user="root",password="")
mycursor = mydb.cursor(buffered=True)

"""
Three tables:
    1. form1
    2. form2
    3. form3

Columns:
    1. id (not null, primary key, auto increment)
    2. date (DATE, default DATE/CURRENT_TIMESTAMP, Not null)
"""

# redirect route
@app.route("/")
def index():
    return redirect("/create")


# create route
@app.route("/create", methods=["GET", "POST"])
def form():
    # get date
    today = date.today().strftime("%Y-%m-%d")

    # define init forms | for fields
    form1 = forms.Form1Form()
    form2 = forms.Form2Form()
    form3 = forms.Form3Form()

    # fetching top 3 reasons
    # mycursor.execute(f"select id from complaints_table order by no_of_complaints DESC limit 3;")
    # records = mycursor.fetchall()
    # NOTE: records table not found
    records = [1, 2, 3]

    # coping dict
    data1 = copy.deepcopy(form1.data)
    data2 = copy.deepcopy(form2.data)
    data3 = copy.deepcopy(form3.data)

    # deleting csrf token
    del data1["csrf_token"]
    del data2["csrf_token"]
    del data3["csrf_token"]

    # select query for 3 three forms
    try:
        # will throw error is the columns are not in table
        # happens when user is visiting the page for first time and columns are not created
        mycursor.execute(
            f"SELECT {', '.join(data1.keys())} FROM form1 where date='{today}'"
        )
        raw_data1 = mycursor.fetchall()
        mycursor.execute(
            f"SELECT {', '.join(data2.keys())} FROM form2 where date='{today}'"
        )
        raw_data2 = mycursor.fetchall()
        mycursor.execute(
            f"SELECT {', '.join(data3.keys())} FROM form3 where date='{today}'"
        )
        raw_data3 = mycursor.fetchall()
    except:
        # override it by creating empty list
        raw_data1 = []
        raw_data2 = []
        raw_data3 = []

    # checking for form data
    if len(raw_data1) == 0 and len(raw_data2) == 0 and len(raw_data3) == 0:
        form1 = forms.Form1Form()
        form2 = forms.Form2Form()
        form3 = forms.Form3Form()
    else:
        # if form data exists retrieve them
        # form1
        values1 = raw_data1[0]
        names1 = [name for name in data1.keys()]
        data_form1 = {}
        for index in range(len(values1)):
            data_form1[names1[index]] = values1[index]
        form1 = forms.Form1Form(data=data_form1)
        # form2
        values2 = raw_data2[0]
        names2 = [name for name in data2.keys()]
        data_form2 = {}
        for index in range(len(values2)):
            data_form2[names2[index]] = values2[index]
        form2 = forms.Form2Form(data=data_form2)
        # form3
        values3 = raw_data3[0]
        names3 = [name for name in data3.keys()]
        data_form3 = {}
        for index in range(len(values3)):
            data_form3[names3[index]] = values3[index]
        form3 = forms.Form3Form(data=data_form3)

    if request.method == "POST":
        # get the data and seperate as forms
        data = json.loads(request.data)
        form1_data = data["form1"]
        form2_data = data["form2"]
        form3_data = data["form3"]
        # breakpoint()

        # override the forms and create a new form from data
        form1 = forms.Form1Form(data=form1_data)
        form2 = forms.Form2Form(data=form2_data)
        form3 = forms.Form3Form(data=form3_data)

        # check valid
        if form1.validate() and form2.validate() and form3.validate():
            # remove csrf
            form1_data.pop("csrf_token")
            form2_data.pop("csrf_token")
            form3_data.pop("csrf_token")
            # add date to the data
            form1_data["date"] = today
            form2_data["date"] = today
            form3_data["date"] = today

            # valid and new entry | create
            if len(raw_data1) == 0 and len(raw_data2) == 0 and len(raw_data3) == 0:
                # for form 1
                for name in form1_data.keys():
                    try:
                        mycursor.execute(f"SELECT {name} from `form1`;")
                        mycursor.fetchone()
                    except:
                        mycursor.execute(
                            f"ALTER TABLE `form1` add {name} text NULL DEFAULT NULL;"
                        )
                form1_names = form1_data.keys()
                form1_values = form1_data.values()
                mycursor.execute(
                    f"INSERT INTO form1 ({', '.join(form1_names)}) VALUES {tuple(form1_values)};"
                )
                # for form 2
                for name in form2_data.keys():
                    try:
                        mycursor.execute(f"SELECT {name} from `form2`;")
                        mycursor.fetchone()
                    except:
                        mycursor.execute(
                            f"ALTER TABLE `form2` add {name} text NULL DEFAULT NULL;"
                        )
                form2_names = form2_data.keys()
                form2_values = form2_data.values()
                mycursor.execute(
                    f"INSERT INTO form2 ({', '.join(form2_names)}) VALUES {tuple(form2_values)};"
                )
                # for form 3
                for name in form3_data.keys():
                    try:
                        mycursor.execute(f"SELECT {name} from `form3`;")
                        mycursor.fetchone()
                    except:
                        mycursor.execute(
                            f"ALTER TABLE `form3` add {name} text NULL DEFAULT NULL;"
                        )
                form3_names = form3_data.keys()
                form3_values = form3_data.values()
                mycursor.execute(
                    f"INSERT INTO form3 ({', '.join(form3_names)}) VALUES {tuple(form3_values)};"
                )

            # valid and old entry | update
            else:
                # form1
                for name, value in form1_data.items():
                    mycursor.execute(
                        f"UPDATE form1 SET {name}='{value}' WHERE date='{today}'"
                    )
                # form2
                for name, value in form2_data.items():
                    mycursor.execute(
                        f"UPDATE form2 SET {name}='{value}' WHERE date='{today}'"
                    )
                # form3
                for name, value in form3_data.items():
                    mycursor.execute(
                        f"UPDATE form3 SET {name}='{value}' WHERE date='{today}'"
                    )

            # save
            mydb.commit()
            return "success"

        # form is invalid
        return "error"

    return render_template(
        "main.html", form1=form1, form2=form2, form3=form3, records=records
    )


# detail view
@app.route("/detail", methods=["GET", "POST"])
def detail():
    # define init forms | for fields
    form1 = forms.Form1Form()
    form2 = forms.Form2Form()
    form3 = forms.Form3Form()

    # fetching top 3 reasons
    # mycursor.execute(f"select id from complaints_table order by no_of_complaints DESC limit 3;")
    # records = mycursor.fetchall()
    # NOTE: records table not found
    records = [1, 2, 3]

    date = None

    if request.method == "POST":
        date = request.form["selected_date"]

        # copy dict
        form1_data = copy.deepcopy(form1.data)
        form2_data = copy.deepcopy(form2.data)
        form3_data = copy.deepcopy(form3.data)
        # del csrf token
        form1_data.pop("csrf_token")
        form2_data.pop("csrf_token")
        form3_data.pop("csrf_token")

        try:
            # get the data
            mycursor.execute(
                f"SELECT {', '.join(form1_data.keys())} FROM form1 where date='{date}'"
            )
            raw_data1 = mycursor.fetchall()

            mycursor.execute(
                f"SELECT {', '.join(form2_data.keys())} FROM form2 where date='{date}'"
            )
            raw_data2 = mycursor.fetchall()

            mycursor.execute(
                f"SELECT {', '.join(form3_data.keys())} FROM form3 where date='{date}'"
            )
            raw_data3 = mycursor.fetchall()

        except:
            # date not found | empty the list
            raw_data1 = []
            raw_data2 = []
            raw_data3 = []

        if len(raw_data1) == 0:
            flash("Data not found for the given date. Please try another date.")
        else:
            # form1
            values1 = raw_data1[0]
            names1 = [name for name in form1_data.keys()]
            data_form1 = {}
            for index in range(len(values1)):
                data_form1[names1[index]] = values1[index]
            form1 = forms.Form1Form(data=data_form1)

            # form2
            values2 = raw_data2[0]
            names2 = [name for name in form2_data.keys()]
            data_form2 = {}
            for index in range(len(values2)):
                data_form2[names2[index]] = values2[index]
            form2 = forms.Form2Form(data=data_form2)

            # form3
            values3 = raw_data3[0]
            names3 = [name for name in form3_data.keys()]
            data_form3 = {}
            for index in range(len(values3)):
                data_form3[names3[index]] = values3[index]
            form3 = forms.Form3Form(data=data_form3)

    return render_template(
        "detail.html", form1=form1, form2=form2, form3=form3, records=records, date=date
    )


if __name__ == "__main__":
    app.secret_key = "secret"
    app.run(debug=True)
