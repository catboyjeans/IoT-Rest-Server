from collections import deque 

#   Save last n items per object invocation
SAMPLES = 10

#   Creates empty queue 
history_samples= deque(maxlen=SAMPLES)
for i in range(100):
    history_samples.append(i)

print(*history_samples, sep='\n')

#   Test the update thing

query = {}

query.update(a=1)
print(query)

query.update(a=2)
print(query)

query.update(a=3)
print(query)


