from firewall import Firewall

def test_severity():
    depths = [0, 1, 4, 6]
    ranges = [3, 2, 4, 4]
    firewall = Firewall(depths, ranges)
    firewall.run()
    assert firewall.totalSeverity == 24

def test_severity_with_delay_3():
    depths = [0, 1, 4, 6]
    ranges = [3, 2, 4, 4]
    firewall = Firewall(depths, ranges, 3)
    firewall.run()
    assert firewall.totalSeverity > 0

def test_severity_with_delay_7():
    depths = [0, 1, 4, 6]
    ranges = [3, 2, 4, 4]
    firewall = Firewall(depths, ranges, 7)
    firewall.run()
    assert firewall.totalSeverity > 0

def test_severity_with_delay_10():
    depths = [0, 1, 4, 6]
    ranges = [3, 2, 4, 4]
    firewall = Firewall(depths, ranges, 10)
    firewall.run()
    assert firewall.totalSeverity == 0
