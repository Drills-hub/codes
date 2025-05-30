import sys
input = sys.stdin.readline

def find_meeting_room_sizes(W, P, partition_positions):
    positions = [0] + partition_positions + [W]
    possible_sizes = set()
    for i in range(len(positions)):
        for j in range(i+1, len(positions)):
            possible_sizes.add(positions[j] - positions[i])
    result = sorted(possible_sizes)
    return result

W, P = map(int, input().split())
partition_positions = list(map(int, input().split()))
sizes = find_meeting_room_sizes(W, P, partition_positions)

print(' '.join(map(str, sizes)))