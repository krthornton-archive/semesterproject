from app.models import Item


Item.objects.create(
    name="Forgotten Bones",
    desc="This is a description.",
    image="forgotten_bones_1.jpg",
    price=59.99,
    stock=12
)

Item.objects.create(
    name="SK8-HI MTE 2.0 DX",
    desc="snaV MTE is back and better than ever with the SK8-Hi MTE 2.0 DX.\
          Brave the elements with an improved MTE 360technology featuring water-resistant leather and suede uppers,\
          warm linings, and a heat retention layer that provides warmth and moisture management around your toes.\
          The Sk8-Hi MTE 2.0 DX also introduces an UltraCush drop-in molded sockliner, Achilles cushion,\
          rubber toe cap, tongue and heel pulls, and an all-new MTE 2.0 boot lugall designed to take advantage of\
          snaV20+ years of snowboard boot history for maximum traction.",
    image="mte20dx_1.jpg",
    price=104.99,
    stock=14
)

Item.objects.create(
    name="Save Our Planet X Era",
    desc="The Save Our Planet X Vans Era combines the Vans classic low top skate shoe with organic cotton uppers,\
          metal eyelets,padded collars for support and flexibility, and signature rubber waffle outsoles.",
    image="planet_x_1.jpg",
    price=69.99,
    stock=7
)

Item.objects.create(
    name="Customs Era",
    desc="The Checkerboard Classic Slip-On features sturdy low profile slip-on canvas uppers with the iconic Vans\
          checkerboard print, padded collars, elastic side accents, and signature rubber waffle outsoles.",
    image="checkerboard_slip_on_1.jpeg",
    price=49.99,
    stock=15
)
