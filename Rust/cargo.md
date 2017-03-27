# Rust - Cargo [&#128279;](https://doc.rust-lang.org/book/getting-started.html)

Cargo is Rust's package manager, it handles compilation and downloading & installing dependancies.

## Creating a Cargo Project

Project Folder Structure:
```
src
- main.rs (for executable projects)
- lib.rs (for libraries)
Cargo.toml (cargo configuration file)
```

Configuration File (Cargo.toml):
```toml
[package]

name = "project_name"
version = "0.0.1"
authors = [ "Author Name <author email>" ]
```

Quick Skeleton project:
- `cargo new project_name --bin` \
creates a new project with basic configuration for an executable project

## Building & Running a Cargo Project
- Building: `cargo build`
- Running: `./target/debug/project_name` 
- Build & Run: `cargo run`

### Building for production
- Building: `cargo build --release` \
this provides multiple optimisations over the developer build, however is a slower process.