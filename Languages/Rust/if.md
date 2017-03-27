# Rust - If [&#128279;](https://doc.rust-lang.org/book/if.html)

- Simmilar to dynamic language `if`
```rust
let x = 5;

if x == 5 {
    println!("x is five!");
} else if x == 6 {
    println!("x is six!");
} else {
    println!("x is not five :(");
}
```
- Shorthand:
```rust
let x = 5;

let y = x == 5 { 10 } else { 15 }; // y: i32
```
- If is an expression, the value of the expression is value of the last expression in the chosen branch.
- If without an else is always `()`