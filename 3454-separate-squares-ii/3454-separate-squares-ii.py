from bisect import bisect_left

class SegmentTree:
    def __init__(self, coords):
        self.n = len(coords) - 1 
        self.coords = coords
        self.len = [0] * (4 * self.n)
        self.cnt = [0] * (4 * self.n)
    
    def _update(self, node, l, r, ql, qr, val):
        if ql >= r or qr <= l:
            return
        if ql <= l and r <= qr:
            self.cnt[node] += val
        else:
            mid = (l + r) // 2
            self._update(node * 2, l, mid, ql, qr, val)
            self._update(node * 2 + 1, mid, r, ql, qr, val)
        
        if self.cnt[node] > 0:
            self.len[node] = self.coords[r] - self.coords[l]
        else:
            if l + 1 == r:
                self.len[node] = 0
            else:
                self.len[node] = self.len[node * 2] + self.len[node * 2 + 1]
    
    def update(self, x1, x2, val):
        ql = bisect_left(self.coords, x1)
        qr = bisect_left(self.coords, x2)
        if ql < qr:
            self._update(1, 0, self.n, ql, qr, val)
    
    def total_length(self):
        return self.len[1]

class Solution(object):
    def separateSquares(self, squares):


        def union_area_2d(squares):

            events = []
            unique_x = set()
            for x, y, l in squares:
                unique_x.add(x)
                unique_x.add(x + l)
                events.append((y, 1, x, x + l)) 
                events.append((y + l, -1, x, x + l))  
            unique_x = sorted(unique_x)
            
            events.sort()
            segtree = SegmentTree(unique_x)
            
            area = 0
            prev_y = events[0][0] if events else 0
            i = 0
            while i < len(events):
                y = events[i][0]
                if y > prev_y:
                    width = segtree.total_length()
                    height = y - prev_y
                    area += width * height
                
                while i < len(events) and events[i][0] == y:
                    _, typ, x1, x2 = events[i]
                    segtree.update(x1, x2, typ)
                    i += 1
                
                prev_y = y
            
            return area
        
        total_union = union_area_2d(squares)
        if total_union == 0:
            return 0.0
            
        target = total_union / 2.0

        y_events = []
        for x, y, l in squares:
            y_events.append((y, 1, x, x + l)) 
            y_events.append((y + l, -1, x, x + l))  
        y_events.sort()
        
        if not y_events:
            return 0.0
            

        unique_x = set()
        for _, _, x1, x2 in y_events:
            unique_x.add(x1)
            unique_x.add(x2)
        unique_x = sorted(unique_x)
        

        segtree = SegmentTree(unique_x)
        

        area_above = total_union
        prev_h = float('-inf')
        
        i = 0
        while i < len(y_events):
            h = y_events[i][0]
            
 
            union_x_length = segtree.total_length()
            
            if prev_h != float('-inf'):

                area_at_h_start = area_above
                area_at_h_end = area_above - union_x_length * (h - prev_h)
                

                if union_x_length > 0:
                    if area_at_h_start >= target >= area_at_h_end:

                        dh = (area_at_h_start - target) / float(union_x_length)
                        return prev_h + dh
                else:

                    if area_at_h_start == target:
                        return prev_h
            

            area_above = area_above - union_x_length * (h - prev_h) if prev_h != float('-inf') else area_above
            

            while i < len(y_events) and y_events[i][0] == h:
                _, typ, x1, x2 = y_events[i]
                segtree.update(x1, x2, typ)
                i += 1
            
            prev_h = h
        
        if abs(area_above - target) < 1e-9:
            return prev_h
        
        min_y = min(y for _, y, _ in squares)
        max_y = max(y + l for _, y, l in squares)
        
        def area_above_h(h_val):

            above_squares = []
            for x, y, l in squares:
                if h_val < y + l: 
                    y_start = max(y, h_val)
                    above_squares.append((x, x + l, y_start, y + l))
            
            if not above_squares:
                return 0.0
            
            events = []
            unique_x = set()
            for x1, x2, y1, y2 in above_squares:
                unique_x.add(x1)
                unique_x.add(x2)
                events.append((y1, 1, x1, x2))
                events.append((y2, -1, x1, x2))
            
            if not events:
                return 0.0
                
            unique_x = sorted(unique_x)
            events.sort()
            segtree_temp = SegmentTree(unique_x)
            
            area = 0
            prev_y = events[0][0]
            i = 0
            while i < len(events):
                y = events[i][0]
                if y > prev_y:
                    width = segtree_temp.total_length()
                    height = y - prev_y
                    area += width * height
                
                while i < len(events) and events[i][0] == y:
                    _, typ, x1, x2 = events[i]
                    segtree_temp.update(x1, x2, typ)
                    i += 1
                
                prev_y = y
            
            return area
        
        left, right = min_y, max_y
        for _ in range(60):  
            mid = (left + right) / 2.0
            area_mid = area_above_h(mid)
            if area_mid > target:
                left = mid
            else:
                right = mid
        
        return (left + right) / 2.0