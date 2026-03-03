def calculate_stats(data):
    return {
        "mean": sum(data) / len(data),
        "min": min(data),
        "max": max(data),
    }