seconds = 3665
minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
days, hours = divmod(hours, 24)
print(f"""
days: {days},
hours: {hours},
minutes: {minutes},
seconds: {seconds}
""")