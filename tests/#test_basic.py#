import sqer

class FakeRecord(object):
    def __init__(self, sequence, name=''):
        self.sequence = sequence
        self.name = name

def test_sum_bp():
    assert sqer.sum_bp(FakeRecord('ATGC')) == 4

def test_sum_bp_records():
    rl = [ FakeRecord("A"), FakeRecord("G") ]
    assert sqer.sum_bp_records(rl) == 2
