# Rust - Primitive Types [&#128279;](https://doc.rust-lang.org/book/primitive-types.html)

Primitive types are types built into the language. The standard library does build on some of them, but below are the most primitive.

## Booleans
- name: `bool`
- values: `true` and `false`
```rust
let x = true;

let y:bool = false;
```

## Char
- created with a single tick (`'`)
- `char` is a single character
- a `char` 4 bytes not 1
```rust
let x = 'x';
let two_hearts = '💕';
```

## Numberic types
- categories: signed & unsigned, fixed & variable, floating-point & integer.
- types are built of 2 parts, the category and the size. `u16` is an unsigned type with 16 bits of size. The more bits lets you have larger numbers.
```rust
// default inference
let x = 42; // x: i32
let y = 1.0; // y: f64
```

Different numeric types avaliable
- i8, i16, i32, i64
- u8, u16, u32, u64
- isize, usize
- f32, f64

### x-bit numbers
- 4  => 2^4 
    - u0 - 15
    - i-8 - +7
- 8  => 2^8
    - u0 - 254 
    - i-128 - +127
- 16 => 2^16
    - u0 - 65,536
    - i-32,768 - +32,767
- 32 => 2^32
    - u0 - 4,294,967,295
    - i-2,147,483,648 - +2,147,483,647
- 64 => 2^64 
    - Big numbers :P

### Signed and Unsigned
Unsigned numbers are integers, signed numbers range from - to +. However this means that an unsigned number of the same bit as a signed number can be double the size. eg. unsigned: 0-15, signed: -8-+7.

### Fixed-size types
Fixed size types have a specific number of bits in their representation, valid options are: 8, 16, 32, 64. u32 is an unsigned 32-bit int and i64 is a signed 64-bit number.

### Variable-size types
Types whos size depends on the underlying machine architecture, their range is enought o express the size of any collection, so they have size as the category and come signed and unsigned.

### Floating-point types
2 floating point types: f32 and f64. These correspond to 'IEEE-754 single and double precision numbers' <-- Google :P.

## Arrays
- By default arrays are immutable.
- Arrays have type [T; N]
```rust
let a = [1,2,3]; // a: [i32; 3]
let mut m = [1,2,3] // m: [i32; 3]
```
- Shorthand for initilizing each element of an array to the same value:
```rust
let a = [0; 20]; // a: [i32, 20]
```
- Get the number of elements in an array with a.len():
```rust
let a = [1,2,3];

println!("a has {} elements", a.len());
```
- you can access a specific element with *subscript notation*
- if you try to access a subscript that is not in the array you will get an error
```rust
let names =["Bob", "Dave", "Nick"]; // names: [&str; 3]

println!("The second name is: {}", names[0]);
```

## Slices
A slice is a refrence to or a "view" into another data structure.
- Useful for a safe efficient access to a portion of an array without copying
- Slices have a defined length and can be mutable or immutable
- Internally slices are represented as a pointer to the beginning of the data and the length

### Slicing syntax
- Slices have type `&[T]`
- `&` indicates that slices are similar to [references]()
- `[]` allow you to define the range of the slice
```rust
let a = [0, 1, 2 ,3, 4];
let complete = &a[..]; // a slice containing everything in a
let middle = &a[1..4]; // a slice taking only the elements 1, 2 & 3
```

## str
- str is the most primitive string type
- it is an unsized type
- it is not very useful by itself but useful when placed behind a reference

## Tuples
- Ordered list of fixed size.
- Tuples are *heterogeneous*: we can have multiple types in the same tuple
- For now read `&str` as a *string slice* (tbc)
```rust
let x = (1, "hello"); // unannotated

let x: (i32, &str) = (1, "hello"); // annotated
```
- You can assign one tuple to another if they have the same types and *arity*
- Tuples have the same arity when they have the same length.
```rust
let mut x = (1, 2); // x: (i32, i32)
let y = (2, 3); // y: (i32, i32)

x = y;
```
- You can access fields in a tuple through a *destructuring let*:
```rust
let (x, y, z) - (1, 2, 3);

println!("x is {}", x);
```
- A single value in a parenthesis vs a single element tuple:
```rust
(0,); // Single element tuple
(0); // 0 in parenthsis
```

### Tuple Indexing
- You can access fields of a tuple with indexing:
```rust
let tuple = (1, 2, 3);

let x = tuple.0;
let y = tuple.1;
let z = tuple.2;

println!("x is {}", x);
```

## Functions
- Functions have a type:
```rust
fn foo(x: i32) -> i32 { x }

let x: fn(i32) -> i32 = foo; // type definition `fn(i32) -> i32`
```