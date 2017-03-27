# Rust - Functions [&#128279;](https://doc.rust-lang.org/book/functions.html)

Main function is the most important one as it is the entrance to our app
```rust
fn main() {
}
```

A simple function decloration that prints the sum of 2 numbers.
- Unlike `let` you must declare the types of funciton arguments.
```rust
fn main() {
    print_sum(5, 6);
}

fn print_sum(x: i32, y: i32) {
    println!("sum is: {}", x + y);
}
```

Returning a value
- Returns exactly one value
- You declare the type after `->`
- The last line of a function determines what it returns
- To return leave out the `;`
```rust
fn add_one(x: i32) -> i32 {
    x + 1
}
```

## Expressions vs. Statements
- Rust is primarily an expression-based language. There are 2 statements but everything else is an expression.
- An expression returns a value, a statement does not.

**Declareation Statements**
- `let` is *not* an expression, it will produce a compile time error if used as though it is
```rust
x = y = 5 // will not work

let x = (let y = 5); // will not work
```
- assigning to an already-bound variable is still an expression, unlike other languages the value of an assignment is an empty tuple `()` because the assigned value can have [only one owner](??).
```rust
let mut y = 5;

let x = (y = 6); // `x` has the value `()` not `6`
```

**Expression statements**
- Turns any expression into a statement.
- Rust's grammar expects statements to follow other statements.
- You use semicolons to seperate expressions from each other
```rust
fn add_one(x: i32) -> i32 {
    x + 1 // with the `;` would return `()` however without returns the sum
}
```

## Early returns
- you can use a return on the last line, but it is considered bad practice.
```rust
fn foo(x: i32) -> i32 {
    return x;

    // this code never runs
    x + 1
}
```

## Diverging functions
- `!` function return is known as 'diverges'.
- A diverging function can be used as any type (?? odd)
```rust
fn diverges() -> ! {
    // Panic causes a crash and will never return
    panic!("This function never returns!");
}
```

## Function pointers
- You can create a variable binding which point to a function
```rust
fn plus_one(o: i32) -> i32 {
    i + 1
}

// without type inference
let f: fn(i32) -> i32 = plus_one;

// with type inference
let f = plus_one;

let six = f(5);
```