#!/usr/bin/env python3

def score_analytics():
    import sys

    print("=== Player Score Analytics ===")
    try:
        if len(sys.argv) < 2:
            raise ValueError("No scores provided. Usage: python3 ft_score_analytics.py <score_1> <score_2>...")
        scores = []
        for arg in sys.argv[1:]:
            try:
                scores.append(int(arg))
            except ValueError:
                raise ValueError(f"Invalid score: {arg} is not an integer.")
        print(f"Scores processed: {str(scores)}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    score_analytics()