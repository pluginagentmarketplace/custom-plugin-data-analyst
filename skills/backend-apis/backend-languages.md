---
name: backend-languages
description: Master backend programming languages: Node.js, Python, Go, Rust, PHP, Java. Learn language basics, frameworks, and when to use each language.
---

# Backend Programming Languages

## Language Selection Guide

### Node.js/JavaScript
**Best for:** Real-time apps, JavaScript everywhere, rapid development

```javascript
// Express.js example
const express = require('express');
const app = express();

app.get('/api/users', async (req, res) => {
  const users = await db.users.find();
  res.json(users);
});

app.listen(3000);
```

### Python
**Best for:** Data processing, ML, rapid development

```python
from flask import Flask

app = Flask(__name__)

@app.route('/api/users', methods=['GET'])
def get_users():
    users = db.users.find()
    return jsonify(users)

if __name__ == '__main__':
    app.run(port=3000)
```

### Go
**Best for:** High performance, concurrency, cloud native

```go
package main

func getUsers(w http.ResponseWriter, r *http.Request) {
    users := db.FindUsers()
    json.NewEncoder(w).Encode(users)
}

func main() {
    http.HandleFunc("/api/users", getUsers)
    http.ListenAndServe(":3000", nil)
}
```

### Rust
**Best for:** Systems programming, extreme performance

```rust
use actix_web::{web, App, HttpServer, HttpResponse};

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new()
            .route("/api/users", web::get().to(get_users))
    })
    .bind("127.0.0.1:3000")?
    .run()
    .await
}
```

### Java
**Best for:** Enterprise, type safety, scalability

```java
@RestController
@RequestMapping("/api")
public class UserController {
    @GetMapping("/users")
    public List<User> getUsers() {
        return userService.getAllUsers();
    }
}
```

## Language Comparison

| Language | Learning | Performance | Ecosystem | Use Case |
|----------|----------|-------------|-----------|----------|
| **Node.js** | Easy | Good | Massive | Real-time |
| **Python** | Easy | Moderate | Excellent | Data/ML |
| **Go** | Medium | Excellent | Growing | Cloud |
| **Rust** | Hard | Best | Growing | Systems |
| **Java** | Hard | Excellent | Massive | Enterprise |

## Package Managers

- **Node.js**: npm, yarn, pnpm
- **Python**: pip, conda, poetry
- **Go**: go get, go mod
- **Rust**: cargo
- **Java**: Maven, Gradle

## Best Practices

✅ Use async/await for I/O
✅ Implement proper error handling
✅ Log appropriately
✅ Validate all inputs
✅ Use environment variables
✅ Write tests
✅ Document APIs

## Next Steps

1. Choose one language
2. Learn fundamentals
3. Build REST API
4. Add database integration
5. Deploy to production
