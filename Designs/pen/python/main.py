from Pen import *
from strategies.writeStrategies import *
from Refil import *
from Enums import *

# write behaviours
# let's keep one only for now.
smooth_writeBehaviour = SmoothWriteBehaviour()
fountain_writeBehaviour = FountainWriteBehaviour()
marker_writeBehaviour = MarkerWriteBehaviour()

# Initialize inks
gel_ink = Ink(Colour.BLUE, InkType.GEL, 1)
fountain_ink = Ink(Colour.BLACK, InkType.FOUNTAIN, 0.5)
ball_ink = Ink(Colour.RED, InkType.NON_GEL, 3)
marker_ink = Ink(Colour.GREEN, InkType.FLUID, 2)

# Nip's
normal_nip = Nip(2, NipType.NORMAL)
ball_nip = Nip(2, NipType.BALL)
fountain_nip = Nip(2, NipType.FOUNTAIN)
sponge_nip = Nip(2, NipType.SPONGE)

# Refils
gelpen_refil = GelPenRefil(gel_ink, RefilType.GEL, normal_nip, 25)
ballpen_refil = BallPenRefil(ball_ink, RefilType.BALL, ball_nip, 14)
marker_refil = MarkerRefil(marker_ink, RefilType.MARKER, sponge_nip, 45)

gelPen = (
    PenFactory.createGelPen().
    setCanChangeRefil(True).
    setRefil(gelpen_refil).
    setWriteBehaviour(smooth_writeBehaviour).
    set_name("Butterflow").
    set_company("cello").
    set_price(10).
    build()
)

ballPen = (
    PenFactory.createBallPen().
    setCanChangeRefil(True).
    setRefil(ballpen_refil).
    setWriteBehaviour(smooth_writeBehaviour).
    set_name("Reynolds").
    set_company("Reynolds").
    set_price(6).
    build()
)

marker = (
    PenFactory.createMarker().
    setCanChangeRefil(True).
    setRefil(marker_refil).
    setWriteBehaviour(marker_writeBehaviour).
    set_name("Nataraj").
    set_company("marker").
    set_price(40).
    build()
)

fountain_pen = (
    PenFactory.createFountainPen().
    setInk(fountain_ink).
    setWriteBehaviour(fountain_writeBehaviour).
    set_name("Ultima").
    set_company("Faber").
    set_price(300).
    build()
)

print(gelPen.__dict__)
print(ballPen.__dict__)
print(fountain_pen.__dict__)
print(marker.__dict__)

gelPen.write()
ballPen.write()
fountain_pen.write()
marker.write()
