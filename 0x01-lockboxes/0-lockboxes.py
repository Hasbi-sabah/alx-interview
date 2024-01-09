#!/usr/bin/python3
""" module for the functions canUnlockAll and open_sesame"""


def canUnlockAll(boxes):
    """Check if it's possible to unlock all boxes in a given list of boxes"""
    opened = [0]
    open_sesame(boxes, boxes[0], 0, opened)
    if len(boxes) == len(opened):
        return True
    return False


def open_sesame(boxes, box, idx, opened):
    """Recursive helper function to explore the connections between boxes"""
    if idx not in opened:
        opened.append(idx)
    for key in box:
        if key not in opened:
            open_sesame(boxes, boxes[key], key, opened)
