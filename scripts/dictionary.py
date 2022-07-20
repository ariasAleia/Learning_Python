month_conversions = {
    "Jan": "January",
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

print(month_conversions["Feb"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Derc"))
print(month_conversions.get("Derc", "Key was not found :P"))