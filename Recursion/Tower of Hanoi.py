# ─────────────────────────────────────────────
# 5. Tower of Hanoi
# Move n disks from source peg to destination using an auxiliary peg.
# Rule: Never place a larger disk on a smaller one.
#
# Approach: Recursive insight —
#           Step 1: Move top (n-1) disks from src → aux
#           Step 2: Move bottom (largest) disk from src → dst
#           Step 3: Move (n-1) disks from aux → dst
# Time : O(2^n)  — minimum moves required is 2^n - 1
# Space: O(n)    — call stack depth
# ─────────────────────────────────────────────
def tower_of_hanoi(n, source='A', destination='C', auxiliary='B'):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
 
    tower_of_hanoi(n - 1, source, auxiliary, destination)   # step 1
    print(f"Move disk {n} from {source} → {destination}")   # step 2
    tower_of_hanoi(n - 1, auxiliary, destination, source)   # step 3
 
 
# ---- Test ----
tower_of_hanoi(3)