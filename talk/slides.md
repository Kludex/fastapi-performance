---
theme: gaia
class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
footer: "@marcelotryle"
marp: true
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
---

## Performance Tips with the FastAPI Expert

![bg:40% 80%](assets/marcelo.png)
Marcelo Trylesinski

---

# About me

![w:600](https://live.staticflickr.com/4458/37545736336_93f1591985_b.jpg)

---

## FastAPI Expert

![w:950 center](assets/fastapi-expert.png)


---

## OSS Maintainer

<div class="columns">
<div>

### Uvicorn

![w:450](https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png)

</div>
<div>

### Starlette

![w:600](https://www.starlette.io/img/starlette.png)

</div>
</div>


---

## Performance Tips

![w:400](assets/fastapi.svg)


---

## Simple Application

![w:800](assets/simple.svg)

---

## Simple Application

https://json-generator.com/

https://jsontopydantic.com/

---

## Simple Application

# requests | req/s
--- | ---
9990 | 334.37

---

## Use uvloop

![w:800](assets/uvloop.png)

---

## Use uvloop

<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Simple App + uvloop

# requests | req/s
--- | ---
11256 | 376.71

</div>
</div>

### **~12%**

---

### Use uvloop

![w:500](assets/pip-uvloop.svg)

---

### Use httptools

Python binding for the nodejs HTTP parser

---

### Use httptools


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Simple App + httptools

# requests | req/s
--- | ---
11040 | 369.32

</div>
</div>

### **~10%**

---

### Use httptools

![w:500](assets/pip-httptools.svg)

---

### Bigger Threadpool

![w:800](assets/threadpool.svg)

---

### Bigger Threadpool


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Increasing Threadpool

# requests | req/s
--- | ---
11014 | 368.44

</div>
</div>

### **~10%**

---

### Simple Async Application

![w:800](assets/simple-async.svg)

---

### Simple Async Application


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Simple Async App

# requests | req/s
--- | ---
11470 | 383.72

</div>
</div>

### **~15%**

---

### Duplicated validation

![w:800](assets/convert-once.svg)

---

### Duplicated validation


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Single Validation

# requests | req/s
--- | ---
13449 | 449.90

</div>
</div>

### **~35%**

---

### Use ORJSON

![w:800](assets/orjson.svg)

---

### Use ORJSON


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Using ORJSON

# requests | req/s
--- | ---
14441 | 483.09

</div>
</div>

### **~45%**

---

### Without Validation

![w:600](assets/without-validation.svg)

---

### Without Validation


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Without Validation

# requests | req/s
--- | ---
28664 | 958.86

</div>
</div>

### **~187%**

---

### Without Logging

![w:800](assets/without-logging.svg)

---

### Without Logging


<div class="columns">
<div>

### Simple App

# requests | req/s
--- | ---
9990 | 334.37

</div>
<div>

### Without Logging

# requests | req/s
--- | ---
10884 | 364.12

</div>
</div>

### **~9%**

---

### Bonus: Use ASGI Middleware

![w:1000](assets/base-http-middleware.png)

---

### Bonus: Use ASGI Middleware

![w:1000](assets/http-middleware.svg)

---

### Bonus: Use ASGI Middleware

![w:700](assets/asgi-middleware.svg)

---

### Bonus: Use ASGI Middleware

Read about **ASGI Pure Middleware** on:

https://www.starlette.io/middleware/

---

### Bonus: Compressing Responses

![w:800](assets/gzip-middleware.svg)

---

# Thank You!

## Questions?

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />


<i class="fab fa-linkedin"></i> Marcelo Trylesinski
<i class="fab fa-twitter"></i> @marcelotryle
<i class="fab fa-github"></i> Kludex


<i class="fas fa-heart"></i> github.com/sponsors/Kludex
