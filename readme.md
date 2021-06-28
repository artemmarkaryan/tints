# Tints
## Routes 
<details>
<summary>see</summary>

### Product

`GET /product/all`
[ссылка](http://80.78.246.133:8000/product/all)
```
{
	data: {
		categories: [Category]
	}
}
```


`GET /product/bestsellers`
`GET /product/all`
[ссылка](http://80.78.246.133:8000/product/bestsellers)

```
{
	data: {
		products: [SkuPreview]
	}
}
```

`GET /product/category/<int:categoryId>`
[ссылка](http://80.78.246.133:8000/product/category/1)

```
{
	data: {
		categories: Category
	}
}

```


`GET /shade/all`
[ссылка](http://80.78.246.133:8000/shade/all)
```
{
	data: {
		shades: [Shade]
	}
}

```


`GET /category/all/preview`
[ссылка](http://80.78.246.133:8000/category/all/preview)
``` 
{
	data: {
		categoryPreviews: [CategoryPreview]
	}
}
```


`GET /product/<int:id>`
[ссылка](http://80.78.246.133:8000/product/1)
```
{
	data: {
		product: Product
	}
}
```

### Banner
`GET /banner/all`
[ссылка](http://80.78.246.133:8000/banner/all)
```
{
	data: {
		banners: Banner
	}
}
```

### Review (Отзывы покупателей)
`GET /review/all`
[ссылка](http://80.78.246.133:8000/review/all)
```
{
	data: {
		reviews: [Review]
	}
}
```

### Feedback
`POST /feedback`
[ссылка](http://80.78.246.133:8000/feedback)
```
request: {
    contact: string 
    text: string 
}
```

### Newsletter
`POST /newsletter`
[ссылка](http://80.78.246.133:8000/newsletter)
```
request: {
    email: string
}
```

</details>

### Order
`POST /order`
```
request: NewOrder
responce: 
200: OK
data: {
    orderId:    int
    key:        string 
}
400: Неправильные параметры
```

`GET /order/<order_id>?key=<order_key>`
```
responce:
200: OK
data: {
    Order
}
404: Нет такого ордера или неправльный ключ
```

`GET /order/<order_id>/paymentURL?key=<order_key>`
```
responce:
200: OK
data: {paymentURL: string}
404: Нет такого ордера или неправльный ключ
```

### Shipping method
`GET /shippingMethod/all`
```
responce
data: {
    id:             int
    description:    string
    name:           string
    price:          float
}
```

### Payment method
`GET /paymentMethod/all`
```
responce
data: {
    code:           string
    description:    string
}
```


## DTO 
<details>
<summary>see</summary>

```
Banner
{
    title: string
    text: string
    image: string
    buttonText: string
    buttonUrl: string
}
```

```
CategoryPreview
{
    id: int
    name: string
    translit: string
}
```

```
Category
{
    id: int
    name: string
    translit: string
    sku: [SkuPreview]
}
```

```
SkuPreview
{
    id: int
    productId: int
    categoryId: int
    name: string
    translit: string
    vendorCode: string
    oldPrice: number
    price: number
    image: string
    new: bool 
    top: bool
    shadeId: int
}

```

```
Sku
{
    id: int
    productId: int
    categoryId: int
    name: string
    translit: string
    vendorCode: string
    oldPrice: number
    price: number
    images: [string]
    new: bool 
    top: bool
    shadeId: int
}
```

```
Product
{
    id: int
    categoryId: int
    name: string
    translit: string
    description: string
    info: [Info]
    sku: [Sku]
    related: [SkuPreview]
}
```

```
Info
{
    title: string
    text: string
}
```

```
Shade
{
    id: int
    image: string
    name: string
}
```

```
Review
{
    title: string
    author: string
    url: string
    date: string
    description: string
}
```

```
NewOrder - отправляете на сервер при создании заказа 
name:               string
email:              string
phone:              string
comment:            string
paymentMethodCode:  string
shippingMethodId:   int
items:              [NewItem]
```

```
Order - получаете с сервера для отображения на странице заказа
name:               string
email:              string
phone:              string
address:            string
comment:            string
shippingDate:       string
shippingTime:       string
paymentMethod:      string
shippingMethod:     string
shippingPrice:      float
items:              [Item]
itemsPrice:         float
fullPrice:          float
status:             string
canPay:             bool
```

```
NewItem - отправляете на сервер при создании заказа
skuId:          int
quantity:       int
```

```
Item - получаете с сервера для отображения на странице заказа
skuId:          int
name:           string
quantity:       int
price:          float
```

</details>