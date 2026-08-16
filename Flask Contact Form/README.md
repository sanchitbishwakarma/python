```html
{% if error %}
    <p>{{ error }}</p>
{% endif %}
```

Remember:

* `{% ... %}` → **Jinja logic** (`if`, `for`, etc.)
* `{{ ... }}` → **display a value** (`error`, `name`, etc.)
