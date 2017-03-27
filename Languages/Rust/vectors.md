# Rust - Vectors [&#128279;]()

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
- use `get` or `get_mut` to get an index without panicing if it does not exist.