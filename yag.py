import yagmail

reviver="singhmanmeet523@gmail.com"
body="message fron yagmail"

yag=yagmail.SMTP("manmeettestpython@gmail.com")
yag.send(to=reviver,subject="yagmail test",contents=body)