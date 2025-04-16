def compute_scores(U, S, L, B, weights, threshold=0.5):
    w1, w2, w3, w4 = weights
    score_onboard = w1 * U
    score_edge = w1 * U + w2 * S + w3 * L + w4 * B
    score_cloud = w1 * U + w4 * B

    scores = {
        'onboard': round(score_onboard, 3),
        'edge': round(score_edge, 3),
        'cloud': round(score_cloud, 3)
    }

    best_tier = max(scores, key=scores.get)
    if scores[best_tier] >= threshold:
        return best_tier, scores[best_tier]
    return 'onboard', scores['onboard']