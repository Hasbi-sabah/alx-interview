#!/usr/bin/python3
def canUnlockAll(boxes):
    opened = [0]
    open_sesame(boxes, boxes[0], 0, opened)
    if len(boxes) == len(opened):
        return True
    return False


def open_sesame(boxes, box, idx, opened):
    if idx not in opened:
        opened.append(idx)
    for key in box:
        if key not in opened:
            open_sesame(boxes, boxes[key], key, opened)
