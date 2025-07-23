ecommerce_project/
│
├── manage.py
├── requirements.txt
│
├── ecommerce_project/               # Project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── asgi.py / wsgi.py
│
├── customer/                        # Custom user & addresses
│   ├── models.py                    # CustomUser, CustomerAddress
│   ├── serializers.py               # CustomerSerializer, CustomerAddressSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── products/                        # Product & category
│   ├── models.py                    # Category, Product
│   ├── serializers.py               # ProductListSerializer, ProductDetailSerializer, CategoryListSerializer, CategoryDetailSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── reviews/                         # Reviews & ratings
│   ├── models.py                    # Review, ProductRating (can optionally be kept here)
│   ├── serializers.py               # ReviewSerializer, ProductRatingSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── cart/                            # Cart system
│   ├── models.py                    # Cart, CartItem
│   ├── serializers.py               # CartSerializer, CartItemSerializer, CartStatSerializer, SimpleCartSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── wishlist/                        # Wishlist feature
│   ├── models.py                    # Wishlist
│   ├── serializers.py               # WishlistSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── orders/                          # Order system
│   ├── models.py                    # Order, OrderItem
│   ├── serializers.py               # OrderSerializer, OrderItemSerializer
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── core/                            # Shared utilities
    ├── permissions.py
    ├── pagination.py
    ├── mixins.py
    ├── utils.py
    └── constants.py (optional)
