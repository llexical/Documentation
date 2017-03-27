# Rust - Comments [&#128279;](https://doc.rust-lang.org/book/comments.html)

**Line Comments**
```rust
// line comment
```

**Doc Comments**
```rust
/// A doc comment
/// 
/// # Example
/// - Accepts markdown

//! # Crate/Module/Library 
//! 
//! Description here of crate/module/library
//!
//! ```
//! let five = 5;
//!
//! assert_eq!(6, add_one(5));
//!
//! # fn add_one(x: i32) -> i32 {
//! #   x + 1
//! #}
//! ```
```
- Doc comments can be used to generate HTML documentation from these docs
- Also the code examples can be run as tests!