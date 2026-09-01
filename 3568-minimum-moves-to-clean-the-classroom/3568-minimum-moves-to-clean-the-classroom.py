from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        """
        :type classroom: List[str]
        :type energy: int
        :rtype: int
        """
        m, n = len(classroom), len(classroom[0])
        start_pos = -1
        litter_mask_map = {}
        litter_count = 0

        # Pre-process grid and map litter positions to bits
        for r in range(m):
            for c in range(n):
                cell = classroom[r][c]
                if cell == 'S':
                    start_pos = r * n + c
                elif cell == 'L':
                    litter_mask_map[r * n + c] = 1 << litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1
        if full_mask == 0:
            return 0

        num_cells = m * n
        num_masks = 1 << litter_count

        # Flat array for max remaining energy lookup: best_energy[pos][mask]
        best_energy = [[-1] * num_masks for _ in range(num_cells)]
        
        # BFS Queue holds packed elements or tuples: (pos, mask, e)
        queue = deque([(start_pos, 0, energy)])
        best_energy[start_pos][0] = energy

        steps = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            for _ in range(len(queue)):
                pos, mask, e = queue.popleft()

                if mask == full_mask:
                    return steps

                r, c = divmod(pos, n)

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < m and 0 <= nc < n:
                        cell = classroom[nr][nc]
                        if cell == 'X':
                            continue

                        ne = e - 1
                        if ne < 0:
                            continue

                        npos = nr * n + nc
                        nmask = mask

                        # Collect litter if step onto 'L'
                        if cell == 'L' and npos in litter_mask_map:
                            nmask |= litter_mask_map[npos]

                        # Restore max capacity at reset points 'R'
                        if cell == 'R':
                            ne = energy

                        # Strict state-energy pruning
                        if ne > best_energy[npos][nmask]:
                            best_energy[npos][nmask] = ne
                            queue.append((npos, nmask, ne))

            steps += 1

        return -1