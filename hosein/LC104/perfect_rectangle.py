class Solution:
    def isRectangleCover(self, rectangles):
        x1 = min(r[0] for r in rectangles)
        y1 = min(r[1] for r in rectangles)
        x2 = max(r[2] for r in rectangles)
        y2 = max(r[3] for r in rectangles)
        area = 0
        corners = set()
        for x1_, y1_, x2_, y2_ in rectangles:
            area += (x2_ - x1_) * (y2_ - y1_)
            for x, y in ((x1_, y1_), (x1_, y2_), (x2_, y1_), (x2_, y2_)):
                if (x, y) in corners:
                    corners.remove((x, y))
                else:
                    corners.add((x, y))
        if area != (x2 - x1) * (y2 - y1):
            return False
        if corners != {(x1, y1), (x1, y2), (x2, y1), (x2, y2)}:
            return False
        return True