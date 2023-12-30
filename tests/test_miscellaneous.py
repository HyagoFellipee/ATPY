import pytest
from src.miscellaneous import Miscellaneous


@pytest.fixture
def misc():
    return Miscellaneous()

spot_len = 8

def test_delta_t(misc):
    misc.delta_t = 0.000001
    right_delta_t = "1.E-6".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 1
    right_delta_t = "1".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 1E6
    right_delta_t = "1.E6".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 0.5
    right_delta_t = "5.E-1".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 200
    right_delta_t = "2.E2".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 25 
    right_delta_t = "2.5E1".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 0.956789
    right_delta_t = "9.567E-1".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 2139021940284104
    right_delta_t = "2.139E15"
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 0.00000000
    right_delta_t = "0".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = 0.000000000340932492395324
    right_delta_t = "3.4E-10".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

    misc.delta_t = "0312321"
    right_delta_t = "0312321".rjust(spot_len)
    assert misc.delta_t == right_delta_t
    assert misc.first_line == right_delta_t + misc.first_line[8:]

def test_t_max(misc):
    misc.t_max = 0.000001
    right_t_max = "1.E-6".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 1
    right_t_max = "1".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 1E6
    right_t_max = "1.E6".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 0.5
    right_t_max = "5.E-1".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 200
    right_t_max = "2.E2".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 25
    right_t_max = "2.5E1".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 0.956789
    right_t_max = "9.567E-1".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max + misc.first_line[16:]

    misc.t_max = 2139021940284104
    right_t_max = "2.139E15"
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max.rjust(spot_len) + misc.first_line[16:]

    misc.t_max = 0.00000000
    right_t_max = "0".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max.rjust(spot_len) + misc.first_line[16:]

    misc.t_max = 0.000000000340932492395324
    right_t_max = "3.4E-10".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max.rjust(spot_len) + misc.first_line[16:]

    misc.t_max = "0312321"
    right_t_max = "0312321".rjust(spot_len)
    assert misc.t_max == right_t_max
    assert misc.first_line == misc.first_line[0:8] + right_t_max.rjust(spot_len) + misc.first_line[16:]

def test_x_opt(misc):
    misc.x_opt = True
    right_x_opt = "1".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = False
    right_x_opt = "0".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = 1
    right_x_opt = "1".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = 0
    right_x_opt = "0".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = "0"
    right_x_opt = "0".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = "1"
    right_x_opt = "1".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = "hi"
    right_x_opt = "hi".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = 1232
    right_x_opt = "1".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]

    misc.x_opt = "  "
    right_x_opt = " ".rjust(spot_len)
    assert misc.x_opt == right_x_opt
    assert misc.first_line == misc.first_line[0:16] + right_x_opt + misc.first_line[24:]


def test_c_opt(misc):
    misc.c_opt = True
    right_c_opt = "1".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = False
    right_c_opt = "0".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = 1
    right_c_opt = "1".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = 0
    right_c_opt = "0".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = "0"
    right_c_opt = "0".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = "1"
    right_c_opt = "1".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = "hi"
    right_c_opt = "hi".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = 1232
    right_c_opt = "1".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]

    misc.c_opt = "  "
    right_c_opt = " ".rjust(spot_len)
    assert misc.c_opt == right_c_opt
    assert misc.first_line == misc.first_line[0:24] + right_c_opt + misc.first_line[32:]


def test_epslin(misc):
    misc.epslin = True
    right_epslin = "1".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = False
    right_epslin = "0".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = 1
    right_epslin = "1".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = 0
    right_epslin = "0".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = "0"
    right_epslin = "0".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = "1"
    right_epslin = "1".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = "hi"
    right_epslin = "hi".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = 1232
    right_epslin = "1".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]

    misc.epslin = "  "
    right_epslin = " ".rjust(spot_len)
    assert misc.epslin == right_epslin
    assert misc.first_line == misc.first_line[0:32] + right_epslin + misc.first_line[40:]


def test_tolmat(misc):
    misc.tolmat = True
    right_tolmat = "1".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = False
    right_tolmat = "0".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = 1
    right_tolmat = "1".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = 0
    right_tolmat = "0".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = "0"
    right_tolmat = "0".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = "1"
    right_tolmat = "1".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = "hi"
    right_tolmat = "hi".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = 1232
    right_tolmat = "1".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]

    misc.tolmat = "  "
    right_tolmat = " ".rjust(spot_len)
    assert misc.tolmat == right_tolmat
    assert misc.first_line == misc.first_line[0:40] + right_tolmat + misc.first_line[48:]


def test_tstart(misc):
    misc.tstart = 0.000001
    right_tstart = "1.E-6".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 1
    right_tstart = "1".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 1E6
    right_tstart = "1.E6".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 0.5
    right_tstart = "5.E-1".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 200
    right_tstart = "2.E2".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 25
    right_tstart = "2.5E1".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 0.956789
    right_tstart = "9.567E-1".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 2139021940284104
    right_tstart = "2.139E15"
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart.rjust(spot_len) + misc.first_line[56:]

    misc.tstart = 0.00000000
    right_tstart = "0".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = 0.000000000340932492395324
    right_tstart = "3.4E-10".rjust(spot_len).rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

    misc.tstart = "0312321"
    right_tstart = "0312321".rjust(spot_len)
    assert misc.tstart == right_tstart
    assert misc.first_line == misc.first_line[0:48] + right_tstart + misc.first_line[56:]

def test_iout(misc):
    misc.iout = 0.000001
    right_iout = "1.E-6".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 1
    right_iout = "1".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]


    misc.iout = 0.5
    right_iout = "5.E-1".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]


    misc.iout = 200
    right_iout = "2.E2".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 25
    right_iout = "2.5E1".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 0.956789
    right_iout = "9.567E-1".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 2139021940284104
    right_iout = "2.139E15"
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 0.00000000
    right_iout = "0".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = 0.000000000340932492395324
    right_iout = "3.4E-10".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

    misc.iout = "0312321"
    right_iout = "0312321".rjust(spot_len)
    assert misc.iout == right_iout
    assert misc.second_line == right_iout + misc.second_line[8:]

def test_iplot(misc):
    misc.iplot = 0.000001
    right_iplot = "1.E-6".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 1
    right_iplot = "1".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 1E6
    right_iplot = "1.E6".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 0.5
    right_iplot = "5.E-1".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 200
    right_iplot = "2.E2".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 25
    right_iplot = "2.5E1".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 0.956789
    right_iplot = "9.567E-1".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 2139021940284104
    right_iplot = "2.139E15"
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 0.00000000
    right_iplot = "0".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = 0.000000000340932492395324
    right_iplot = "3.4E-10".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]

    misc.iplot = "0312321"
    right_iplot = "0312321".rjust(spot_len)
    assert misc.iplot == right_iplot
    assert misc.second_line == misc.second_line[0:8] + right_iplot + misc.second_line[16:]   

def test_idoubl(misc):
    misc.idoubl = True
    right_idoubl = "1".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = False
    right_idoubl = "0".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = 1
    right_idoubl = "1".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = 0
    right_idoubl = "0".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = "0"
    right_idoubl = "0".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = "1"
    right_idoubl = "1".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = "hi"
    right_idoubl = "hi".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = 1232
    right_idoubl = "1".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]

    misc.idoubl = "  "
    right_idoubl = " ".rjust(spot_len)
    assert misc.idoubl == right_idoubl
    assert misc.second_line == misc.second_line[0:16] + right_idoubl + misc.second_line[24:]


def test_kout(misc):
    misc.kout = True
    right_kout = "1".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = False
    right_kout = "0".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = 1
    right_kout = "1".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = 0
    right_kout = "0".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = "0"
    right_kout = "0".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = "1"
    right_kout = "1".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = "hi"
    right_kout = "hi".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = 1232
    right_kout = "1".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]

    misc.kout = "  "
    right_kout = " ".rjust(spot_len)
    assert misc.kout == right_kout
    assert misc.second_line == misc.second_line[0:24] + right_kout + misc.second_line[32:]


def test_maxout(misc):
    misc.maxout = True
    right_maxout = "1".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = False
    right_maxout = "0".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = 1
    right_maxout = "1".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = 0
    right_maxout = "0".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = "0"
    right_maxout = "0".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = "1"
    right_maxout = "1".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = "hi"
    right_maxout = "hi".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]

    misc.maxout = 1232
    right_maxout = "1".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]
    
    misc.maxout = "  "
    right_maxout = " ".rjust(spot_len)
    assert misc.maxout == right_maxout
    assert misc.second_line == misc.second_line[0:32] + right_maxout + misc.second_line[40:]


def test_ipun(misc):
    misc.ipun = True
    right_ipun = "1".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = False
    right_ipun = "0".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = 1
    right_ipun = "1".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = 0
    right_ipun = "0".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = "0"
    right_ipun = "0".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = "1"
    right_ipun = "1".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = "hi"
    right_ipun = "hi".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = 1232
    right_ipun = "1".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]

    misc.ipun = "  "
    right_ipun = " ".rjust(spot_len)
    assert misc.ipun == right_ipun
    assert misc.second_line == misc.second_line[0:40] + right_ipun + misc.second_line[48:]


def test_memsav(misc):
    misc.memsav = True
    right_memsav = "1".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = False
    right_memsav = "0".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = 1
    right_memsav = "1".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = 0
    right_memsav = "0".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = "0"
    right_memsav = "0".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = "1"
    right_memsav = "1".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = "hi"
    right_memsav = "hi".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = 1232
    right_memsav = "1".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]

    misc.memsav = "  "
    right_memsav = " ".rjust(spot_len)
    assert misc.memsav == right_memsav
    assert misc.second_line == misc.second_line[0:48] + right_memsav + misc.second_line[56:]


def test_icat(misc):
    misc.icat = True
    right_icat = "1".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = False
    right_icat = "0".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = 1
    right_icat = "1".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = 0
    right_icat = "0".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = "0"
    right_icat = "0".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = "1"
    right_icat = "1".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = "hi"
    right_icat = "hi".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = 1232
    right_icat = "1".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]

    misc.icat = "  "
    right_icat = " ".rjust(spot_len)
    assert misc.icat == right_icat
    assert misc.second_line == misc.second_line[0:56] + right_icat + misc.second_line[64:]


def test_nenerg(misc):
    misc.nenerg = True 
    right_nenerg = "1".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = False
    right_nenerg = "0".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = 1
    right_nenerg = "1".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = 0
    right_nenerg = "0".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = "0"
    right_nenerg = "0".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = "1"
    right_nenerg = "1".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = "hi"
    right_nenerg = "hi".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = 1232
    right_nenerg = "1".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]

    misc.nenerg = "  "
    right_nenerg = " ".rjust(spot_len)
    assert misc.nenerg == right_nenerg
    assert misc.second_line == misc.second_line[0:64] + right_nenerg + misc.second_line[72:]


def test_iprsup(misc):
    misc.iprsup = True
    right_iprsup = "1".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = False
    right_iprsup = "0".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = 1
    right_iprsup = "1".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = 0
    right_iprsup = "0".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = "0"
    right_iprsup = "0".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = "1"
    right_iprsup = "1".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = "hi"
    right_iprsup = "hi".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = 1232
    right_iprsup = "1".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]

    misc.iprsup = "  "
    right_iprsup = " ".rjust(spot_len)
    assert misc.iprsup == right_iprsup
    assert misc.second_line == misc.second_line[0:72] + right_iprsup + misc.second_line[80:]


def test_first_line(misc): 

    line_len = 56

    misc.first_line = " ".ljust(line_len)
    assert misc.first_line == " ".ljust(line_len)
    assert misc.delta_t == " ".rjust(spot_len)
    assert misc.t_max == " ".rjust(spot_len)
    assert misc.x_opt == " ".rjust(spot_len)
    assert misc.c_opt == " ".rjust(spot_len)
    assert misc.epslin == " ".rjust(spot_len)
    assert misc.tolmat == " ".rjust(spot_len)
    assert misc.tstart == " ".rjust(spot_len)

    misc.first_line = "1" * line_len
    assert misc.first_line == "1" * line_len
    assert misc.delta_t == "1" * spot_len
    assert misc.t_max == "1" * spot_len
    assert misc.x_opt == "1" * spot_len
    assert misc.c_opt == "1" * spot_len
    assert misc.epslin == "1" * spot_len
    assert misc.tolmat == "1" * spot_len
    assert misc.tstart == "1" * spot_len

    misc.first_line = "   1.E-6    .001                                 ".ljust(line_len)
    assert misc.first_line == "   1.E-6    .001                                 ".ljust(line_len)
    assert misc.delta_t == "1.E-6".rjust(spot_len)
    assert misc.t_max == ".001".rjust(spot_len)
    assert misc.x_opt == " ".rjust(spot_len)
    assert misc.c_opt == " ".rjust(spot_len)
    assert misc.epslin == " ".rjust(spot_len)
    assert misc.tolmat == " ".rjust(spot_len)
    assert misc.tstart == " ".rjust(spot_len)

def test_second_line(misc): 

    line_len = 80

    misc.second_line = " ".ljust(line_len)
    assert misc.second_line == " ".ljust(line_len)
    assert misc.iout == " ".rjust(spot_len)
    assert misc.iplot == " ".rjust(spot_len)
    assert misc.idoubl == " ".rjust(spot_len)
    assert misc.kout == " ".rjust(spot_len)
    assert misc.maxout == " ".rjust(spot_len)
    assert misc.ipun == " ".rjust(spot_len)
    assert misc.memsav == " ".rjust(spot_len)
    assert misc.icat == " ".rjust(spot_len)
    assert misc.nenerg == " ".rjust(spot_len)
    assert misc.iprsup == " ".rjust(spot_len)

    misc.second_line = "1" * line_len 
    assert misc.second_line == "1" * line_len
    assert misc.iout == "1" * spot_len
    assert misc.iplot == "1" * spot_len
    assert misc.idoubl == "1" * spot_len
    assert misc.kout == "1" * spot_len
    assert misc.maxout == "1" * spot_len
    assert misc.ipun == "1" * spot_len
    assert misc.memsav == "1" * spot_len
    assert misc.icat == "1" * spot_len
    assert misc.nenerg == "1" * spot_len
    assert misc.iprsup == "1" * spot_len


    misc.second_line = "     500       1       1       1       1       0       0       1       0".ljust(line_len)
    assert misc.second_line == "     500       1       1       1       1       0       0       1       0".ljust(line_len)
    assert misc.iout == "500".rjust(spot_len)
    assert misc.iplot == "1".rjust(spot_len)
    assert misc.idoubl == "1".rjust(spot_len)
    assert misc.kout == "1".rjust(spot_len)
    assert misc.maxout == "1".rjust(spot_len)
    assert misc.ipun == "0".rjust(spot_len)
    assert misc.memsav == "0".rjust(spot_len)
    assert misc.icat == "1".rjust(spot_len)
    assert misc.nenerg == "0".rjust(spot_len)
    assert misc.iprsup == " ".rjust(spot_len)

