### Question requires

1. **`/login` route**

   * Validate submitted username and password.

2. **Session management**

   * Store the username after successful authentication.

3. **Protected `/dashboard`**

   * Read from the session.

4. **`/logout` route**

   * Clear the active session.
   * Redirect to login.

5. **HTML template snippets**

   * Login/dashboard templates.

### What you did

| Requirement                | Your code                       | Status |
| -------------------------- | ------------------------------- | ------ |
| `/login`                   | `@app.route("/login"...`        | ✅      |
| Validate username/password | Checks against `database`       | ✅      |
| Session after login        | `session["user"] = {...}`       | ✅      |
| Store username             | `username` is stored in session | ✅      |
| Protected dashboard        | Checks `session.get("user")`    | ✅      |
| Dashboard reads session    | Passes `user` to template       | ✅      |
| `/logout`                  | `@app.route("/logout"...`       | ✅      |
| Clear session              | `session.pop("user", None)`     | ✅      |
| Redirect to login          | `redirect(url_for("login"))`    | ✅      |
| HTML snippets              | Login + dashboard templates     | ✅      |

**Verdict: Your solution satisfies the question.** ✅
