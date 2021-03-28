# A class for each guard
class Guard:
    # Constructor: ID, with 0 minutes asleep
    def __init__(self, ID):
        self.ID = ID
        self.time_span = [0 for i in range(60)]

    # Given a sleep start and end, increment all minutes in that span
    def increment_span(self, start, end):
        for t in range(start, end):
            self.time_span[t] += 1

    # Find the minute with the most time asleep for this guard
    def find_mode_minute(self):
        max_val = max(self.time_span)
        for t in range(len(self.time_span)):
            if self.time_span[t] == max_val:
                return t
            
        return -1

    # Get the number of minutes asleep
    def find_minutes_asleep(self):
        return sum(self.time_span)

def sort_entries(doc_name):
    log = open(doc_name)
    line = log.readline()
    day_dict = {}

    while line != "":
        # Split into date, time, description
        ini_split = line.split("] ") # Split by time; info
        date, time = ini_split[0][6:].split()
        desc = ini_split[1]
        date = date + "-" + time.split(":")[0]

        # Add data
        if date not in day_dict.keys():
            day_dict[date] = []
        day_dict[date].append((int(time.split(":")[1]), desc.strip()))
            
        # Get next entry
        line = log.readline()

    log.close()

    # Sort by timestamp
    for day in day_dict.keys():
        day_dict[day].sort(key=lambda entry: entry[0])

    sorted_days = sorted(day_dict.keys(),
                         key=lambda date: int("".join(date.split("-"))))

    # Final list is built from sorted dates
    final_list = []
    for date in sorted_days:
        final_list += day_dict[date]
    
    return final_list

def generate_guard_records(records):
    # Sort sleep info by guards
    guards = []
    current_id = -1
    sleep_start = -1
    sleep_end = -1      
    for record in records:
        record_parts = record[1].split()
        # New guard entry
        if record_parts[0] == "Guard":
            current_id = int(record_parts[1][1:])

            # Add new guard if not already recorded
            for guard in guards:
                if guard.ID == current_id:
                    break
            else:
                guards.append(Guard(current_id))
                
            continue
        # End new guard entry
        
        # Check ID has been set
        if current_id    == -1:
            raise IndexError("ID not set")

        # Add sleep record
        if record_parts[0] == "falls":
            if sleep_start != -1 or sleep_end != -1:
                raise IndexError("Stray Sleep Record")

            sleep_start = record[0]
        elif record_parts[0] == "wakes":
            sleep_end = record[0]

            for guard in guards:
                if guard.ID == current_id:
                    guard.increment_span(sleep_start, sleep_end)
                    break
            else:
                raise IndexError("Guard not found")

            sleep_end = -1
            sleep_start = -1
        # End sleep record
        else:
            print("Unknown Record Found")

    return guards

if __name__ == "__main__":
    sorted_info = sort_entries("input.txt")
    guards = generate_guard_records(sorted_info)
            
    print([(guard.ID, guard.find_minutes_asleep()) for guard in guards])

    max_sleep = max([guard.find_minutes_asleep() for guard in guards])
    for guard in guards:
        if guard.find_minutes_asleep() == max_sleep:
            print((guard.ID, guard.find_mode_minute()))
            print(guard.ID* guard.find_mode_minute())
