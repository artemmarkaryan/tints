# Tints
## Database models
- [x] Category
	- id: int
	- name: string
	- translitName: string

- [x] Shade
	- id: int
	- image: string

- [x] Product
	- id: int
	- name: string
	- translitName: string
	- description: string
	- shade: int
	- new: bool
	- top: bool

- [x] ProductInfo
	- id: int
	- product: int
	- title: string
	- text: string

- [x] SKU
	- id: int
	- name: string
	- product: int
	- translitName: string
	- vendorCode: string
	- oldPrice: float
	- price: float
	- weight: int

- [x] SKUImage
	- id: int
	- SKU: int
	- image: string

- [ ] Article
- [ ] AboutArticle
- [ ] AdviceArticle