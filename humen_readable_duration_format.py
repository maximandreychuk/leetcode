# Your task in order to complete this Kata is
# to write a function which formats a duration, given
# as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer.
# If it is zero, it just returns "now". Otherwise,
# the duration is expressed as a combination of years,
# days, hours, minutes and seconds.

def format_duration(seconds: int) -> str:
    if seconds == 0:
        return "now"
    elif seconds < 60:
        if seconds == 1:
            return f"{seconds} second"
        return f"{seconds} seconds"
    elif seconds >= 60 and seconds < 3600:
        sec, min = seconds % 60, seconds // 60
        if sec == 1 and min == 1:
            return f"{min} minute and {sec} second"
        elif sec == 1 and min != 1:
            return f"{min} minutes and {sec} second"
        elif sec != 1 and min == 1:
            return f"{min} minute and {sec} seconds"
        return f"{min} minutes and {sec} seconds"
    elif seconds >= 3600 and seconds < 86400:
        hour = seconds // 3600
        if hour > 1:
            hour_str = f"{hour} hours"
        else:
            hour_str = f"{hour} hour"
        min = (seconds - hour * 3600) // 60
        if min > 1:
            min_str = f"{min} minutes"
        else:
            min_str = f"{min} minute"
        sec = (seconds - hour * 3600 )- (min * 60)
        if sec > 1:
            sec_str = f"{sec} seconds"
        else:
            sec_str = f"{sec} second"
        return f"{hour_str}, {min_str} and {sec_str}"
    elif seconds >= 86400 and seconds < 31536000:
        day = seconds // 86400
        if day > 1:
            day_str = f"{day} days"
        else:
            day_str = f"{day} day"
        hour = (seconds - (day * 86400)) // 3600
        if hour > 1:
            hour_str = f"{hour} hours"
        else:
            hour_str = f"{hour} hour"
        min = (seconds - hour * 3600 - day * 86400) // 60
        if min > 1:
            min_str = f"{min} minutes"
        else:
            min_str = f"{min} minute"
        sec = (seconds - hour * 3600-day * 86400-min * 60 ) % 60
        if sec > 1:
            sec_str = f"{sec} seconds"
        else:
            sec_str = f"{sec} second"
        return f"{day_str}, {hour_str}, {min_str} and {sec_str}"
    elif seconds >= 31536000:
        year = seconds // 31536000
        if year > 1:
            year_str = f"{year} years"
        else:
            year_str = f"{year} year"
        day = (seconds - year * 31536000) // 86400
        if day > 1:
            day_str = f"{day} days"
        else:
            day_str = f"{day} day"
        hour = (seconds - year * 31536000 - day * 86400) // 3600
        if hour > 1:
            hour_str = f"{hour} hours"
        else:
            hour_str = f"{hour} hour"
        min = (seconds - year * 31536000 - day * 86400 - hour * 3600) // 60
        if min > 1:
            min_str = f"{min} minutes"
        else:
            min_str = f"{min} minute"
        sec = (seconds - year * 31536000- hour * 3600 - day * 86400 - min * 60) % 60
        if sec > 1:
            sec_str = f"{sec} seconds"
        else:
            sec_str = f"{sec} second"
        return f"{year_str}, {day_str}, {hour_str}, {min_str} and {sec_str}"



# (format_duration(3600), "1 hour")
# (format_duration(3662), "1 hour, 1 minute and 2 seconds")
# (format_duration(15731080), "182 days, 1 hour, 44 minutes and 40 seconds")

print(format_duration(15731080)) # "182 days, 1 hour, 44 minutes and 40 seconds"
print(format_duration(132030240)) # "4 years, 68 days, 3 hours and 4 minutes")
print(format_duration(15731080))
print(format_duration(3662))
print(format_duration(7201))
print(format_duration(3570))