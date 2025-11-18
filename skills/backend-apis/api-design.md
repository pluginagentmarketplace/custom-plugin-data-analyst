---
name: api-design
description: Master REST API design, GraphQL, API security, authentication, rate limiting, and API documentation. Learn OpenAPI/Swagger specifications.
---

# API Design Best Practices

## REST API Design

### Resource-Oriented Design

```
GET    /api/users              # List users
POST   /api/users              # Create user
GET    /api/users/:id          # Get user
PUT    /api/users/:id          # Update user
DELETE /api/users/:id          # Delete user
```

### Request/Response Format

```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "John",
    "email": "john@example.com"
  },
  "meta": {
    "timestamp": "2024-01-01T00:00:00Z"
  }
}
```

## HTTP Status Codes

| Code | Meaning | Example |
|------|---------|---------|
| 200 | Success | GET request successful |
| 201 | Created | Resource created |
| 400 | Bad Request | Invalid parameters |
| 401 | Unauthorized | Missing auth token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 500 | Server Error | Internal error |

## API Authentication

### JWT (JSON Web Token)

```javascript
// Generate token
const token = jwt.sign({ userId: 123 }, 'secret_key');

// Verify token
const decoded = jwt.verify(token, 'secret_key');
```

### OAuth 2.0
Standard protocol for third-party authentication

## API Documentation (OpenAPI)

```yaml
openapi: 3.0.0
info:
  title: User API
  version: 1.0.0

paths:
  /users:
    get:
      summary: List all users
      responses:
        '200':
          description: Successful response
```

## Security Best Practices

✅ Use HTTPS always
✅ Implement rate limiting
✅ Validate all inputs
✅ Use API keys/tokens
✅ Implement CORS properly
✅ Log API access
✅ Monitor unusual activity

## GraphQL Alternative

```graphql
query GetUser {
  user(id: 1) {
    id
    name
    email
    posts {
      title
    }
  }
}
```

### GraphQL Benefits
✅ Query exactly what you need
✅ Single endpoint
✅ Reduces over/under-fetching
✅ Self-documenting

## API Versioning

```
/api/v1/users    # Version 1
/api/v2/users    # Version 2
```

## Next Steps

1. Design API schema
2. Implement endpoints
3. Add authentication
4. Document with OpenAPI
5. Test thoroughly
