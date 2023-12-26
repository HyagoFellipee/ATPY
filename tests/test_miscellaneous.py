import pytest
from src.miscellaneous import Miscellaneous


@pytest.fixture
def misc():
    return Miscellaneous()

spot_len = 8

def test_delta_t(misc):
    misc.delta_t = 0.000001
    assert misc.delta_t == "1.E-6".ljust(spot_len)

    misc.delta_t = 1
    assert misc.delta_t == "1".ljust(spot_len)

    misc.delta_t = 1E6
    assert misc.delta_t == "1.E6".ljust(spot_len)

    misc.delta_t = 0.5
    assert misc.delta_t == "5.E-1".ljust(spot_len)

    misc.delta_t = 200
    assert misc.delta_t == "2.E2".ljust(spot_len)

    misc.delta_t = 25 
    assert misc.delta_t == "2.5E1".ljust(spot_len)

    misc.delta_t = 0.956789
    assert misc.delta_t == "9.567E-1".ljust(spot_len)

    misc.delta_t = 2139021940284104
    assert misc.delta_t == "2.139E15"

    misc.delta_t = 0.00000000
    assert misc.delta_t == "0".ljust(spot_len)

    misc.delta_t = 0.000000000340932492395324
    assert misc.delta_t == "3.4E-10 "

    misc.delta_t = "0312321"
    assert misc.delta_t == "0312321".ljust(spot_len)

def test_t_max(misc):
    misc.t_max = 0.000001
    assert misc.t_max == "1.E-6".ljust(spot_len)

    misc.t_max = 1
    assert misc.t_max == "1".ljust(spot_len)

    misc.t_max = 1E6
    assert misc.t_max == "1.E6".ljust(spot_len)

    misc.t_max = 0.5
    assert misc.t_max == "5.E-1".ljust(spot_len)

    misc.t_max = 200
    assert misc.t_max == "2.E2".ljust(spot_len)

    misc.t_max = 25
    assert misc.t_max == "2.5E1".ljust(spot_len)

    misc.t_max = 0.956789
    assert misc.t_max == "9.567E-1".ljust(spot_len)

    misc.t_max = 2139021940284104
    assert misc.t_max == "2.139E15"

    misc.t_max = 0.00000000
    assert misc.t_max == "0".ljust(spot_len)

    misc.t_max = 0.000000000340932492395324
    assert misc.t_max == "3.4E-10 "

    misc.t_max = "0312321"
    assert misc.t_max == "0312321".ljust(spot_len)

def test_x_opt(misc):
    misc.x_opt = True
    assert misc.x_opt == "1       "

    misc.x_opt = False
    assert misc.x_opt == "0       "

    misc.x_opt = 1
    assert misc.x_opt == "1       "

    misc.x_opt = 0
    assert misc.x_opt == "0       "

    misc.x_opt = "0"
    assert misc.x_opt == "0       "

    misc.x_opt = "1"
    assert misc.x_opt == "1       "

    misc.x_opt = "hi"
    assert misc.x_opt == "hi".ljust(spot_len)

    misc.x_opt = 1232
    assert misc.x_opt == "1".ljust(spot_len)

def test_c_opt(misc):
    misc.c_opt = True
    assert misc.c_opt == "1       "

    misc.c_opt = False
    assert misc.c_opt == "0       "

    misc.c_opt = 1
    assert misc.c_opt == "1       "

    misc.c_opt = 0
    assert misc.c_opt == "0       "

    misc.c_opt = "0"
    assert misc.c_opt == "0       "

    misc.c_opt = "1"
    assert misc.c_opt == "1       "

    misc.c_opt = "hi"
    assert misc.c_opt == "hi".ljust(spot_len)

    misc.c_opt = 1232
    assert misc.c_opt == "1".ljust(spot_len)

def test_epslin(misc):
    misc.epslin = True
    assert misc.epslin == "1       "

    misc.epslin = False
    assert misc.epslin == "0       "

    misc.epslin = 1
    assert misc.epslin == "1       "

    misc.epslin = 0
    assert misc.epslin == "0       "

    misc.epslin = "0"
    assert misc.epslin == "0       "

    misc.epslin = "1"
    assert misc.epslin == "1       "

    misc.epslin = "hi"
    assert misc.epslin == "hi".ljust(spot_len)

    misc.epslin = 1232
    assert misc.epslin == "1".ljust(spot_len)
    
def test_tolmat(misc):
    misc.tolmat = True
    assert misc.tolmat == "1       "

    misc.tolmat = False
    assert misc.tolmat == "0       "

    misc.tolmat = 1
    assert misc.tolmat == "1       "

    misc.tolmat = 0
    assert misc.tolmat == "0       "

    misc.tolmat = "0"
    assert misc.tolmat == "0       "

    misc.tolmat = "1"
    assert misc.tolmat == "1       "

    misc.tolmat = "hi"
    assert misc.tolmat == "hi".ljust(spot_len)

    misc.tolmat = 1232
    assert misc.tolmat == "1".ljust(spot_len)

def test_tstart(misc):
    misc.tstart = 0.000001
    assert misc.tstart == "1.E-6".ljust(spot_len)

    misc.tstart = 1
    assert misc.tstart == "1".ljust(spot_len)

    misc.tstart = 1E6
    assert misc.tstart == "1.E6".ljust(spot_len)

    misc.tstart = 0.5
    assert misc.tstart == "5.E-1".ljust(spot_len)

    misc.tstart = 200
    assert misc.tstart == "2.E2".ljust(spot_len)

    misc.tstart = 25
    assert misc.tstart == "2.5E1".ljust(spot_len)

    misc.tstart = 0.956789
    assert misc.tstart == "9.567E-1".ljust(spot_len)

    misc.tstart = 2139021940284104
    assert misc.tstart == "2.139E15"

    misc.tstart = 0.00000000
    assert misc.tstart == "0".ljust(spot_len)

    misc.tstart = 0.000000000340932492395324
    assert misc.tstart == "3.4E-10 "

    misc.tstart = "0312321"
    assert misc.tstart == "0312321".ljust(spot_len)

def test_iout(misc):
    misc.iout = 0.000001
    assert misc.iout == "1.E-6".ljust(spot_len)

    misc.iout = 1
    assert misc.iout == "1".ljust(spot_len)

    misc.iout = 1E6
    assert misc.iout == "1.E6".ljust(spot_len)

    misc.iout = 0.5
    assert misc.iout == "5.E-1".ljust(spot_len)

    misc.iout = 200
    assert misc.iout == "2.E2".ljust(spot_len)

    misc.iout = 25
    assert misc.iout == "2.5E1".ljust(spot_len)

    misc.iout = 0.956789
    assert misc.iout == "9.567E-1".ljust(spot_len)

    misc.iout = 2139021940284104
    assert misc.iout == "2.139E15"

    misc.iout = 0.00000000
    assert misc.iout == "0".ljust(spot_len)

    misc.iout = 0.000000000340932492395324
    assert misc.iout == "3.4E-10 "

    misc.iout = "0312321"
    assert misc.iout == "0312321".ljust(spot_len)

def test_iplot(misc):
    misc.iplot = 0.000001
    assert misc.iplot == "1.E-6".ljust(spot_len)

    misc.iplot = 1
    assert misc.iplot == "1".ljust(spot_len)

    misc.iplot = 1E6
    assert misc.iplot == "1.E6".ljust(spot_len)

    misc.iplot = 0.5
    assert misc.iplot == "5.E-1".ljust(spot_len)

    misc.iplot = 200
    assert misc.iplot == "2.E2".ljust(spot_len)

    misc.iplot = 25
    assert misc.iplot == "2.5E1".ljust(spot_len)

    misc.iplot = 0.956789
    assert misc.iplot == "9.567E-1".ljust(spot_len)

    misc.iplot = 2139021940284104
    assert misc.iplot == "2.139E15"

    misc.iplot = 0.00000000
    assert misc.iplot == "0".ljust(spot_len)

    misc.iplot = 0.000000000340932492395324
    assert misc.iplot == "3.4E-10 "

    misc.iplot = "0312321"
    assert misc.iplot == "0312321".ljust(spot_len)
   
def test_idoubl(misc):
    misc.idoubl = True
    assert misc.idoubl == "1       "

    misc.idoubl = False
    assert misc.idoubl == "0       "

    misc.idoubl = 1
    assert misc.idoubl == "1       "

    misc.idoubl = 0
    assert misc.idoubl == "0       "

    misc.idoubl = "0"
    assert misc.idoubl == "0       "

    misc.idoubl = "1"
    assert misc.idoubl == "1       "

    misc.idoubl = "hi"
    assert misc.idoubl == "hi".ljust(spot_len)

    misc.idoubl = 1232
    assert misc.idoubl == "1".ljust(spot_len)

def test_kout(misc):
    misc.kout = False
    assert misc.kout == "0       "

    misc.kout = True
    assert misc.kout == "1       "

    misc.kout = 1
    assert misc.kout == "1       "

    misc.kout = 0
    assert misc.kout == "0       "

    misc.kout = "0"
    assert misc.kout == "0       "

    misc.kout = "1"
    assert misc.kout == "1       "

    misc.kout = "hi"
    assert misc.kout == "hi".ljust(spot_len)

    misc.kout = 1232
    assert misc.kout == "1".ljust(spot_len)

def test_maxout(misc):
    misc.maxout = True
    assert misc.maxout == "1       "

    misc.maxout = False
    assert misc.maxout == "0       "

    misc.maxout = 1
    assert misc.maxout == "1       "

    misc.maxout = 0
    assert misc.maxout == "0       "

    misc.maxout = "0"
    assert misc.maxout == "0       "

    misc.maxout = "1"
    assert misc.maxout == "1       "

    misc.maxout = "hi"
    assert misc.maxout == "hi".ljust(spot_len)

    misc.maxout = 1232
    assert misc.maxout == "1".ljust(spot_len)

def test_ipun(misc):
    misc.ipun = False
    assert misc.ipun == "0       "

    misc.ipun = True
    assert misc.ipun == "1       "

    misc.ipun = 1
    assert misc.ipun == "1       "

    misc.ipun = 0
    assert misc.ipun == "0       "

    misc.ipun = "0"
    assert misc.ipun == "0       "

    misc.ipun = "1"
    assert misc.ipun == "1       "

    misc.ipun = "hi"
    assert misc.ipun == "hi".ljust(spot_len)

    misc.ipun = 1232
    assert misc.ipun == "1".ljust(spot_len)

def test_memsav(misc):
    misc.memsav = False
    assert misc.memsav == "0       "

    misc.memsav = True
    assert misc.memsav == "1       "

    misc.memsav = 1
    assert misc.memsav == "1       "

    misc.memsav = 0
    assert misc.memsav == "0       "

    misc.memsav = "0"
    assert misc.memsav == "0       "

    misc.memsav = "1"
    assert misc.memsav == "1       "

    misc.memsav = "hi"
    assert misc.memsav == "hi".ljust(spot_len)

    misc.memsav = 1232
    assert misc.memsav == "1".ljust(spot_len)

def test_icat(misc):
    misc.icat = False
    assert misc.icat == "0       "

    misc.icat = True
    assert misc.icat == "1       "

    misc.icat = 1
    assert misc.icat == "1       "

    misc.icat = 0
    assert misc.icat == "0       "

    misc.icat = "0"
    assert misc.icat == "0       "

    misc.icat = "1"
    assert misc.icat == "1       "

    misc.icat = "hi"
    assert misc.icat == "hi".ljust(spot_len)

    misc.icat = 1232
    assert misc.icat == "1".ljust(spot_len)

def test_nenerg(misc):
    misc.nenerg = False
    assert misc.nenerg == "0       "

    misc.nenerg = True
    assert misc.nenerg == "1       "

    misc.nenerg = 1
    assert misc.nenerg == "1       "

    misc.nenerg = 0
    assert misc.nenerg == "0       "

    misc.nenerg = "0"
    assert misc.nenerg == "0       "

    misc.nenerg = "1"
    assert misc.nenerg == "1       "

    misc.nenerg = "hi"
    assert misc.nenerg == "hi".ljust(spot_len)

    misc.nenerg = 1232
    assert misc.nenerg == "1".ljust(spot_len)

def test_iprsup(misc):
    misc.iprsup = False
    assert misc.iprsup == "0       "

    misc.iprsup = True
    assert misc.iprsup == "1       "

    misc.iprsup = 1
    assert misc.iprsup == "1       "

    misc.iprsup = 0
    assert misc.iprsup == "0       "

    misc.iprsup = "0"
    assert misc.iprsup == "0       "

    misc.iprsup = "1"
    assert misc.iprsup == "1       "

    misc.iprsup = "hi"
    assert misc.iprsup == "hi".ljust(spot_len)

    misc.iprsup = 1232
    assert misc.iprsup == "1".ljust(spot_len)
