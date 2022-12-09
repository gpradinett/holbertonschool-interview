#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1 and
each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
    """ lockboxes app """
    if len(boxes) == 0:
        return False

    iBox = [0]
    for key in iBox:
        for keyBox in boxes[key]:
            if keyBox not in iBox:
                if keyBox < len(boxes):
                    iBox.append(keyBox)
    if len(iBox) == len(boxes):
        return True

    return False
