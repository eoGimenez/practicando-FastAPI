from fastapi import APIRouter
from fastapi.responses import Response, HTMLResponse, PlainTextResponse
from typing import Optional

# Custom response
router = APIRouter(
    prefix='/product',
    tags=['product']
)

products = ["Reloj", "TV", "Radio"]


@router.get('/')
def get_products():
    # return products
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


# @router.get('/withheader')
# def get_products(response: Response,
#                  custom_header: Optional
#                  ):


@router.get('/{id}', responses={
    200: {
        "content": {
            "text/html": {
                "example": "<div>Product</div>"
            }
        },
        "description": "Return the HTML for an object"
    },
    404: {
        "content": {
            "text/plain": {
                "example": "Product not available"
            }
        },
        "description": "A cleartext error message"
    }
})
def get_product(id: int):
    if id > len(products):
        out = 'Product not available'
        return PlainTextResponse(status_code=404, content=out, media_type="text/plain")
    else:
        out = f"""
            <head>
                <style>
                .product {{
                width: 500px;
                height: 30px;
                border: 2px inset green;
                backgound-color: lightblue:
                text-align: center;
                }}
                </style>
            </head>
            <div class='product'> Random Product </div>
        """
        return HTMLResponse(content=out, media_type="text/html")
