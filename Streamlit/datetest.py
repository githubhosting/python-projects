from datetime import date

dob = "2003-03-05"
formated = date.fromisoformat(dob).strftime("%d  %B  %Y")
