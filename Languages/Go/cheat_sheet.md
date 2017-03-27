# Go - Cheat Sheet

## Basics
```go
var Foo int    // set variable with type
Foo = 1        // assign value to foo
bar := Foo     // type inference & assign
&Foo           // pass reference
Bar{}          // new struct
```

## Basic Types
```go
int             // 234
string          // “Hello” double quotes only!
float32         // 2.33F
bool            // true / false

[]int           // array
map[string]int  // map define 
interface{}     // interface as a basic can hold any type of data, but not access it easily

interface       // Interface when used in inheritance
struct          // Basic ‘object’ type
```

## Exports
```go
package ‘main’  // is the main function exported as an executable not importable
package ‘foo’   // creates a package (namespace in C)
type Barr int   // exportable value
type barr int   // un-exportable value
```

## Imports
```go
// Single import
import ‘github.com/user/repo'

// Multi Import
import (
     ‘fmt’                                        // core package import
 
     ‘github.com/user/repo'                       // git repo containing a go package
     random_package ‘github.com/user2/repo2'      // go package with custom name
)
```

## Functions
```go
// Basic function
func Foo (input []string) int {
     return len(input)
}

// Function with multiple outputs
func Foo (input []string) (int, error) {
     // Do stuff here ( you must always return 2 outputs from this function )
}
```

## Structs
```go
// Struct with method
type Item struct {
     Cost      float32 // public
     count     int     // private
     barString string  // private
}

func (i *Item) CostWithVat(vat float32) float32 {
     return i.Cost * vat
}

// Referencing other struct
type Basket struct {
     Items []*Item     // referencing an array of other structs
}
```

## Interfaces - *NEED TO LEARN MORE*
```go
// Struct and Interface
type Human interface {
     SayHi()
     Gender
}

type Person struct {
     Human Human    
}

func (p *Person) SayHi() {
     fmt.Println(‘Hi!’)
}
```