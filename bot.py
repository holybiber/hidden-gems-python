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
        zielpos_x = round(width/2)
        zielpos_y = round(width/2)
    else:
        zielpos_x = gem[0]["position"][0]
        zielpos_y = gem[0]["position"][1]

    if zielpos_x < unspos_x:
        move = "W"
    elif zielpos_x > unspos_x:
        move = "E"
    elif zielpos_y > unspos_y:
        move = "S"
    elif zielpos_y < unspos_y:
        move = "N"
    else:
        move = "WAIT"

    print(f"wir x:{unspos_x}, y:{unspos_y}; Ziel x: {zielpos_x}, y: {zielpos_y}", file=sys.stderr, flush=True)

    print(move, flush=True)

    first_tick = False
