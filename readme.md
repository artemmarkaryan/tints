# Tints
<details>
<summary>Database models</summary>

```
Category
- id: int
- name: string
- translitName: string
```

```
Shade
- id: int
- image: string
```

```
Product
- id: int
- name: string
- translitName: string
- description: string
- shade: int
- new: bool
- top: bool
```

```
ProductInfo
- id: int
- product: int
- title: string
- text: string
```

```
SKU
- id: int
- name: string
- product: int
- translitName: string
- vendorCode: string
- oldPrice: float
- price: float
- weight: int
```

```
SKUImage
- id: int
- SKU: int
- image: string
```

```
Review
- id: int
- date: string
- title: string
- url: string
- author: string
- pros: string
- cons: string
```

```
Article
- id: int
- title: string
- image: string
- description: string
- text: string

AboutArticle(Article)

AdviceArticle(Article)
```

```
Banner
- id: int
- title: string
- text: string
- image: string
- buttonText: string
- buttonUrl: string
```
</details>

<details>
<summary>Routes</summary>

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
```
{
	data: {
		products: [Sku]
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
		sahdes: [Shade]
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


</details>

<details>
<summary>DTO</summary>

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
	sku: [Sku]
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
	image: string
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
	related: [Sku]
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
}
```


</details>
