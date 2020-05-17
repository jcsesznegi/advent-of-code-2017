from firewall import Firewall

def test_severity():
    depths = [0, 1, 4, 6]
    ranges = [3, 2, 4, 4]
    firewall = Firewall(depths, ranges)
    firewall.run()
    assert firewall.totalSeverity == 24
