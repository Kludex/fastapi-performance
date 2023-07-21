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

## Performance Tips by the FastAPI Expert

![w:300](assets/marcelo.png)
Marcelo Trylesinski

---

# Who am I?

---

![w:750 center](assets/fastapi-logo.png)

---

# OSS Maintainer

<div class="columns">
<div>

## Uvicorn

![w:450](https://raw.githubusercontent.com/tomchristie/uvicorn/master/docs/uvicorn.png)

</div>
<div>

## Starlette

![w:600](assets/starlette-logo.png)

</div>
</div>

---

# Software Engineer @

![w:750](assets/pydantic-logo.svg)

---

# Try Pydantic V2!

![w:1000](assets/pydantic-v2.png)

---

# Data people, help us!

[pydantic.dev/roadmap](https://pydantic.dev/roadmap/)

---

## Performance Tips

![w:400](assets/fastapi.svg)


---

## Simple Application

![w:800](assets/simple.svg)

---

## Simple Application

![w:600](assets/install-fastapi.svg)

---

## Simple Application

https://json-generator.com/

https://jsontopydantic.com/

---

## Use uvloop

![w:800](assets/uvloop.png)

---

## Use uvloop

Improvement of **~10%**

---

### Use uvloop

![w:500](assets/pip-uvloop.svg)

---

### Use httptools

Python binding for the nodejs HTTP parser

---

### Use httptools

Improvement of **~10%**

---

### Use httptools

![w:500](assets/pip-httptools.svg)

---

### Bigger Threadpool

![w:800](assets/threadpool.svg)

---

### Bigger Threadpool


Improvement of **~5%**

---

### Simple Async Application

![w:800](assets/simple-async.svg)

---

### Simple Async Application


Improvement of **~15%**

---

### Duplicated validation

![w:800](assets/convert-once.svg)

---

### Duplicated validation

Improvement of **~25%**

---

### Use ORJSON

![w:800](assets/orjson-code.svg)

---

### Use ORJSON


Improvement of **~5%**

---

### Without Validation

![w:600](assets/without-validation.svg)

---

### Without Validation


Improvement of **~150%**

---

### Without Logging

![w:800](assets/without-logging.svg)

---

### Without Logging


Improvement of **~15%**

---

### Without any of the previous improvements...

Using Pydantic V2...

---

Improvement of **~265%**

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
