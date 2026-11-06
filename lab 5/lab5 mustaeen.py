import math
def minimax(depth, index, max_turn, scores, target_depth, leaves):
    if depth == target_depth:
        leaves[0] += 1
        return scores[index]
    if max_turn:
        return max(
            minimax(depth + 1, index * 2, False, scores, target_depth, leaves),
            minimax(depth + 1, index * 2 + 1, False, scores, target_depth, leaves),
        )
    return min(
        minimax(depth + 1, index * 2, True, scores, target_depth, leaves),
        minimax(depth + 1, index * 2 + 1, True, scores, target_depth, leaves),
    )
def alphabeta(depth, index, max_turn, scores, target_depth, alpha, beta, leaves):
    if depth == target_depth:
        leaves[0] += 1
        return scores[index]
    if max_turn:
        value = float("-inf")
        for i in range(2):
            value = max(
                value,
                alphabeta(depth + 1, index * 2 + i, False, scores, target_depth, alpha, beta, leaves),
            )
            alpha = max(alpha, value)
            if alpha >= beta:
                break
        return value
    value = float("inf")
    for i in range(2):
        value = min(
            value,
            alphabeta(depth + 1, index * 2 + i, True, scores, target_depth, alpha, beta, leaves),
        )
        beta = min(beta, value)
        if alpha >= beta:
            break
    return value


scores1 = [3, 5, 2, 9, 0, 7]
depth1 = math.ceil(math.log2(len(scores1)))
scores1 += [0] * (2 ** depth1 - len(scores1))
leaves = [0]
print("Tree 1 minimax:", minimax(0, 0, True, scores1, depth1, leaves), "leaves:", leaves[0])

scores2 = [3, 5, 2, 9, 3, 5, 2, 9]
depth2 = int(math.log2(len(scores2)))
leaves = [0]
print("Tree 2 minimax:", minimax(0, 0, True, scores2, depth2, leaves), "leaves:", leaves[0])
leaves = [0]
print("Tree 2 alphabeta:", alphabeta(0, 0, True, scores2, depth2, float("-inf"), float("inf"), leaves), "leaves:", leaves[0])

scores3 = [9, 2, 5, 3, 9, 2, 5, 3]
leaves = [0]
print("Tree 2 reordered minimax:", minimax(0, 0, True, scores3, depth2, leaves), "leaves:", leaves[0])
leaves = [0]
print("Tree 2 reordered alphabeta:", alphabeta(0, 0, True, scores3, depth2, float("-inf"), float("inf"), leaves), "leaves:", leaves[0])

scores4 = [7]
leaves = [0]
print("Edge case minimax:", minimax(0, 0, True, scores4, 0, leaves), "leaves:", leaves[0])
leaves = [0]
print("Edge case alphabeta:", alphabeta(0, 0, True, scores4, 0, float("-inf"), float("inf"), leaves), "leaves:", leaves[0])
