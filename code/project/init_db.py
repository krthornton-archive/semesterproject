from app.models import Item

# add some items
Item.objects.create(name="Forgotten Bones", desc="This is a description.",
                    image="forgotten_bones_1.jpg", price=5.99, stock=12)
