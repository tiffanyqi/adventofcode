from datetime import datetime

logs = []
with open('input.txt') as inputfile:
    for line in inputfile:
        log = line.strip().split('\n')[0].split('] ')
        date = datetime.strptime(log[0][1:], '%Y-%m-%d %H:%M')
        entry = log[1] # falls asleep , wakes up , Guard #3559 begins shift
        logs.append({
            'date': date,
            'entry': entry,
        })

logs.sort(key=(lambda key: key['date']))
records = {}
guard_id = 0
prev_time = 0

for log in logs:
    logged_minute = log['date'].minute
    entry = log['entry']
    if entry[0] == 'G': # guard begins shift
        guard_id = int(entry.split(' ')[1][1:])
    elif entry[0] == 'f': # falls asleep
        prev_time = logged_minute
    else: # wakes up
        if guard_id in records:
            records[guard_id]['total'] += logged_minute - prev_time
        else:
            records[guard_id] = {
                'total': logged_minute - prev_time,
                'minutes': {},
            }

        for minute in range(prev_time, logged_minute):
            if minute not in records[guard_id]['minutes']:
                records[guard_id]['minutes'][minute] = 1
            else:
                records[guard_id]['minutes'][minute] += 1

def most_minutes_strategy():
    guard_with_max_minutes = max(records.keys(), key=(lambda key: records[key]['total']))
    guard_minutes = records[guard_with_max_minutes]['minutes']
    max_minute = max(guard_minutes.keys(), key=(lambda key: guard_minutes[key]))
    return guard_with_max_minutes * max_minute

def most_frequency_minute_strategy():
    guard_with_most_frequency = 0
    max_minute = 0
    max_minute_value = 0
    for guard_id in records.keys():
        guard_minutes = records[guard_id]['minutes']
        minute_key = max(guard_minutes.keys(), key=(lambda key: guard_minutes[key]))
        minute_value = guard_minutes[minute_key]
        if minute_value > max_minute_value:
            max_minute = minute_key
            max_minute_value = minute_value
            guard_with_most_frequency = guard_id
    print(guard_with_most_frequency, max_minute)
    print(records[guard_with_most_frequency])
    return guard_with_most_frequency * max_minute

print(most_frequency_minute_strategy())
