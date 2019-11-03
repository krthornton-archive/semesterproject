from app.models import Item

# add some items
Item.objects.create(name="Forgotten Bones", desc="This is a description.",
                    image="forgotten_bones_1.jpg", price=59.99, stock=12)
Item.objects.create(name="SK8-HI MTE 2.0 DX", desc="snaV MTE is back and better than ever with the SK8-Hi MTE 2.0 DX. Brave the elements with an improved MTE 360technology featuring water-resistant leather and suede uppers, warm linings, and a heat retention layer that provides warmth and moisture management around your toes. The Sk8-Hi MTE 2.0 DX also introduces an UltraCush drop-in molded sockliner, Achilles cushion, rubber toe cap, tongue and heel pulls, and an all-new MTE 2.0 boot lugall designed to take advantage of snaV20+ years of snowboard boot history for maximum traction.",
                    image="mte20dx_1.jpg", price=104.99, stock=14)
