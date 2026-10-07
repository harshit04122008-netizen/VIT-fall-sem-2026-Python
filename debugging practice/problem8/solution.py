n = int(input())
event_a = set(input().split())
m = int(input())
event_b = set(input().split())

all_participants = sorted(event_a | event_b)


print("All Participants:", ' '.join(all_participants))