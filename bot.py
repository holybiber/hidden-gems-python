#!/usr/bin/env python3
import sys, json, random

random.seed(1)
erste_runde = True


def entfernung(pos1_x, pos1_y, pos2_x, pos2_y):
    if pos1_x > pos2_x:
        abstand_x = pos1_x - pos2_x
    else:
        abstand_x = pos2_x - pos1_x

    if pos1_y > pos2_y:
        abstand_y = pos1_y - pos2_y
    else:
        abstand_y = pos2_y - pos1_y

    return abstand_x + abstand_y


# Bestimme das nächste Ziel (nächster Edelstein)
# Wenn wir kein Edelstein in Sichtweite haben, geben wir (-1, -1) zurück
def nächstes_ziel(unspos_x, unspos_y, gems):
    ziel_x = -1
    ziel_y = -1
    kleinste_entfernung = 1000

    for gem in gems:
        gem_x = gem["position"][0]
        gem_y = gem["position"][1]
        gem_entfernung = entfernung(unspos_x, unspos_y, gem_x, gem_y)
        if gem_entfernung < kleinste_entfernung:
            ziel_x = gem_x
            ziel_y = gem_y
            kleinste_entfernung = gem_entfernung

    return (ziel_x, ziel_y)


def ist_mauer(pos_x, pos_y, mauern):
    for mauer in mauern:
        if mauer[0] == pos_x and mauer[1] == pos_y:
            return True
    return False


if __name__ == '__main__':
    for line in sys.stdin:
        data = json.loads(line)

        if erste_runde:
            config = data.get("config", {})
            breite = config.get("width")
            höhe = config.get("height")
            print(f"Elisa launching on a {breite}x{höhe} map",
                file=sys.stderr, flush=True)

        unspos_x = data.get("bot")[0]
        unspos_y = data.get("bot")[1]
        gems = data.get("visible_gems")

        (zielpos_x, zielpos_y) = nächstes_ziel(unspos_x, unspos_y, gems)
        if zielpos_x == -1 and zielpos_y == -1:
            move = random.choice(["W", "E", "S", "N"])
        elif zielpos_x < unspos_x and not ist_mauer(unspos_x - 1, unspos_y, data.get('wall')):
            move = "W"
        elif zielpos_x > unspos_x and not ist_mauer(unspos_x + 1, unspos_y, data.get('wall')):
            move = "E"
        elif zielpos_y > unspos_y and not ist_mauer(unspos_x , unspos_y+1, data.get('wall')):
            move = "S"
        elif zielpos_y < unspos_y and not ist_mauer(unspos_x, unspos_y-1, data.get('wall')):
            move = "N"
        else:
            move = "WAIT"

        print(f"wir x:{unspos_x}, y:{unspos_y}; Ziel x: {zielpos_x}, y: {zielpos_y}", file=sys.stderr, flush=True)

        print(move, flush=True)

        erste_runde = False
