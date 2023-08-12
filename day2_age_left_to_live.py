expected_age = int(input("What age would you want to like up to: "))
current_age = int(input("What is your current age: "))
hours = 788400
days = 365
weeks = 52
months = 12

n_years = expected_age - current_age
n_months = (months * n_years)
n_weeks = (weeks * n_years)
n_days = (days * n_years)
n_hours = (hours * n_years)
life_time = (f"- Current age {current_age} years\n"
             f"- Remaining: {n_years} years to reach: {expected_age} years\n"
             f"You have {n_months} months, "
             f"{n_weeks} weeks, "
             f"{n_days} days, and "
             f"{n_hours} hours left to reach {expected_age} years.")
print(life_time)
