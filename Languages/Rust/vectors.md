# Rust - Vectors [&#128279;](https://doc.rust-lang.org/book/vectors.html)

A vector is a dynamic or 'growable' array, implimented as type `Vec<T>` (standard library).
- `T` allows vectors of any type
- Vectors allocate their data on the heap.
- Create with `vec!` macro
```rust
// Basic vec
let v = vec![1, 2 ,3 ,4 ,5]; // v: Vec<i32>

// Repeating initial value
let v = vec![0; 10]; // vector of 10 0's
```
*note: you can use either `[]` or `()` with macros, but `[]` is convention with `vec!`*
- vectors must know the size of T at the compile time, if this will not work then you need to store a pointer to that thing. The `box` Type works for this.

## Accessing elements
- `[]`s used to get a specific index
```rust
let v = vec![1, 2, 3, 4, 5];

println!("The third element of v is {}", v[2]);

// NOTE: the index must be of usize type
let i: usize = 0;
let j: i32 = 0;

v[i]; // Works
v[j]; // Doesn't work
```

## Out-of-bounds Access
- use `get` or `get_mut` to get an index without panicing if it does not exist. These functions return `None` if given an invalid index.
```rust
let v = vec![1, 2, 3];
match v.get(7) {
    Some(x) => println!("Item 7 is {}", x),
    None => println!("Sorry, this vector is too short")
}
```

## Iterating
- You can loop through a vectors elements with `for`.
- There are 3 different ways to do this:
```rust
// Reference
let mut v = vec![1, 2, 3, 4, 5];

for i in &v {
    println!("A reference to {}", i);
}

// Mutable Reference
for i in &mut v {
    println!("A mutable reference to {}", i);
}

// Take ownership(???) of the vector and its elements
for i in v {
    println!("Take ownership of the vector and its element {}", i);
}
```
- **If you take ownership of a vector you cannot iterate it again, by reference you can iterate multiple times.**

## Read More:
- [API Documentation](https://doc.rust-lang.org/std/vec/)

