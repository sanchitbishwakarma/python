# Flask Exam Quick Note

**Secret key is important** for `session` and `flash()`:

```py
import os

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
```

### Functions to remember

```py
# Get form data
name = request.form.get("name", "").strip()

# Set session
session["user"] = user

# Get session
user = session.get("user")

# Flash message
flash("Message", category="success")

# Redirect
return redirect(url_for("home_page"))

# Generate route URL
url_for("registration_form")

# Render HTML template
return render_template("registration-form.html")
```

### Exam flow

```text
request.form
     ↓
validate
     ↓
flash() if error
     ↓
session["user"] = user
     ↓
redirect()
     ↓
session.get("user")
```

**Age validation:**

```py
if not 16 <= age <= 60:
    flash("Allowed age is 16-60")
```

**Remember:** `session` and `flash()` require Flask's secret key.
