def whatTime(seconds):
    hours = int(seconds/3600)
    seconds = seconds - (hours*3600)
    minutes = int(seconds/60)
    seconds = seconds - (minutes*60)
    return str(hours) + ":" + str(minutes) + ":" + str(seconds)

print(whatTime(3661))
