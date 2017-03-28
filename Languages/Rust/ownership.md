# Ownership

Ownership is an important Rust feature, which you will be using alot. Ownership allows Rust to handle memory saftey.

- Rust is focused on safety and speed, and it accomplishes this through 'zero-cost-abstractions', meaning the abstractions cost as little as possible to make them work. 
- Ownership is all *done at compile time* so all of this has NO runtime cost
- It can be quite a learning curve (seems worth it to me xD) 'beware the borrow checker' :P

Sections:
- [Ownership]()
- [Borrowing](borrowing,md)
- [Lifetimes](lifetimes.md)

## Ownership
- Variable bindings have a property in Rust, they have 'ownership' of what they are bound to.
- When the binding goes out of scope, Rust will free these bound resources.

E.g:
```rust
fn foo() {
    let v = vec![1, 2, 3];
}
```
- When v comes into scope a new vector is created on **the stack**
- The stack allocates space on **the heap**
- At the end of `foo()`, `v` goes out of scope, Rust cleans up everything related to the vector and also the heap-allocated memory. This happens at the end of each scope.

## Move semantics
- There is exactly ONE binding to any given resource:
```rust
// Variable binding
let v = vec![1, 2, 3];

let v2 = v;

 // would throw an error as the vector has been moved from v to v2
println!("v[0] is: {}", v[0]);

// Function
fn take(v: Vec<i32>) {
    // unimportant
}

let v = vec![1, 2, 3];

take(v);

// would throw an error as v's value's ownership has been moved to the functions variable.
println!("v[0] is: {}", v[0]) 
```

## The Details
You cannot use a binding after you have moved it because:
```rust
let x = 10;
```
- Rust allocates memory for i32 on the stack
- Copies the bit patterns representing 10 to the allocated memory
- Binds the variable name `x` to the memory region for future reference.

```rust
let v = vec![1, 2, 3];

let mut v2 = v;
```
- First line allocates memory for `v` on the stack like it does for `x` above.
- On top of that it also allocates some memory on the heap for the data `([1, 2, 3])`
- Rust copies the address of this heap allocation to an internal pointer, which is part of the vector object placed on the stack.
- **The vector object and its data live in seperate memory reigions.**
- The vector on the stack and its data in the heap must agree at all times regarding: length, capaicty, etc.
- `v` => `v2` Rust does a bitwise copy of the vector object `v` into the stack allocation represented by `v2`
    - This is a shallow copy and does not create a copy of the heap allocation containing the data.
    - 2 pointers would consequently be pointing at the same memory allocation on the heap (violating Rust's saftey guarantees by allowing a [data race](http://blog.regehr.org/archives/490))
    - e.g:
    ```rust
    v2.truncate(2);
    ```
    - We just truncated `v2` to 2 elements, however `v` would be an invalid vector as it wouldn't know the heap data was truncated (so its knowlege of size, length, etc. would be incorrect).
    - Consequently `v` will allow you to access `v[2]` even though it doesn't exist. This is a big issue as it may lead to segmentation fault' or allow an authorised user to read from memory they shouldn't be able to see.
- Optimisations may remove the acual copy of the bytes on the stack, depending on circumstances, so it can be more efficent than it sounds.



