import subprocess
import os
thisdir = os.path.dirname(__file__)
thisdir = os.path.normpath(thisdir)

sqerdir = os.path.join(thisdir, '../')
sqerdir = os.path.normpath(sqerdir)

datadir = os.path.join(sqerdir, 'data')
datadir = os.path.normpath(datadir)

def test_count_reads():
    scriptpath = os.path.join(sqerdir, 'count-read-bp.py')
    datapath = os.path.join(datadir, 'test-reads.fa')
    print thisdir, sqerdir, scriptpath, datapath

    p = subprocess.Popen([scriptpath, datapath],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (out, err) = p.communicate()

    assert p.returncode == 0
    assert "8 bp total" in out, out

def test_count_reads_2():
    scriptpath = os.path.join(sqerdir, 'count-read-bp.py')
    datapath = os.path.join(datadir, 'test-reads.fq')
    print thisdir, sqerdir, scriptpath, datapath

    p = subprocess.Popen([scriptpath, datapath],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    (out, err) = p.communicate()

    assert p.returncode == 0
    assert "5755 bp total" in out, out
