# Rust - Variable Bindings [&#128279;](https://doc.rust-lang.org/book/variable-bindings.html)

- [Official Docs](https://doc.rust-lang.org/book/variable-bindings.html)

## Variable Bindings
A basic variable binding:
```rust
let x = 5
```

## Patterns
The left hand side of the statement is a 'pattern' not a variable name allowing things like this:
```rust
let (x, y) = (1, 2)
```

## Type Annotations
- Statically typed language (duh :P)
- Rust has 'type inference' so it can figure it out

If you want to explicity add types, place them after colon:
```rust
let x: i32 = 5; // i32 is a 32-bit signed integer
```

## Mutability
- Default: variable bindings are *immutable*

To make a variable mutable you can use `mut`:
```rust
// Incorrect: throws error
let x = 5;
x = 10

// Correct: will update value
let mut x = 5; // mut x: i32
x = 10;
```

Saftey is the main reason that bindings are immutable by default, if you forget to add `mut` the compiler will inform you and you can check if you intended that variable binding to be mutable or not.

> "It is preferable avoid explicit mutation ... that being said, sometimes, mutation is what you need so it is not forbidden" - Rust docs

## Initializing bindings

Bindings must be initialized with a value before you are allowed to use them
```rust
// Warning: unused variable
let x: i32 

// Incorrect: throws an error
let x: i32;
println!("The value of x is: {}, x);
```

## Scope and shadowing

Variables are constrained to the block they are defined in `{ ... }`, function definitions are also blocks.

```rust
fn main() {
    let x: i32 = 17;
    {
        let y: i32 = 3;
        println!("x: {}, y: {}", x, y); // Correct
    }
    println!("x: {}, y: {}", x, y); // Incorrect: Scope error
}
```

Variable bindings can be *shadowed*. Bascially meaning you can define a variable with the same name as another binding in the same scope and override it.

```rust
let x: i32 = 8; // x = 8
{
    let x = 54; // x = 54
}
// x = 8
let x = 42; // x = 42
```

Shadowing and mutable bindings seem simmilar however they are 2 different concepts and cannot always be used interchangably. 
- Shadowing allows you to bind name to a value to a different type 
- Shadowing does not alter or destroy the value it was bound to and the value will continue to exist until it goes out of scope. *??? I feel this is important - TBC :P*

```rust
let mut x: i32 = 1;
x = 7;
let x = x; // `x` is now immutable and bound to '7'.

let y = 4;
let y = "I can also be bound to text"; // `y` is now a different type
```