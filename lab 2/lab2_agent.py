# Lab 2: classroom agent. Temp in Celsius, occupied is True/False.
# ECO, COOL, WARM, IDLE are mode labels only, no real hardware.
# Empty room has priority. At exactly 20 or 26 degrees, occupied room = IDLE.

class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied:
            return "ECO"
        if temp > 26:
            return "COOL"
        if temp < 20:
            return "WARM"
        return "IDLE"

class StatefulAgent(ClassroomAgent):
    def __init__(self):
        self.previous = None

    def act_stateful(self, temp, occupied):
        target = self.act(temp, occupied)
        send = target != self.previous  # send only when mode changes
        self.previous = target
        return target, send

print("Part 1: reflex agent (manual sequence)")
agent = ClassroomAgent()
percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
for step, (temp, occupied) in enumerate(percepts, 1):
    print(step, (temp, occupied), "->", agent.act(temp, occupied))

print("\nPart 2: stateful agent (Task 3 trace)")
stateful = StatefulAgent()
trace = [(29, True), (29, True), (20, True), (26, True),
         (19, True), (29, False), (29, False)]
for temp, occupied in trace:
    previous = stateful.previous
    target, send = stateful.act_stateful(temp, occupied)
    print("previous:", previous, "| percept:", (temp, occupied),
          "| target:", target, "|", "send command" if send else "no command")

print("\nPart 3: check - noisy sequence around 26 degrees")
noisy = StatefulAgent()
for temp, occupied in [(25, True), (27, True), (25, True), (27, True)]:
    target, send = noisy.act_stateful(temp, occupied)
    print((temp, occupied), "->", target, "| send:", send)
print("Note: memory does not stop switching when the target keeps changing.")
