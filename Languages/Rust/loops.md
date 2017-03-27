# Rust - Loops [&#128279;](https://doc.rust-lang.org/book/loops.html)

Iterative options:
- `loop`
- `while`
- `for`

## Loop
- Infinate loop is the simpliest in Rust
- Infinate loop & `while true {}` are treated differently, you should always use `loop` in this instances
```rust
loop {
    println!("Loop forever!");
}
```

## While
- `while` is good for if you do not know how many times you will need the loop
```rust
let mut x = 5; // mut x: i32
let mut done = false; // mut done: bool

while !done {
    x += x - 3;

    println!("{}", x);

    if x % 5 {
        done = true // breaks the loop
    }
}
```

## For
- For looping a specific number of times.
- The expression needs to be able to be converted into an interator using `IntoIterator`
```rust
// for var in expression {}
// The upper bound is exclusive though so loop will print 0-9
for x in 0..10 {
    println!("{}", x);
}
```

### Enumerate
- Helps you keep track of how many times you have looped
```rust
// Ranges
for (index, value) in (5..10).enumerate() {
    println!("index = {} and value = {}", index, value);
}

// iterators
let lines = "hello\nworld".lines()

for (linenumber, line) in lines.enumerate() {
    println!("{}: {}", linenumber, line);
}
```

## Ending iteration manually
- `break`
- `continue`
- `return`

```rust
// instead of while shown above
let mut x = 5;

loop {
    x += x - 3;

    println!("{}", x);

    if x % 5 == 0 { break; }
}
```

## Loop labels
- Allows you to continue iteration over your choosen loop
```rust
'outer: for x in 0..10 {
    'inner: for y in 0..10 {
        if x % 2 == 0 { continue 'outer; } // Continues the loop over `x`.
        if y % 2 == 0 { continue 'inner; } // Continues the loop over `y`.
        println!("x: {}, y: {}", x, y);
    }
}
```