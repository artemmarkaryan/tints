# Tints
## Database models
- [ ] Category
	- id: int
	- name: string
	- translitName: string

- [ ] Product
	- id: int
	- name: string
	- translitName: string
	- description: string
	- shade: int
	- new: bool
	- top: bool

- [ ] Shade
	- id: int
	- image: string

- [ ] ProductInfo
	- id: int
	- product: int
	- title: string
	- text: string

- [ ] SKU
	- id: int
	- name: string
	- vendorCode: string
	- oldPrice: float
	- price: float
	- weight: int

- [ ] SKUImage
	- id: int
	- SKU: int
	- image: string

- [ ] Article
- [ ] AboutArticle
- [ ] AdviceArticle