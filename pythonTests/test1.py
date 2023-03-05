from collections import deque 

#   Save last n items per object invocation
SAMPLES = 100

#   Creates empty queue 
history_samples= deque(maxlen=SAMPLES)
for i in range(100):
    history_samples.append(i)

print(*history_samples, sep='\n')