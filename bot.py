#!/usr/bin/env python3
import sys, json, random

random.seed(1)
first_tick = True

move = "N"
for line in sys.stdin:
    data = json.loads(line)
    if first_tick:
        config = data.get("config", {})
        width = config.get("width")
        height = config.get("height")
        print(f"Elisa launching on a {width}x{height} map",
              file=sys.stderr, flush=True)

    unspos_x = data.get("bot")[0]
    unspos_y = data.get("bot")[1]
    gem = data.get("visible_gems")
    if len(gem) == 0:
        move = random.choice(["N", "S", "E", "W"])
    else:
        gempos_x = gem[0]["position"][0]
        gempos_y = gem[0]["position"][1]
        if gempos_x < unspos_x:
            move = "W"
        elif gempos_x > unspos_x:
            move = "E"
        elif gempos_y > unspos_y:
            move = "S"
        elif gempos_y < unspos_y:
            move = "N"

        print(f"wir x:{unspos_x}, y:{unspos_y}; Edelstein x: {gempos_x}, y: {gempos_y}", file=sys.stderr, flush=True)

    print(move, flush=True)

    first_tick = False
