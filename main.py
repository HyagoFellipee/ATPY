import card as crd 

card = crd.ATPCard() 
dc = crd.DCSource()
dc.line = "11XX0001 0      1.E4                                               -1.      1.E3"
card.source.add_source(dc)
card.write_to_file("test.txt")