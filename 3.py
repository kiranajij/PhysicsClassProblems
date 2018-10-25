import csv

name = raw_input("Please enter your name:\t")
password = raw_input("Please enter your password:\t")

with open("login_info.csv", "a+") as data:
    csv_reader = csv.reader(data, delimiter=",")
    for row in csv_reader:
        if row[0] == name:
            if row[1] == password:
                print "Password Matched"
            else:
                print "Wrong Password"

            break
    else:
        writer = csv.writer(data)
        writer.writerow([name, password])
        print "Your name has been entered successfully"
