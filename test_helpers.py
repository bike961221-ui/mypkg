from mypkg.helpers import calculate_stats

def test_calculate_stats():
    data = [1, 2, 3, 4, 5]
    result = calculate_stats(data)

    assert result["mean"] == 3
    assert result["min"] == 1
    assert result["max"] == 5