from app.models import Item


Item.objects.create(
    name="Forgotten Bones",
    desc="The Forgotten Bones Classic Slip-On features sturdy low profile canvas uppers with an allover print,\
          padded collars, elastic side accents, and signature rubber waffle outsoles.",
    image="forgotten_bones_1.jpg",
    price=59.99,
    stock=12
)

Item.objects.create(
    name="SK8-HI MTE 2.0 DX",
    desc="snaV MTE is back and better than ever with the SK8-Hi MTE 2.0 DX.\
          Brave the elements with an improved MTE 360technology featuring water-resistant leather and suede uppers,\
          warm linings, and a heat retention layer that provides warmth and moisture management around your toes.",
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

Item.objects.create(
    name="Anaheim Factory SID DX",
    desc="New to the Anaheim Factory pack, the SID DX features high-gloss, heritage-inspired color palettes, our\
          iconic flying-V logo, and cotton velvet uppers for a unique look, feel, and construction.",
    image="anaheim_factory_1.jpg",
    price=84.99,
    stock=69,
)

Item.objects.create(
    name="SK8-HI 46 MTE DX",
    desc=" Deluxe weather-resistant suede and leather uppers, warm linings, and a heat retention layer between\
    sockliner and outsole keep feet warm and dry while the newly-constructed vulcanized lug outsole takes advantage\
    of 20 years of snow boot history for maximum traction.",
    image="mte_dx_1.png",
    price=94.99,
    stock=420,
)

Item.objects.create(
    name="Kids Old Skool V",
    desc="The Old Skool V, Vans classic skate shoe and the first to bare the iconic side stripe, is tooled especially\
    for kids with hook and loop closures in place of laces for easy on-and-off.",
    image="old_school_v.png",
    price=39.99,
    stock=14,
)

Item.objects.create(
    name="Mid Slip SF MTE",
    desc="The Mid Slip SF MTE is a mid top slip-on silhouette designed for the elements. Featuring water-repellant\
    leather uppers, warm linings, and a heat retention layer between sockliner and outsole to keep feet warm and dry.",
    image="mid_slip_1.png",
    price=89.99,
    stock=24,
)

Item.objects.create(
    name="Flipping Sequins Slide-On",
    desc="Offering ultimate comfort and all-day ease, the Flipping Sequins Slide-On sandal features synthetic leather\
    straps with foam-backed soft stretch textile linings and adjustable sequins.",
    image="flipping_sequins.png",
    price=44.99,
    stock=25,
)
