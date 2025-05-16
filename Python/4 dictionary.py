#dictionaries in python allow users to store key value pairs
month_Convert = {
    "Jan": "January", #key: value, keys can be numbers but have to be unique
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(month_Convert["Nov"])
print(month_Convert.get("Dec"))
print(month_Convert.get("Hey", "Not a valid key")) #if not a key, shows 'None' or the inputed version


month = input("Input a key: ")
print(month_Convert[month])


